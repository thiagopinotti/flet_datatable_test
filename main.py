from flet import *
from model import Encomendas

def main(page: Page):

    page.theme_mode = 'light'

    def update_table():
        enc = Encomendas.select()
        for i in enc:
            table.rows.append(
                DataRow(
                    cells=[
                        DataCell(Text(i.id)),
                        DataCell(Text(i.evento)),
                        DataCell(Text(i.cliente)),
                        DataCell(Text(i.data)),
                        DataCell(Text(i.cerimonial)),
                        DataCell(Text(i.local)),
                        DataCell(Text(i.horario)),
                        DataCell(IconButton(icon='delete', data=i, on_click=remover))
                    ]
                )
            )
        page.update()

    def clean_textfields():
        evento.value = cliente.value = data.value = cerimonial.value = local.value = horario.value = ''
        page.update()
    
    def db_save(e):
        table.rows.clear()
        table.update()
        Encomendas.create(
            evento= evento.value,
            cliente= cliente.value,
            data= data.value,
            cerimonial= cerimonial.value,
            local= local.value,
            horario= horario.value
        )
        update_table()
        evento.focus()
        clean_textfields()
    
    def remover(e):
        id = e.control.data
        Encomendas.delete_by_id(id)
        table.rows.clear()
        update_table()
        
    # TITULO
    titulo = Text('TESTANDO FORMULARIO')

    # TABELA
    table = DataTable(
        height=300,
        border= border.all(2, "black"),
        columns=[
            DataColumn(Text('ID')),
            DataColumn(Text('Evento')),
            DataColumn(Text('Cliente')),
            DataColumn(Text('Data')),
            DataColumn(Text('Cerimonia')),
            DataColumn(Text('Local')),
            DataColumn(Text('Horario')),
            DataColumn(Text('Ações'))
        ],
        rows=[]
    )

    # TEXTFIELDS
    # id = TextField(label='ID', width=50)
    evento = TextField(label='Evento', width=300)
    cliente = TextField(label='Cliente', width=400)
    data = TextField(label='Data', width=400)
    cerimonial = TextField(label='Cerimonia', width=400)
    local = TextField(label='Local', width=400)
    horario = TextField(label='Horário', width=400)

    # BOTÕES
    btn_save = ElevatedButton('+', on_click=db_save)

    page.add(
        titulo,
        Row(wrap=True,
            controls=[
                evento,
                cliente,
                data,
                cerimonial,
                local,
                horario,
                btn_save
            ]
        ),
        table
    )
    update_table()


app(target=main)
