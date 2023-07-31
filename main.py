from flet import *
from model import Encomendas

def main(page: Page):

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
                        DataCell(btn_delete)
                    ]
                )
            )
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
    
    
    def remover(e):
        table.rows.clear()
        table.update()
        
    # TITULO
    titulo = Text('TESTANDO FORMULARIO')

    # TABELA
    table = DataTable(
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
    id = TextField(label='ID', width=50)
    evento = TextField(label='Evento', width=300)
    cliente = TextField(label='Cliente', width=400)
    data = TextField(label='Data', width=400)
    cerimonial = TextField(label='Cerimonia', width=400)
    local = TextField(label='Local', width=400)
    horario = TextField(label='Horário', width=400)

    # BOTÕES
    btn_save = ElevatedButton('+', on_click=db_save)
    btn_delete = IconButton(icon='delete', on_click=remover)

    page.add(
        titulo,
        Row(wrap=True,
            controls=[
                id,
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
