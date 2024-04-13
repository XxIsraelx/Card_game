import flet as ft

def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment_alignment = ft.MainAxisAlignment.CENTER
    page.window_min_width = 500
    page.bgcolor = ft.colors.BLACK

    image = ft.Container(
        expand=2,
        clip_behavior=ft.ClipBehavior.NONE,
        border_radius=ft.border_radius.vertical(top=20),
        gradient=ft.LinearGradient(
            begin=ft.alignment.bottom_left,
            end=ft.alignment.top_right,
            colors=[ft.colors.BROWN, ft.colors.SURFACE],
        ),
        content=ft.Image(
            src = 'https://static.wikia.nocookie.net/clashofclans/images/9/9b/Barbarian-xx.png/revision/latest?cb=20170703143506',
            scale=ft.Scale(scale=1.5),
        )

    )

    info = ft.Container(
        expand=2,
        padding=ft.padding.all(2),
        alignment=ft.alignment.center,
        content= ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(value='LEVEL 4', color=ft.colors.ORANGE),
                ft.Text(
                    value='Bárbaro',
                    weight=ft.FontWeight.BOLD,
                    size=30,
                    color=ft.colors.BLACK
                ),
                ft.Text(
                    value='O Bárbaro é um guerreiro destemido, com seu bigode imponente e seus músculos ele pode causar grandes estragos em aldeias inimigas. Solte uma horda destes bárbaros e espere para ver o caos!',
                    color=ft.colors.GREY,
                    text_align=ft.TextAlign.CENTER,
                    )
            ]
        )
    )
    skills = ft.Container(
        expand=1,
        bgcolor=ft.colors.ORANGE,
        padding=ft.padding.symmetric(horizontal=10),
        border_radius=ft.border_radius.vertical(bottom=20),
        content=ft.Row(
            controls=[
                ft.Column(
                    expand=1,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text(
                            value='20',
                            color=ft.colors.WHITE,
                            weight=ft.FontWeight.BOLD,
                            size=40
                        ),
                        ft.Text(
                            value='DEFESA',
                            color=ft.colors.WHITE,
                        )
                    ]
                ),
                ft.VerticalDivider(opacity=0.5),

                ft.Column(
                    expand=1,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text(
                            value='16',
                            color=ft.colors.WHITE,
                            weight=ft.FontWeight.BOLD,
                            size=40
                        ),
                        ft.Text(
                            value='VELOCIDADE',
                            color=ft.colors.WHITE,
                        )
                    ]
                ),
                ft.VerticalDivider(opacity=0.5),

                ft.Column(
                    expand=1,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text(
                            value='150',
                            color=ft.colors.WHITE,
                            weight=ft.FontWeight.BOLD,
                            size=40
                        ),
                        ft.Text(
                            value='DANO',
                            color=ft.colors.WHITE,
                        )
                    ]
                ),
            ]
        )
    )
 
    layout = ft.Container(
        height=600,
        width=350,
        shadow=ft.BoxShadow(blur_radius=100, color=ft.colors.BROWN),
        clip_behavior=ft.ClipBehavior.NONE,
        border_radius=ft.border_radius.all(30),
        bgcolor=ft.colors.WHITE,
        content=ft.Column(
            spacing=0,
            controls=[
                image,
                info,
                skills,
            ]
        )
    )

    page.add(layout)

if __name__ == "__main__":
    ft.app(target = main)