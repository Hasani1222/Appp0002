import flet as ft
from flet_core.types import CrossAxisAlignment


def main(page: ft.Page):
    page.title="¿Me perdonas?"
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.bgcolor="blue"
    
    lbl1=ft.Text("¿Me perdonas?",
                style=ft.TextStyle(size=40,weight="bold"))
    
    ing1=ft.Image(src="triste.png",width=200,height=200)
    
    btnSi=ft.ElevatedButton("Si",
                            color="geen",
                            width=100,
                            height=50)
    
    btnNo=ft.ElevatedButton("No",
                            color="red",
                            width=100,
                            height=50)
    def no(e):
        btnSi.width+=30
        btnNo.height+=10
        page.update()
        
    def si(e):
        ing1.src="Feliz.png"
        page.update()
        
    btnSi.on_click=si
    btnNo.on_click=no
        
    page.add(
        ft.Column(
            [
                lbl1,
                ing1,
                ft.Row([btnSi,btnNo],
                    alignment=ft.MainAxisAlignment.CENTER,
                    ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=20
        )
    )

ft.app(main)
