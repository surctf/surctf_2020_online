## ULTRA SECRET CHAT: Write-up

### Шаг 1

Итак, у нас имеется картинка с Биллом Клинтоном с 4 альбомами. Что обычно делает типичный цтфер? Правильно, забивает на содержание картинки и кидает её в Stegsolve (что в данном таске является правильным решением).


### Шаг 2

Открываем File Format и находим в конце это: `aHR0cDovL3NlcmdrYXRzdXIucHl0aG9uYW55d2hlcmUuY29tLw==.(420).`
Ничего не напоминает? Конечно, это Base64. Кидаем в декодер строку до точки и получаем ссылку: [`http://sergkatsur.pythonanywhere.com/`](http://sergkatsur.pythonanywhere.com/).

### Шаг 3

Итак, многие во время контеста забыли, что от них требуется в данном таске. А требовалось найти **ЧАТ**. Так как на сайте ничего нет, даже в исходном коде страницы *(в первой версии сайта у некоторых на фоне играла музыка, но позже я её удалил оттуда, чтобы не сбивать с толку)*, возможно чат находится в одном из разделов на сайте, но мы его не знаем.
И тут вспоминаем про таск [**BIP BOP i'm just a roBOT**](https://github.com/surctf/surctf_2020_online/tree/master/tasks/just_a_robot), где требовалось открыть robots.txt.
Открываем [`http://sergkatsur.pythonanywhere.com/robots.txt`](http://sergkatsur.pythonanywhere.com/robots.txt) и видим, что скрыта директория /chat.

### Шаг 4

Переходим на [`http://sergkatsur.pythonanywhere.com/chat`](http://sergkatsur.pythonanywhere.com/chat) *(кстати, некоторые даже не залезали в robots.txt, а сразу догадались перейти в директорию /chat)*.

### Шаг 5

Видим, что перед нами открылся чат. Ой, требуется пароль... Успокаиваемся, возвращаемся к **шагу 2** и понимаем, что [**420**](https://www.youtube.com/watch?v=hsojt7iEcTQ) - это пароль.
Вводим, видим сообщение `c3VyY3RmX3N1cDRfczNjcjN0X2NoNHRfbG1hbw==` и понимаем, что это снова *базашестьдесятчетыре* и получаем флаг: `surctf_sup4_s3cr3t_ch4t_lmao`
