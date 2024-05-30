import tkinter as tk
from PIL import Image, ImageTk

class QuizGameGUI:
    def __init__(self, master): #этот код определяет конструктор класса с двумя параметрами: self и master.
        self.master = master #в объекте self создается атрибут с названием "master" и ему присваивается значение переменной "master"
        self.master.title("Игра-викторина")

        self.questions = [
            "Как называется самая длинная река в Африке?",
            "В какой стране находятся Великие пирамиды Гизы?",
            "Из скольких штатов состоят Соединенные Штаты Америки?",
            "Какая страна граничит с Великобританией?",
            "Какой стране принадлежат Канарские острова?",
            "Как называется море, не имеющее береговой линии?",
            "В какой стране находится гора Эверест?",
            "Как называется столица штата Нью-Йорк?",
            "В честь какого озера названо известное мифическое чудовище?",
            "Как называется самая большая пустыня в мире?"
        ]

        self.answers = [
            "Нил", "Египет", "50", "Ирландия", "Испания",
            "Саргассово", "Непал", "Олбани", "Лох-Несс", "Антарктическая"
        ]

        self.current_question = 0 #отслеживание текущего вопроса
        self.user_score = 0

        self.question_label = tk.Label(master, text=self.questions[self.current_question]) #обозначает использование виджета метки из библиотеки tkinter
        self.question_label.pack() # метка, которая будет размещена на интерфейсе.

        self.answer_entry = tk.Entry(master) #Этот код создает виджет ввода текста
        self.answer_entry.pack()

        self.submit_button = tk.Button(master, text="Ответить", command=self.check_answer) #Этот код создает кнопку "Ответить"
        self.submit_button.pack() # это виджет кнопки, который должен появиться на экране

        self.result_label = tk.Label(master, text="")  #этот код создает пустую метку, которая может использоваться для отображения текста в графическом интерфейсе приложения.
        self.result_label.pack() # команда говорит о том, что виджет должен быть упакован в родительский контейнер для отображения на экране.

        # Создание изображения для фона

        self.canvas = tk.Canvas(master, height=800, width=600) #Эта строка кода создает холст в главном окне с заданными размерами
        self.canvas.pack() #это строка кода, которая используется для размещения канвы в главном окне

        self.image = Image.open('C:\\Users\\адимн\\OneDrive\\Рабочий стол\\30_nature.jpg')

        self.bg_image = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, anchor='nw', image=self.bg_image) # этот код создает изображение на холсте в графическом приложении.

    def check_answer(self):  #используется для проверки ответа на вопрос
        user_answer = self.answer_entry.get().lower() #будет содержать значение введенное пользователем, преобразованное в нижний регистр для удобства сравнения или обработки.
        if user_answer == self.answers[self.current_question].lower(): #Это условие проверяет, правелен ли ответ пользователя
            self.user_score += 1
            self.result_label.config(text="Правильно!")
        else:
            self.result_label.config(text=f"Неправильно. Правильный ответ: {self.answers[self.current_question]}")

        self.current_question += 1
        if self.current_question < len(self.questions): #Это условие, которое проверяет, если значение переменной меньше, чем количество вопросов в списке
            self.question_label.config(text=self.questions[self.current_question])  #текст вопроса отображен в виджете
            self.answer_entry.delete(0, tk.END) #весь текст ввода автоматически удаляется из виджета при вызове этой команды.
        else:
            self.show_final_score() #предназначен для вывода итогового счета.

    def show_final_score(self): #показывает окончательный результат
        final_score_text = f"Ваш результат: {self.user_score}!" #вывод результата пользователя
        self.result_label.config(text=final_score_text) #содержит результат

root = tk.Tk() #Этот код используется при создании основного окна  для создания графического пользовательского интерфейса
quiz_game_gui = QuizGameGUI(root) #будет отображено окно игры викторины
root.mainloop() #запускает основной цикл событий для графической пользовательского интерфейса