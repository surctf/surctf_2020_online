## BIP BOP i'm just a roBOT: Write-up

Читаем таск, видим намек на роботов. Переходим по ссылке ничего примечательного не видим, вспоминаем про роботов, пытаемся открыть <a href="http://64.227.79.53:44444/robots.txt"> /robots.txt </a>, погуглите что это и зачем.

Видим  строку: 
`Disallow: /super_secret_place/`

Переходим в <a href="http://64.227.79.53:44444//super_secret_place/"> /super_secret_place/ </a>, видим непонятный текст и пару гиперссылок, переходим по каждой, возбуждаемся, в конце списка находим картинку с флагом.

![flag](./static/flag.png)

Флаг: `surctf_robots_has_heart_too`

> Непонятный текст - это hex, можете перевести его в читаемый текст
