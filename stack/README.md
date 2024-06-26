# Стеки

## 11. Стек с защитой от ошибок

Ограничение времени:	1 секунда

Ограничение памяти: 	64Mb

Ввод:	стандартный ввод или input.txt

Вывод:	стандартный вывод или output.txt

Научитесь пользоваться стандартной структурой данных stack для целых чисел. Напишите программу, содержащую описание стека и моделирующую работу стека, реализовав все указанные здесь методы. Программа считывает последовательность команд и в зависимости от команды выполняет ту или иную операцию. После выполнения каждой команды программа должна вывести одну строчку. Возможные команды для программы:

push n
Добавить в стек число n (значение n задается после команды). Программа должна вывести ok.

pop
Удалить из стека последний элемент. Программа должна вывести его значение.

back
Программа должна вывести значение последнего элемента, не удаляя его из стека.

size
Программа должна вывести количество элементов в стеке.

clear
Программа должна очистить стек и вывести ok.

exit
Программа должна вывести bye и завершить работу.

Перед исполнением операций back и pop программа должна проверять, содержится ли в стеке хотя бы один элемент. Если во входных данных встречается операция back или pop, и при этом стек пуст, то программа должна вместо числового значения вывести строку error.

### Формат ввода

Вводятся команды управления стеком, по одной на строке

### Формат вывода

Программа должна вывести протокол работы стека, по одному сообщению на строке

### Пример

**input.txt**
```c++
push 1
back
exit
```

**output.txt**
```c++
ok
1
bye
```

### [Решение](11.py)

## 12. Правильная скобочная последовательность

Ограничение времени:	1 секунда

Ограничение памяти: 	64Mb

Ввод:	стандартный ввод или input.txt

Вывод:	стандартный вывод или output.txt

Рассмотрим последовательность, состоящую из круглых, квадратных и фигурных скобок. Программа дожна определить, является ли данная скобочная последовательность правильной. Пустая последовательность явлется правильной. Если A – правильная, то последовательности (A), [A], {A} – правильные. Если A и B – правильные последовательности, то последовательность AB – правильная.

### Формат ввода

В единственной строке записана скобочная последовательность, содержащая не более 100000 скобок.

### Формат вывода

Если данная последовательность правильная, то программа должна вывести строку yes, иначе строку no.

### Пример

**input.txt**
```c++
()[]
```

**output.txt**
```c++
yes
```

### [Решение](12.py)

## 13. Постфиксная запись

Ограничение времени:	1 секунда

Ограничение памяти: 	256Mb

Ввод:	стандартный ввод или input.txt

Вывод:	стандартный вывод или output.txt

В постфиксной записи (или обратной польской записи) операция записывается после двух операндов. Например, сумма двух чисел A и B записывается как A B +. Запись B C + D * обозначает привычное нам (B + C) * D, а запись A B C + D * + означает A + (B + C) * D. Достоинство постфиксной записи в том, что она не требует скобок и дополнительных соглашений о приоритете операторов для своего чтения.

### Формат ввода

В единственной строке записано выражение в постфиксной записи, содержащее цифры и операции +, -, *. Цифры и операции разделяются пробелами. В конце строки может быть произвольное количество пробелов.

### Формат вывода

Необходимо вывести значение записанного выражения.

### Пример

**input.txt**
```c++
8 9 + 1 7 - *
```

**output.txt**
```c++
-102
```

### [Решение](13.py)

## 14. Сортировка вагонов lite

Ограничение времени:	1 секунда

Ограничение памяти: 	64Mb

Ввод:	стандартный ввод или input.txt

Вывод:	стандартный вывод или output.txt

К тупику со стороны пути 1 (см. рисунок) подъехал поезд. Разрешается отцепить от поезда один или сразу несколько первых вагонов и завезти их в тупик (при желании, можно даже завезти в тупик сразу весь поезд). После этого часть из этих вагонов вывезти в сторону пути 2. После этого можно завезти в тупик еще несколько вагонов и снова часть оказавшихся вагонов вывезти в сторону пути 2. И так далее (так, что каждый вагон может лишь один раз заехать с пути 1 в тупик, а затем один раз выехать из тупика на путь 2). Заезжать в тупик с пути 2 или выезжать из тупика на путь 1 запрещается. Нельзя с пути 1 попасть на путь 2, не заезжая в тупик.

Известно, в каком порядке изначально идут вагоны поезда. Требуется с помощью указанных операций сделать так, чтобы вагоны поезда шли по порядку (сначала первый, потом второй и т.д., считая от головы поезда, едущего по пути 2 в сторону от тупика). Напишите программу, определяющую, можно ли это сделать.

### Формат ввода

Вводится число N — количество вагонов в поезде (1 ≤ N ≤ 100). Дальше идут номера вагонов в порядке от головы поезда, едущего по пути 1 в сторону тупика. Вагоны пронумерованы натуральными числами от 1 до N, каждое из которых встречается ровно один раз.

### Формат вывода

Если сделать так, чтобы вагоны шли в порядке от 1 до N, считая от головы поезда, когда поезд поедет по пути 2 из тупика, можно, выведите сообщение YES, если это сделать нельзя, выведите NO.

### Пример

**input.txt**
```c++
3
3 2 1
```

**output.txt**
```c++
YES
```

### [Решение](14.py)

## 15. Великое Лайнландское переселение

Ограничение времени:	1 секунда

Ограничение памяти: 	256Mb

Ввод:	стандартный ввод или input.txt

Вывод:	стандартный вывод или output.txt

Лайнландия представляет из себя одномерный мир, являющийся прямой, на котором располагаются N городов, последовательно пронумерованных от 0 до N - 1 . Направление в сторону от первого города к нулевому названо западным, а в обратную — восточным.
Когда в Лайнландии неожиданно начался кризис, все были жители мира стали испытывать глубокое смятение. По всей Лайнландии стали ходить слухи, что на востоке живётся лучше, чем на западе.
Так и началось Великое Лайнландское переселение. Обитатели мира целыми городами отправились на восток, покинув родные улицы, и двигались до тех пор, пока не приходили в город, в котором средняя цена проживания была меньше, чем в родном.

### Формат ввода

В первой строке дано одно число N (2 <= N <= 10^5) —  количество городов в Лайнландии. Во второй строке дано N чисел ai (0 <= ai <= 10^9) — средняя цена проживания в городах с нулевого по (N - 1)-ый соответственно.

### Формат вывода

Для каждого города в порядке с нулевого по (N - 1)-ый выведите номер города, в который переселятся его изначальные жители. Если жители города не остановятся в каком-либо другом городе, отправившись в Восточное Бесконечное Ничто, выведите -1 

### Пример

**input.txt**
```c++
10
1 2 3 2 1 4 2 5 3 1
```

**output.txt**
```c++
-1 4 3 4 -1 6 9 8 9 -1
```

### [Решение](15.py)