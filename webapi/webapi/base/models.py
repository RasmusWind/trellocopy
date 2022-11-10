from django.db import models

# Board tabellen. Den har et navn og en position.
class Board(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    position = models.SmallIntegerField(default=0, null=False, blank=False)

    def __str__(self):
        return self.name

# Task tabellen. Den har et navn, en beskrivelse, en position(hvor på boardet skal den være) og et complete felt.
class Task(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    board = models.ForeignKey(Board, related_name="tasks", null=True, blank=True, on_delete=models.SET_NULL)
    position = models.SmallIntegerField(default=0, null=False, blank=False)
    complete = models.BooleanField(default=False)
    image = models.ImageField(upload_to="pictures", null=True, blank=True)

    def __str__(self):
        return self.name

# Todo tabellen. Den har et navn, en beskrivelse, en position(hvor på en task skal den være) og et complete felt.
# Todo har en foreignkey til Task.
# "related_name" gør sådan at man kan få en liste af todos ud fra en task, eksempel:
# task_variable.todos.all() = en liste af alle de todos som har en foreignkey til
# lige præcist denne task.
class Todo(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    task = models.ForeignKey(Task, related_name="todos", null=True, blank=True, on_delete=models.SET_NULL)
    position = models.SmallIntegerField(default=0, null=False, blank=False)
    complete = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
# Team tabellen. Den har et navn, en mange til mange relation til task og en foreignkey til task.
# ManyToMany relationen gør sådan at et team kan have flere tasks og en task kan have flere teams der arbejder på den.
# Foreignkey relationen gør sådan at vi kan vise hvilken task teamet arbejder på lige nu.
# Der er to "related_name" i denne tabel.
# Dette gør sådan at Task har to lister, en for alle de teams der har den(mange til mange, "teams"),
# og en for alle de teams der har den som deres current_task(foreignkey, "current_teams")
class Team(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    tasks = models.ManyToManyField(Task, related_name="teams")
    current_task = models.ForeignKey(Task, related_name="current_teams", null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

# Worker tabellen. Den har et fornavn, efternavn, email, team og en current todo.
# current_todo fordi at en worker kun kan arbejde på en todo af gangen.
# for at se hvor mange opgaver en worker har i alt kan man gå igennem dens team, eksempel:
# worker1 er en instance af vores worker class
# for team in worker1.teams.all():
#     print(team.name)
#     for task in team.tasks.all():
#         print(task.name)    
#         for todo in task.todos.all():
#             print(todo.name)
class Worker(models.Model):
    first_name = models.CharField(max_length=200, null=False, blank=False)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=254)
    teams = models.ManyToManyField(Team, related_name="workers")
    current_todo = models.ForeignKey(Todo, null=True, blank=True, on_delete=models.SET_NULL)    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"