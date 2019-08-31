# Data-management-toolkits-for-translation-projects
my new project

Added add_code file<br>
It was available to use it for the walkthrough text

1st attempt: 
- Time elapsed 18.45 sec

2nd attempt: 
- Time elapsed 12.36 sec.
- The output file was more readable.

Demo:

**Input**

```
My secret project
https://gamefaqs.gamespot.com/gba/931905-yu-gi-oh-double-pack/faqs/36138


Chap 1
4.01 - Chapter 1: The Beginning of Battle City
*******************************************************************************

JOEY: The Battle City Tournament is today, David.
Giải đấu Battle City sẽ diễn ra hôm nay đấy, David.

YUGI: Good morning, David.  Have you made your deck?
Chào buổi sáng, David. Cậu đã chuẩn bị cho bộ bài của cậu chưa?

JOEY: Hey, my new deck is something special.
Này, bộ bài mới của tớ đặc biệt lắm.
```

**Output**
```
My secret project


Chap 1
4.01 - Chapter 1: The Beginning of Battle City

JOEY: The Battle City Tournament is today, David.
Giải đấu Battle City sẽ<line>
diễn ra hôm nay đấy,<new>
David.

YUGI: Good morning, David.  Have you made your deck?
Chào buổi sáng, David.<line>
Cậu đã chuẩn bị cho bộ<new>
bài của cậu chưa?

JOEY: Hey, my new deck is something special.
Này, bộ bài mới của tớ<line>
đặc biệt lắm.
```