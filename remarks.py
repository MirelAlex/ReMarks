import flet
from flet import (
    Checkbox,
    Dropdown,
    Column,
    Icon,
    FloatingActionButton,
    IconButton,
    OutlinedButton,
    Page,
    Row,
    Tab,
    Tabs,
    Text,
    TextField,
    UserControl,
    dropdown,
    colors,
    icons,
)
data = [
    {
        "remark_name": "remark22",
        "remark_title": "asd",
        "ticket_id":  "#GMCTC-1",
        "completed": True
    },
    {
        "remark_name": "remark2",
        "remark_title": "asd",
        "ticket_id":  "#GMCTC-1",
        "completed": False
    },
    {
        "remark_name": "remark1",
        "remark_title": "asd",
        "ticket_id":  "#GMCTC-2",
        "completed": False
    },
    {
        "remark_name": "remark2",
        "remark_title": "asd",
        "ticket_id":  "#GMCTC-2",
        "completed": False
    }
]


class Remark(UserControl):
    def __init__(self, remark_name, remark_status_change, remark_delete, ticket_id, remark_title):
        super().__init__()
        self.ticket_id = ticket_id
        self.completed = False
        self.remark_title = remark_title
        self.remark_name = remark_name
        self.remark_status_change = remark_status_change
        self.remark_delete = remark_delete

    def build(self):
        self.display_remark = Checkbox(
            value=self.completed, label=self.remark_name, on_change=self.status_changed
        )
        self.edit_remark = TextField(expand=1)

        self.display_view = Row(
            alignment="spaceBetween",
            vertical_alignment="center",
            controls=[
                self.display_remark,
                Row(
                    spacing=0,
                    controls=[
                        IconButton(
                            icon=icons.CREATE_OUTLINED,
                            tooltip="Edit Remark",
                            on_click=self.edit_clicked,
                        ),
                        IconButton(
                            icons.DELETE_OUTLINE,
                            tooltip="Delete Remark",
                            on_click=self.delete_clicked,
                        ),
                    ],
                ),
            ],
        )

        self.edit_view = Row(
            visible=False,
            alignment="spaceBetween",
            vertical_alignment="center",
            controls=[
                self.edit_remark,
                IconButton(
                    icon=icons.DONE_OUTLINE_OUTLINED,
                    icon_color=colors.GREEN,
                    tooltip="Update Remark",
                    on_click=self.save_clicked,
                ),
            ],
        )
        return Column(controls=[self.display_view, self.edit_view])

    def edit_clicked(self, e):
        self.edit_remark.value = self.display_remark.label
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()

    def save_clicked(self, e):
        self.display_remark.label = self.edit_remark.value
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()

    def status_changed(self, e):
        self.completed = self.display_remark.value
        self.remark_status_change(self)

    def delete_clicked(self, e):
        self.remark_delete(self)


class RemarksApp(UserControl):
    def build(self):
        global data
        self.data = data

        self.ticket_number = TextField(
            prefix_text="#GMCTC-",
            hint_text="ticket number",
            width=200
        )
        self.new_title = TextField(
            hint_text="Add ticket title",
            expand=True
        )
        self.new_remark = TextField(
            hint_text="What needs to be done?",
            on_submit=self.add_clicked,
            expand=True
        )
        self.filter = Tabs(
            selected_index=0,
            on_change=self.tabs_changed,
            tabs=[Tab(text="all"), Tab(text="active"), Tab(text="completed")],
        )
        self.remarks = self.retrieve_data()

        # self.tickets = Tabs(
        #     selected_index=0,
        #     on_change=self.tabs_changed,
        #     scrollable=True,
        #     tabs=[Tab(text="GMCTC-123"), Tab(text="GMCTC-1234"),
        #           Tab(text="GMCTC-1213"), Tab(text="GMCTC-1253"), Tab(text="GMCTC-12333"), Tab(text="GMCTC-12s3")],
        # )

        self.tickets = Dropdown(
            width=200,
            on_change=self.tabs_changed,
            options=[dropdown.Option("all")],
            value="all"
        )

        self.delete_ticket_btn = IconButton(
            icons.DELETE_OUTLINE,
            disabled=True,
            tooltip="Delete Ticket",
            on_click=self.delete_ticket,
        )

        self.items_left = Text("0 items left")

        # update dropdown options
        self.update_dropdown()

        # application's root control (i.e. "view") containing all other controls
        return Column(
            width=600,
            controls=[
                Row([Icon(name=icons.BOOKMARK_ADD, color=colors.PINK), Text(value="ReMarks", style="headlineMedium"), Icon(name=icons.BOOKMARK_ADDED, color=colors.GREEN)],
                    alignment="center"),
                Column(controls=[
                    Row(
                        controls=[
                            self.ticket_number,
                            self.new_title,
                        ],
                    ),
                    Row(
                        controls=[
                            self.new_remark,
                            FloatingActionButton(
                                icon=icons.ADD, bgcolor=colors.PINK, on_click=self.add_clicked),
                        ],
                    ),
                ]),
                Column(
                    spacing=25,
                    controls=[Row([

                        self.filter,
                        self.tickets,
                        self.delete_ticket_btn
                    ]),
                        self.remarks,
                        Row(
                            alignment="spaceBetween",
                            vertical_alignment="center",
                            controls=[
                                self.items_left,
                                OutlinedButton(
                                    text="Clear completed", on_click=self.clear_clicked
                                ),
                            ],
                    ),
                    ],
                ),
            ],
        )

    def retrieve_data(self):
        result = Column()

        if len(self.data):
            # print(self.data)
            for r in self.data:
                remark = Remark(r["remark_name"],
                                self.remark_status_change, self.remark_delete, r["ticket_id"], r["remark_title"])
                remark.completed = r["completed"]
                result.controls.append(remark)
            # self.new_remark.value = ""
            # self.new_remark.focus()
            # self.update()
        return result

    def validate_input(self):
        isInputGood = True
        if self.new_remark.value == '':
            self.new_remark.error_text = 'Add a remark!'
            isInputGood = False
        else:
            self.new_remark.error_text = ''

        if self.ticket_number.value == '' or not self.ticket_number.value.isnumeric():
            self.ticket_number.error_text = 'Add a ticket number!'
            isInputGood = False
        else:
            self.ticket_number.error_text = ''

        if self.new_title.value == '':
            self.new_title.error_text = 'Add a ticket title!'
            isInputGood = False
        else:
            self.new_title.error_text = ''

        super().update()

        return isInputGood

    def add_ticket_to_dropdown(self):
        can_add_it = True
        ticket_id = "#GMCTC-" + self.ticket_number.value

        for op in self.tickets.options:
            if op.key == ticket_id:
                can_add_it = False

        if can_add_it or len(self.tickets.options) == 0:
            self.tickets.options.append(dropdown.Option(ticket_id))
            self.delete_ticket_btn.disabled = False

        # update dropdown "focus" on current ticket id
        self.tickets.value = ticket_id

        return ticket_id

    def add_clicked(self, e):
        # ticket_id = self.tickets.tabs[self.tickets.selected_index].text

        if(self.validate_input()):
            # ticket_id = "#GMCTC-" + self.tickets.value
            ticket_id = self.add_ticket_to_dropdown()
            task = Remark(self.new_remark.value,
                          self.remark_status_change, self.remark_delete, ticket_id, self.new_title.value)
            self.remarks.controls.append(task)
            self.new_remark.value = ""
            self.new_remark.focus()
            self.update()

    def delete_ticket(self, e):
        if self.tickets.value != "all":
            indx = [x.key for x in self.tickets.options].index(
                self.tickets.value)
            self.tickets.options.pop(indx)
            # ticket poped from options list -> pop remark related to it also
            self.pop_ticket_remarks(self.tickets.value)
            tickets_number = len(self.tickets.options)
            self.tickets.value = self.tickets.options[tickets_number-1].key
        self.update()

    def pop_ticket_remarks(self, _id):
        for remark in self.remarks.controls[:]:
            if remark.ticket_id == _id:
                self.remark_delete(remark)

    def remark_status_change(self, task):
        self.update()

    def remark_delete(self, task):
        self.remarks.controls.remove(task)
        self.update()

    def tabs_changed(self, e):
        self.update()

    def clear_clicked(self, e):
        for task in self.remarks.controls[:]:
            if task.completed:
                self.remark_delete(task)

    def update_dropdown(self):
        unique_ids = set([r.ticket_id for r in self.remarks.controls])
        for r in sorted(list(unique_ids)):
            self.tickets.options.append(dropdown.Option(r))

    def update(self):
        count = 0
        status = self.filter.tabs[self.filter.selected_index].text
        # ticket_id = self.tickets.tabs[self.tickets.selected_index].text
        ticket_id = self.tickets.value

        # update input fields and delete btn based on dropdown selection
        if ticket_id != "all":
            self.ticket_number.value = ticket_id.split("-")[-1]
            self.delete_ticket_btn.disabled = False
        else:
            self.ticket_number.value = ''
            self.new_title.value = ''
            self.delete_ticket_btn.disabled = True

        for task in self.remarks.controls:
            task.visible = (
                (
                    status == "all"
                    or (status == "active" and task.completed == False)
                    or (status == "completed" and task.completed)
                )
                and
                (
                    ticket_id == task.ticket_id
                    or ticket_id == "all"
                )
            )
            if task.ticket_id == ticket_id:
                self.new_title.value = task.remark_title

            if not task.completed:
                count += 1
        self.items_left.value = f"{count} active item(s) left"
        super().update()


def main(page: Page):
    page.title = "ReMarks App"
    page.horizontal_alignment = "center"
    page.scroll = "adaptive"
    page.window_width = 600
    page.window_height = 900

    page.update()

    # create application instance
    app = RemarksApp()

    # add application's root control to the page
    page.add(app)
    app.update()


flet.app(target=main)
