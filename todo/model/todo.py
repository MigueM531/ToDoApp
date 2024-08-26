# TODO: Add code here
class Todo:

    def __init__(self, code_id: int, tittle: str, description: str):
        self.code_id: int = code_id
        self.title: str = tittle
        self.description: str = description
        self.completed: bool = False
        self.tags: list[str] = []

    def mark_completed(self):
        self.completed = True

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self) -> str:
        return f"{self.code_id} - {self.title}"


class TodoBook:

    def __init__(self):
        self.todos = {}

    def add_todo(self, title: str, description: str) -> int:
        todo_id = len(self.todos) + 1
        new_todo = Todo(todo_id, title, description)
        self.todos[todo_id] = new_todo
        return todo_id

    def pending_todos(self) -> list:
        return [todo for todo in self.todos.values() if not todo.completed]

    def completed_todos(self) -> list:
        return [todo for todo in self.todos.values() if todo.completed]

    def tags_todo_count(self) -> dict[str, int]:
        all_tags = [tag for todo in self.todos.values() for tag in todo.tags]

        tag_count = {}

        for tag in all_tags:
            if tag in tag_count:
                tag_count[tag] += 1
            else:
                tag_count[tag] = 1
        return tag_count
