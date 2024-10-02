# UrTube
import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return f'{self.nickname}'

    def __ed__(self, other):  # соотносим имя пользователя с базой
        return other.nickname == self.nickname

    def get_info(self):  # возврат имени пользователя и пароля
        return self.nickname, self.password


class Video:
    def __init__(self, title, duration, adult_mode, time_now):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode
        self.time_now = 0

    def __str__(self):  # возврат названия видео
        return self.title


class UrTube:
    def __init__(self):
        self.users = [User1().User2(), User3()]
        self.videos = []
        self.current_user = None

    def log_in(self, ):  # проверяем наличие регистрации в системе
        for user in self.users:
            if (login, hash(password)) == user.get_info():
                self.current_user = user
                return user

    def register(self, nickname, password, age): # проверка нового юзер на принадлежность базе
        new_user = User(nickname, password, age)
        if new_user not in self_users:
            self.users.append(new_user)
            self.current_user = new_user
        else:
            print(f'Пользователь {nickname} уже существует')

    def log_out(self): #обнуляем текущего пользователя
        self.current_user = None

    def add(self, *videos: Video): # Собираем плейлист
        for video in videos:
            if video.title not in self.videos:
                self.videos.append(video)

    def get_videos(self, search): # проверка видео на...?
        titles = []
        for video in self.videos:
            if search.lower() in str(video).lower():
                titles.append(video)

        return titles

    def watch_video(self,title): # контроль возрастной категории
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        for video in self.videos:
            if title == video.title:
                if video.adult_mode and self.current_user.age >= 18:
                    while video.time_now += 1
                    print(video.time_now, end='')
                    time.sleep(1)
                video.time_now = 0
                print('Конец видео')
            else:
                print('Вам нет 18 лет, пожалуйста, покиньте страницу')
            break



ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')







