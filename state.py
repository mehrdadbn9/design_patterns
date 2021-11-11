from abc import ABC, abstractmethod


class Task:
    def __init__(self, title, body, status):
        self.title = title
        self.body = body
        self.status = status
        self.flow = [status]

    @property
    def current(self):
        return self.flow[-1]

    def send(self, to_do_task):
        if to_do_task.__class__ not in self.current.allowed:
            print("is not valid to move to this part do previous step first!!")
        else:
            self.flow.append(to_do_task)
            print("task sent to {to_do_task.__class__}")


class AbstractTask(ABC):
    @property
    @abstractmethod
    def allowed(self):
        pass


class DoneTask(AbstractTask):
    allowed = []


class DoingTask(AbstractTask):
    allowed = [DoneTask]


class TodoTask(AbstractTask):
    allowed = [DoingTask]


class CreatTask(AbstractTask):
    allowed = [TodoTask]


class Operator(AbstractTask):
    allowed = [CreatTask]


if __name__ == '__main__':
    ct = CreatTask()
    tt = TodoTask()
    doing_t = DoingTask()
    done_t = DoneTask()
    opt = Operator()

    task = Task("you should do ...", "detail of ...", Operator)

# correct:
    task.send(ct)
    task.send(tt)
    task.send(doing_t)

# wrong:
    task.send(doing_t)
