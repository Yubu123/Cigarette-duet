from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QIcon
import pygame
import sys

class Window(QWidget):
    def __init__(self, timings, play_music=False):
        super().__init__()
        self.setWindowTitle("Cigarette Duet")
        self.resize(500, 500)
        self.setWindowIcon(QIcon("duet.jpg"))

        if play_music:
            pygame.mixer.init()
            pygame.mixer.music.load("cigarrete.mp3")
            pygame.mixer.music.play(loops=-1)

        self.label = QLabel("", self)
        self.label.setStyleSheet("font-size: 30px; font-family: Arial;")
        self.label.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.schedule_texts(timings)

    def schedule_texts(self, timings):
        for time, text in timings:
            QTimer.singleShot(time, lambda t=text: self.label.setText(t))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    timings1 = [
        (0, "It's"),
        (600, "It's just"),
        (1100, "It's just a cigarette"),
        (2100, "And"),
        (2400, "And I"),
        (2700, "And I only"),
        (3200, "And I only did It"),
        (3800, "And I only did It once"),
        (4800, "It's"),
        (5100, "It's only"),
        (5400, "It's only twice a"),
        (5900, "It's only twice a week"),
        (6700, "So"),
        (7000, "So there's"),
        (7300, "So there's not"),
        (7600, "So there's not much"),
        (8000, "So there's not much of a chance"),
        (9500, "It's"),
        (9800, "It's just"),
        (10300, "It's just a cigarette"),
        (11000, "And"),
        (11600, "And I'm"),
        (12000, "And I'm sorry"),
        (12500, "And I'm sorry that"),
        (12900, "And I'm sorry that I"),
        (13200, "And I'm sorry that I did"),
        (13400, "And I'm sorry that I did It"),
        (14100, "Honey"),
        (14600, "Honey,can't"),
        (14900, "Honey,can't you"),
        (15200, "Honey,can't you trust"),
        (15500, "Honey,can't you trust me"),
        (15700, "When I"),
        (16000, "When I want"),
        (16300, "When I want to stop"),
        (16900, "I"),
        (17300, "I can"),
        (18300, "💗"),

    ]
    timings2 = [
        (0, "It's"),
        (600, "It's just"),
        (1100, "It's just a cigarette"),
        (2100, "It'll"),
        (2400, "It'll soon"),
        (2700, "It'll soon be"),
        (3200, "It'll soon be only"),
        (3800, "It'll soon be only ten"),
        (4800, "It'll"),
        (5100, "It'll make"),
        (5400, "It'll make you"),
        (5900, "It'll make you sick"),
        (6700, "Girl"),
        (7000, "Girl there's"),
        (7300, "Girl there's not"),
        (7600, "Girl there's not much"),
        (8000, "Girl there's not much of a chance"),
        (9500, "It's"),
        (9800, "It's just"),
        (10300, "It's just a cigarette"),
        (11000, "You'll"),
        (11600, "You'll be"),
        (12000, "You'll be sorry"),
        (12500, "You'll be sorry that"),
        (12900, "You'll be sorry that you"),
        (13200, "You'll be sorry that you did"),
        (13400, "You'll be sorry that you did It"),
        (14100, ""),
        (18300, "💗"),
    ]


    screen = app.primaryScreen().availableGeometry()
    center_x = screen.width() // 2
    center_y = screen.height() // 2

    window1 = Window(timings=timings1, play_music=True)
    window2 = Window(timings=timings2, play_music=False)

    spacing = 5
    total_width = window1.width() * 2 + spacing

    window1.move(center_x - total_width // 2, center_y - window1.height() // 2)
    window2.move(center_x - total_width // 2 + window1.width() + spacing,
                 center_y - window2.height() // 2)

    window1.show()
    window2.show()
    sys.exit(app.exec_())
