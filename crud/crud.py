from textual.app import App, ComposeResult
from textual.widgets import Header, LoadingIndicator, Button, Static, Input, Label, TextArea, DataTable, Log, OptionList, LoadingIndicator, RadioButton, RadioSet, RichLog, Tabs, Tab, TabPane, TabbedContent, Markdown
from datetime import datetime
from textual import on, work
from textual.events import Click
import mysql.connector
from textual.containers import ScrollableContainer, Container
CSS_PATH = 'estilos.css'

        
class ConexionSQL(App):
    CSS_PATH = 'estilos.css'
    def __init__(self):
        super().__init__()
        self.user_ = Input("root")
        self.pass_ = Input("1221", id="pass_", password=True)
        self.host_ = Input("127.0.0.1", id="host_")
        self.database_ = Input("northwind", id="database_")
        self.cnx_ = None
        self.log_ = RichLog(highlight=True, markup=True)
        self.tabla_ = DataTable()
        self.tabla_.cursor_type = "row"
        self.tabla_.zebra_stripes = True
        self.opciones_ = OptionList("Conectate primero")
        self.loading_ = LoadingIndicator()
        self.consulta_ = TextArea("jajja", language="python")

    def conex(self) -> None:
       
        yield Label(" Usuario:")
        yield self.user_        
        yield Label(" Contraseña:")
        yield self.pass_
        yield Label(" Host:")
        yield self.host_
        yield Label(" Base de datos:")
        yield self.database_
        yield self.log_
        yield Button("Conectar", id="conexion", variant="success")
        yield Button("Desconectar", id="desconectar", variant="error")
        

    def compose(self) -> ComposeResult:
        with TabbedContent(initial="conex"):
            with TabPane("Conexión SQL", id="conex"):
                yield Container(*self.conex())
            with TabPane("CRUD", id="crud"):
                yield Label(" Menú de tablas")
                yield self.opciones_
                yield self.tabla_ 
                yield self.consulta_
                with RadioSet():
                    yield RadioButton("Eliminar fila", id="delete")#d
                    yield RadioButton("Insertar fila", id="create") #c
                    yield RadioButton("Actualizar valor", id="update")#u            
                    yield RadioButton("Query", id="query")#u       
                    yield RadioButton("No hacer nada", value=True, id="nothing") 
    ##############################################
    async def on_radio_set_changed(self, event: RadioSet.Changed) -> None:
        cambios = [] 
        tabla = str(self.opciones_.get_option_at_index(self.opciones_.highlighted).prompt)
        cursor = self.cnx_.cursor(tabla)
        cursor.execute(f"DESC {tabla}")
        for i in cursor.fetchall():
            cambios.append(str(i[0]))
        if(event.pressed.id == 'create'):
            self.consulta_.text = f"INSERT INTO ({",".join(cambios)})"
        self.log_.write("cambios")
        
            
    @on(Button.Pressed, "#conexion")
    def conectar(self):
        try:
            self.cnx_ = mysql.connector.connect(user= self.user_.value, password = self.pass_.value, host = self.host_.value, database = self.database_.value)
            self.log_.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} Conexión exitosa")
            cursor = self.cnx_.cursor()
            cursor.execute("SHOW TABLES;")
            self.opciones_.clear_options()
            tables = [table[0] for table in cursor.fetchall()]
            for table in tables:
                self.opciones_.add_option(table)       
        except mysql.connector.Error as e:
            self.log_.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} Error al conectarse: {e}")
   
            
    @on(OptionList.OptionHighlighted)
    @work(exclusive=True)
    async def show_selection(self, event: OptionList.OptionHighlighted) -> None:
        if self.cnx_ is not None:
            try:
                cursor = self.cnx_.cursor()
                query = f"SELECT * FROM {self.opciones_.get_option_at_index(self.opciones_.highlighted).prompt}"
                cursor.execute(query)
                self.tabla_.clear(columns=True)
                column_names = [column[0] for column in cursor.description]
                self.tabla_.add_columns(*column_names)  
                self.tabla_.loading = True
                filita = 1  
                while True:
                    rows = cursor.fetchmany(size=50)
                    if not rows:
                        break
                    for row in rows:
                        self.tabla_.add_row(label=filita, *row)
                        filita += 1  

                self.log_.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} Consulta realizada con éxito {self.opciones_.get_option_at_index(self.opciones_.highlighted).prompt}")
                self.tabla_.loading = False
            except mysql.connector.Error as e:
                self.log_.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} Error al ejecutar la consulta: {str(e)}")
        else:
            self.log_.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} No se ha establecido una conexión")            
    
    @on(Button.Pressed, "#desconectar")
    def desconectar(self):
        try:
           self.cnx_.close()
           self.log_.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} Se desconectó correctamente")
        except mysql.connector.Error as e:
            self.log_.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} Hubo problemas al desconectar {e}")

                
if __name__ == "__main__":
    app = ConexionSQL()
    app.run()