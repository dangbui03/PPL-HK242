.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static global I

.method public static fvoid()V
Label0:
Label2:
Label3:
Label1:
	return
.limit stack 1
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is local Ljava/lang/String; from Label2 to Label3
	ldc "a"
	astore_1
	aload_1
	ldc "c"
	fadd
	astore_1
Label3:
Label1:
	return
.limit stack 4
.limit locals 2
.end method

.method public static fint()I
Label0:
Label2:
	iconst_1
	ireturn
Label3:
Label1:
.limit stack 1
.limit locals 0
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
.var 0 is global I from Label2 to Label3
	invokestatic MiniGoClass/fint()I
	istore_0
Label3:
Label1:
	return
.limit stack 1
.limit locals 1
.end method
