import flet as ft
<<<<<<< HEAD
def main(page: ft.Page):
    page.title = "Flet Hello"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    dlg = ft.AlertDialog(
        title=ft.Text("Hola")
    )

    def open_dlg(e):
        page.dialog = dlg
        dlg.open = True
        page.update()

    page.appbar = ft.AppBar(
        title=ft.Text("Hello Word...")
    )
    page.add(
        ft.Row(
            [
                ft.Text("Hello world"),
                ft.ElevatedButton(text = "Show hello world",on_click=open_dlg)
            ]
        )      
    )
ft.app(target=main)
=======


def main(page: ft.Page):
    # the title of the app
    page.title = "Flet Counter App"

    # a light/bright theme
    page.theme_mode = "light"

    # use material 2 design theme | this is just to better mimic the Flutter example
    page.theme = ft.Theme(use_material3=False)

    # the page's alignment
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    def increment_counter(e):
        """Increment the value of the counter_text object by 1, and update the UI to reflect these changes."""
        counter_text.value = str(int(counter_text.value) + 1)
        page.update()

    # the app's appbar
    page.appbar = ft.AppBar(
        title=ft.Text("Flet Demo Home Page", color=ft.colors.WHITE),  # a title of white color
        bgcolor=ft.colors.BLUE,  # a blue background color
        center_title=True  # center the title || without this, the title will be on the left
    )

    # text that contains the counter number to be incremented
    counter_text = ft.Text("0", style=ft.TextThemeStyle.DISPLAY_MEDIUM)

    # the app's FAB
    page.floating_action_button = ft.FloatingActionButton(
        content=ft.Icon(ft.icons.ADD, color=ft.colors.WHITE),
        shape=ft.CircleBorder(),  # gives the button a round/circle shape
        on_click=increment_counter,  # the callback to be executed when this button is clicked
        tooltip="Increment",  # the text to be shown when this button is hovered
        bgcolor=ft.colors.BLUE  # a blue background color
    )

    # adding our widgets/controls to the page/UI
    page.add(
        ft.Text("You have pushed the button this many times:"),
        counter_text
    )


# open a browser tab containing the app | remove the view parameter to open in a native OS window
ft.app(target=main, view=ft.AppView.WEB_BROWSER)
>>>>>>> eb0be072af5272dd2641af85095a5a6384bcd23d
