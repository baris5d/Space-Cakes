# Xtreme	Driving

**Problem	Statement**

Alice,	one	of	the	IEEEXtreme	participants,	is	on	her	way	to	her	university	to	take	part	in	this	year's	contest.
To	get	to	the	university	she	has	to	drive	on	a	four	lane	highway,	but	as	the	highway	is	very	long	she	quickly
becomes	bored.	She	decides	to	practice	for	the	contest	by	thinking	about	some	problems	related	to	the
highway	she's	driving	on.	She	comes	up	with	the	following	problem:

Let's	say	that,	in	a	single	unit	of	time,	her	car,	which	is	of	unit-length,	can	perform	one	of	the	following
three	actions:

```
Drive	one	unit	forward,	staying	in	the	same	lane
```
```
If	the	car	is	not	on	the	left-most	lane,	drive	one	unit	forward	and	switch	to	the	lane	on	the	left
```
```
If	the	car	is	not	on	the	right-most	lane,	drive	one	unit	forward	and	switch	to	the	lane	on	the	right
```
If	the	highway	is	K	units	in	length,	in	how	many	ways	is	it	possible	to	drive	through	the	highway,	provided
that	she	starts	on	the	first	unit	of	the	highway	at	the	left-most	lane,	and	ends	at	the	last	unit	of	the	highway,
also	at	the	left-most	lane?

As	she's	been	training	very	hard	for	the	contest,	it	doesn't	take	her	long	to	come	up	with	a	solution	to	this
problem.	But	all	of	a	sudden,	out	of	nowhere,	a	large	cow	appears	in	front	of	her	car,	and	she	just	barely
manages	to	avoid	crashing	into	it.	She	got	a	bit	too	distracted	thinking	about	the	problem...	But	this	incident
gives	her	an	idea:	what	if	the	highway	had	a	set	of	stationary	cows	that	the	car	must	avoid	crashing	into?

Unfortunately	she	doesn't	have	time	to	think	about	this	version	of	the	problem	as	she	just	arrived	at	the
university	and	the	contest	is	about	to	start.	When	the	contest	starts,	she	is	very	surprised	to	see	that	the
problem	she	was	thinking	about	is	just	like	one	of	the	problems	presented	in	the	contest.	What	a
coincidence!	Again	her	hard	practice	pays	off	and	she	quickly	solves	the	problem.	But	the	real	question	is,
can	you?

**Input	Format**

Input	begins	with	two	integers,	K,	the	length	of	the	highway,	and	N,	the	number	of	cows	standing	on	the
highway,	subject	to	the	following	constraints:

2	<=	K	<=	

0	<=	N	<=	

N	<=	4(K	-	2)

Then	follow	N	lines.	The	i 	line	contains	two	integers	describing	the	location	of	the	i 	cow,	x,	the	lane	on
which	the	cow	is	standing	(1	being	the	left-most,	and	4	being	the	right-most),	and	y,	the	unit	on	which	the
cow	is	standing,	subject	to	the	following	constraints:

1	<=	x	<=	

1	<	y	<	K

Notice	that	no	cows	are	on	the	first	or	last	unit	of	the	highway.	It	is	also	guaranteed	that	no	two	cows	share
the	same	position.

**Output	Format**

You	are	to	output	the	number	of	ways	to	drive	from	the	left-most	lane	at	the	first	unit	of	the	highway	to	the
left-most	lane	at	the	K 	unit	of	the	highway	subject	to	the	rules	described	above,	and	the	additional
constraint	that	the	car	must	not	drive	to	a	position	occupied	by	a	cow.

As	the	number	of	ways	can	be	quite	large,	please	output	the	answer	modulo	10 	+	7.	Note	that	this	is	the
same	as	the	remainder	when	dividing	the	number	of	ways	by	10 	+	7.

**Sample	Input**

```
5	
1	
2	3	
```
**Sample	Output**

```
3
```
**Explanation**

In	this	example	there	are	three	ways	to	drive	through	the	highway,	and	they	are	shown	in	the	following
figures.	Notice	that	the	car	can	drive	in	between	cows	(as	long	as	other	driving	rules	are	fulfilled),	but	it
must	not	drive	to	a	unit	occupied	by	a	cow.



Note:	Two	more	sample	test	cases	are	available	if	you	click	on	the	"Run"	button.