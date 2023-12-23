from textual.app import App, ComposeResult
from textual.widgets import Header, LoadingIndicator, Button, Static, Input, Label, TextArea, DataTable, Log, OptionList, LoadingIndicator
from datetime import datetime
from textual import on, work
import mysql.connector
from textual.containers import ScrollableContainer, Container



class conect(Static):
    def compose(self) ->ComposeResult:
        yield Button("Conectar", id="conexion", variant="success")
        yield Button("Desconectar", id="desconectar", variant="error")

class datos(Static):
    def compose(self) -> ComposeResult:
        yield Label("Usuario:")
        user_ = yield Input("root", id="user_")
        yield Label("Contraseña:")
        pass_= yield Input("1221",id="pass_", password=True) 
        yield Label("Host:")
        host_ = yield Input("127.0.0.1",id="host_")
        yield Label("Base de datos:")
        database_ = yield Input("northwind",id="database_")

class ConexionSQL(App):
    
    def __init__(self):
        super().__init__()
        self.user_ = Input("root")
        self.pass_ = Input("1221", id="pass_", password=True)
        self.host_ = Input("127.0.0.1", id="host_")
        self.database_ = Input("northwind", id="database_")
        self.cnx = None
        self.log_ = Log()
        self.tabla = DataTable()
        self.tabla.zebra_stripes = True
        self.opciones = OptionList("Conectate primero")
        self.loading = LoadingIndicator()

    BINDINGS = [("|", "cambiar_tema", "Cambia el tema de pantalla")]
    
    CSS_PATH = 'estilos.css'
    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield ScrollableContainer (conect())
        yield Label(" Usuario:")
        yield self.user_        
        yield Label(" Contraseña:")
        yield self.pass_
        yield Label(" Host:")
        yield self.host_
        yield Label(" Base de datos:")
        yield self.database_
        yield self.log_
        yield Label(" Menú de tablas")
        yield self.opciones
        yield self.tabla

    @on(Button.Pressed, "#conexion")
    def conectar(self):
        try:
            self.cnx = mysql.connector.connect(user= self.user_.value, password = self.pass_.value, host = self.host_.value, database = self.database_.value)
            self.log_.write_line(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} Conexión exitosa")
            cursor = self.cnx.cursor()
            cursor.execute("SHOW TABLES;")
            self.opciones.clear_options()
            tables = [table[0] for table in cursor.fetchall()]
            for table in tables:
                self.opciones.add_option(table)       
        except mysql.connector.Error as e:
            self.log_.write_line(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} Error al conectarse: {e}")

    @on(OptionList.OptionHighlighted)
    @work(exclusive=True)
    async def show_selection(self, event: OptionList.OptionHighlighted) -> None:
        if self.cnx is not None:
            try:
                cursor = self.cnx.cursor()
                query = f"SELECT * FROM {self.opciones.get_option_at_index(self.opciones.highlighted).prompt}"
                cursor.execute(query)
                self.tabla.clear(columns=True)
                column_names = [column[0] for column in cursor.description]
                self.tabla.add_columns("#", *column_names)  
                self.tabla.loading = True
                filita = 1  
                while True:
                    rows = cursor.fetchmany(size=50)
                    if not rows:
                        break
                    for row in rows:
                        self.tabla.add_row(filita, *row)
                        filita += 1  

                self.log_.write_line(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} Consulta realizada con éxito {self.opciones.get_option_at_index(self.opciones.highlighted).prompt}")
                self.tabla.loading = False
            except mysql.connector.Error as e:
                self.log_.write_line(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} Error al ejecutar la consulta: {str(e)}")
        else:
            self.log_.write_line(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} No se ha establecido una conexión")

    @on(Button.Pressed, "#desconectar")
    def desconectar(self):
        try:
           self.cnx.close()
           self.log_.write_line(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} Se desconectó correctamente")
        except mysql.connector.Error as e:
            self.log_.write_line(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} Hubo problemas al desconectar {e}")

if __name__ == "__main__":
    app = ConexionSQL()
    app.run()
    