from textual.app import App, ComposeResult
from textual.widgets import Header, LoadingIndicator, Button, Static, Input, Label, TextArea, DataTable, Log, OptionList, LoadingIndicator, RadioButton, RadioSet, RichLog, Tabs, Tab, TabPane, TabbedContent, Markdown
from datetime import datetime
from textual import on, work
from textual.events import Click
import mysql.connector
from mysql.connector import IntegrityError
import traceback
import logging
from textual.containers import ScrollableContainer, Container
CSS_PATH = 'estilos.css'

        
class ConexionSQL(App):
    CSS_PATH = 'estilos.css'
    def __init__(self):
        super().__init__()
        self.user_ = Input("crud")
        self.pass_ = Input("", id="pass_", password=True)
        self.host_ = Input("127.0.0.1", id="host_")
        self.database_ = Input("six_flags", id="database_")
        self.cnx_ = None
        self.log_ = RichLog(highlight=True, markup=True)
        self.tabla_ = DataTable()
        self.tabla_.cursor_type = "row"
        self.tabla_.zebra_stripes = True
        self.opciones_ = OptionList("--Conectate primero")
        self.loading_ = LoadingIndicator()
        self.consulta_ = TextArea("--Cuadro de consultas", language="python",theme="vscode_dark")
        #{'dracula', 'github_light', 'monokai', 'vscode_dark'}
        self.seleccionado_ = None

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
                    yield RadioButton("Insertar fila", id="insert") #c
                    yield RadioButton("Actualizar valor", id="update")#u            
                    yield RadioButton("Query", id="query")#u       
                    #yield RadioButton("Ejecutar", value=True, id="ejecutar") 
                
                yield Button("Ejecutar", id="ejecutar", variant="warning")
                    
    ##############################################
            
    @on(Button.Pressed, "#conexion")
    def conectar(self):
        try:
            self.cnx_ = mysql.connector.connect(user= self.user_.value, password = self.pass_.value, host = self.host_.value, database = self.database_.value)
            self.log_.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} Conexión [green]exitosa[/green]")
            cursor = self.cnx_.cursor()
            cursor.execute("SHOW TABLES;")
            self.opciones_.clear_options()
            tables = [table[0] for table in cursor.fetchall()]
            for table in tables:
                self.opciones_.add_option(table)    
        except mysql.connector.Error as e:
            self.log_.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} {e}")
        except Exception as e:
            self.log_.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  [red]Error[/red] al conectarse: {e}")            
        except:
             self.log_.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  {traceback.format_exc()}")
   
    @on(Button.Pressed, "#ejecutar")
    @work(exclusive=True)
    async def consultita(self):
        self.log_.write(str(self.consulta_.text))
        try:            
            cursor = self.cnx_.cursor()
            cursor.execute(str(self.consulta_.text))        
            self.log_.write(f"se hizo")
        except mysql.connector.IntegrityError as err:
                self.log_.write(1)
        except Exception as e:
                self.log_.write(f"{e} jaja")
        except:
             self.log_.write(f"3")

    @on(OptionList.OptionHighlighted)
    @work(exclusive=True)
    async def show_selection(self, event: OptionList.OptionHighlighted) -> None:
        if self.cnx_ is not None:
            try:
                self.seleccionado_ = self.opciones_.get_option_at_index(self.opciones_.highlighted).prompt
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
                self.log_.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} Consulta realizada con éxito [blue]{self.opciones_.get_option_at_index(self.opciones_.highlighted).prompt}[/blue]")
                self.tabla_.loading = False
            except mysql.connector.Error as e:
                self.log_.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} [red]Error[/red] al ejecutar la consulta: {str(e)}")
            except Exception as e:
                self.log_.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  {e}")
            except:
                 self.log_.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  {traceback.format_exc()}")
        else:
            self.log_.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} [red]Error[/red] no se ha establecido una conexión")            
    
    @on(Button.Pressed, "#desconectar")
    def desconectar(self):
        try:
           self.cnx_.close()
           self.log_.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} Se desconectó correctamente")
        except AttributeError as e:
            self.log_.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} [red]Error[/red] no se pudo desconectar, no te haz ni conectado. Error: {str(e)}")
        except mysql.connector.Error as err:
            self.log_.write("Algo salió mal: {}".format(err))
        except Exception as e:
            self.log_.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} [red]Error[/red] desconocido al desconectar: {str(e)}")
        except:
            self.log_.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  {traceback.format_exc()}")

    
    async def on_radio_set_changed(self, event: RadioSet.Changed) -> None:
        
        try:
            tabla = self.seleccionado_
            cambios =[]
            cursor = self.cnx_.cursor(tabla)
            cursor.execute(f"DESC {tabla}")
            for i in cursor.fetchall():
                cambios.append(str(i[0]))
        except Exception as e:
                self.log_.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  {e}")
        except:
            self.log_.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} Error ¿Estás desconectado? ¿Seleccionaste alguna tabla?")     
        if event.pressed.id == 'update':
            try:
                fila_actual = self.tabla_.get_row_at(self.tabla_.cursor_row)
                sets = ', '.join([f'{c} = {fila_actual[i]}' for i, c in enumerate(cambios[1:])])
                self.consulta_.text = f"UPDATE {tabla}\nSET {sets}\nWHERE {cambios[0]} = {fila_actual[0]};"
            except UnboundLocalError as e:
                self.consulta_.text = (f"¿Intentaste seleccionar una tabla primero? Error UnboundLocalError: {e}")
            except Exception as e:
                self.log_.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  {e}")
            except:
                self.log_.write(traceback.format_exc())

        if event.pressed.id == 'delete':
            try:
                fila_actual = self.tabla_.get_row_at(self.tabla_.cursor_row)
                self.consulta_.text = f"DELETE FROM {tabla}\nWHERE {cambios[0]} = {fila_actual[0]};"
            except UnboundLocalError as e:
                self.consulta_.text = (f"¿Intentaste seleccionar una tabla primero? [red]Error[/red] UnboundLocalError: {e}")
            except Exception as e:
                self.log_.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  {e}")
            except:
                self.log_.write(traceback.format_exc())


        if event.pressed.id == 'insert':
            try:
                self.consulta_.text = f"INSERT INTO {tabla} {tuple(cambios)}\n VALUES (\t\n{', '.join(['\n\t' for _ in cambios])}\n);"
            except UnboundLocalError as e:
                self.consulta_.text = (f"¿Intentaste seleccionar una tabla primero? Error UnboundLocalError: {e}")
            except Exception as e:
                self.log_.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  {e}")
            except:
                self.log_.write(traceback.format_exc())
        
        if event.pressed.id == 'query':
            self.consulta_.text = f"-- Inserte la consulta que quiera."
    

       
        
if __name__ == "__main__":
    app = ConexionSQL()
    app.run()
