from flet import *


def main(page: Page):

    def salvar(e):
        table.rows.append(
            DataRow(
                cells=[
                    DataCell(Text(id.value)),
                    DataCell(Text(evento.value)),
                    DataCell(Text(cliente.value)),
                    DataCell(Text(data.value)),
                    DataCell(Text(cerimonial.value)),
                    DataCell(Text(local.value)),
                    DataCell(Text(horario.value))
                ]
            )
        )
        page.update()
        
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
            DataColumn(Text('Horario'))     
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
    btn_save = ElevatedButton('+', on_click=salvar)

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
        ), table
    )


app(target=main)