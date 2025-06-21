.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is w1 LWorker; from Label2 to Label3
	new PPL4
	dup
	invokespecial PPL4/<init>()V
	astore_1
.var 2 is w2 LPPL5; from Label2 to Label3
	new PPL5
	dup
	invokespecial PPL5/<init>()V
	astore_2
	aload_1
	aload_1
	aload_2
Label3:
Label1:
	return
.limit stack 3
.limit locals 3
.end method

.method public <init>()V
.var 0 is this LMiniGoClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static <clinit>()V
Label0:
Label2:
Label3:
Label1:
	return
.limit stack 0
.limit locals 0
.end method
