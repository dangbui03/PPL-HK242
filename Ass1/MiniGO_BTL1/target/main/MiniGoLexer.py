# Generated from main/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2E")
        buf.write("\u0201\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\3\2\3\2\3\3\3\3\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\5\4\u009c\n\4\3\5\3\5\3\5\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33")
        buf.write("\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3\37\3 \3 \3")
        buf.write(" \3!\3!\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3&\3")
        buf.write("\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,\3,\3")
        buf.write("-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3")
        buf.write("\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\7\67\u015c")
        buf.write("\n\67\f\67\16\67\u015f\13\67\38\38\39\39\59\u0165\n9\3")
        buf.write("9\39\3:\3:\3:\7:\u016c\n:\f:\16:\u016f\13:\5:\u0171\n")
        buf.write(":\3:\5:\u0174\n:\3;\3;\3;\7;\u0179\n;\f;\16;\u017c\13")
        buf.write(";\5;\u017e\n;\3<\3<\3<\3<\5<\u0184\n<\3<\6<\u0187\n<\r")
        buf.write("<\16<\u0188\3<\3<\3=\3=\3=\3=\5=\u0191\n=\3=\6=\u0194")
        buf.write("\n=\r=\16=\u0195\3=\3=\3>\3>\3>\3>\5>\u019e\n>\3>\6>\u01a1")
        buf.write("\n>\r>\16>\u01a2\3>\3>\3?\3?\3?\7?\u01aa\n?\f?\16?\u01ad")
        buf.write("\13?\3?\3?\3?\3@\3@\5@\u01b4\n@\3A\6A\u01b7\nA\rA\16A")
        buf.write("\u01b8\3A\3A\3B\3B\3B\3B\7B\u01c1\nB\fB\16B\u01c4\13B")
        buf.write("\3B\3B\3C\3C\3C\3C\3C\7C\u01cd\nC\fC\16C\u01d0\13C\3C")
        buf.write("\3C\3C\3C\3C\3D\3D\3D\3E\3E\3E\7E\u01dd\nE\fE\16E\u01e0")
        buf.write("\13E\3E\3E\3E\5E\u01e5\nE\3E\3E\3F\3F\3F\7F\u01ec\nF\f")
        buf.write("F\16F\u01ef\13F\3F\3F\3F\3F\5F\u01f5\nF\3F\3F\3G\3G\3")
        buf.write("G\3H\3H\3H\3H\5H\u0200\nH\3\u01ce\2I\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37")
        buf.write("\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34")
        buf.write("\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_")
        buf.write("\61a\62c\63e\64g\65i\66k\67m8o\2q\2s9u:w;y<{=}>\177?\u0081")
        buf.write("@\u0083A\u0085B\u0087C\u0089D\u008bE\u008d\2\u008f\2\3")
        buf.write("\2\24\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\4\2GGgg\4\2--")
        buf.write("//\3\2\63;\3\2\62\63\3\2\629\5\2\62;CHch\7\2\f\f\16\17")
        buf.write("$$))^^\5\2\13\13\16\17\"\"\4\2\f\f\17\17\3\3\f\f\b\2\f")
        buf.write("\f\17\17$$))^^dd\5\2\17\17))^^\3\2))\3\2$$\b\2))^^ddp")
        buf.write("pttvv\2\u021d\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t")
        buf.write("\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3")
        buf.write("\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2")
        buf.write("\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2")
        buf.write("\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2")
        buf.write("\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e")
        buf.write("\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2")
        buf.write("s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2")
        buf.write("\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2")
        buf.write("\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2")
        buf.write("\u008b\3\2\2\2\3\u0091\3\2\2\2\5\u0093\3\2\2\2\7\u009b")
        buf.write("\3\2\2\2\t\u009d\3\2\2\2\13\u00a0\3\2\2\2\r\u00a5\3\2")
        buf.write("\2\2\17\u00a9\3\2\2\2\21\u00b0\3\2\2\2\23\u00b5\3\2\2")
        buf.write("\2\25\u00ba\3\2\2\2\27\u00c1\3\2\2\2\31\u00cb\3\2\2\2")
        buf.write("\33\u00d2\3\2\2\2\35\u00d6\3\2\2\2\37\u00dc\3\2\2\2!\u00e4")
        buf.write("\3\2\2\2#\u00ea\3\2\2\2%\u00ee\3\2\2\2\'\u00f7\3\2\2\2")
        buf.write(")\u00fd\3\2\2\2+\u0103\3\2\2\2-\u0107\3\2\2\2/\u010c\3")
        buf.write("\2\2\2\61\u0112\3\2\2\2\63\u0114\3\2\2\2\65\u0116\3\2")
        buf.write("\2\2\67\u0118\3\2\2\29\u011a\3\2\2\2;\u011c\3\2\2\2=\u011e")
        buf.write("\3\2\2\2?\u0121\3\2\2\2A\u0124\3\2\2\2C\u0126\3\2\2\2")
        buf.write("E\u0128\3\2\2\2G\u012b\3\2\2\2I\u012e\3\2\2\2K\u0131\3")
        buf.write("\2\2\2M\u0134\3\2\2\2O\u0136\3\2\2\2Q\u0139\3\2\2\2S\u013c")
        buf.write("\3\2\2\2U\u013f\3\2\2\2W\u0142\3\2\2\2Y\u0145\3\2\2\2")
        buf.write("[\u0147\3\2\2\2]\u0149\3\2\2\2_\u014b\3\2\2\2a\u014d\3")
        buf.write("\2\2\2c\u014f\3\2\2\2e\u0151\3\2\2\2g\u0153\3\2\2\2i\u0155")
        buf.write("\3\2\2\2k\u0157\3\2\2\2m\u0159\3\2\2\2o\u0160\3\2\2\2")
        buf.write("q\u0162\3\2\2\2s\u0168\3\2\2\2u\u017d\3\2\2\2w\u0183\3")
        buf.write("\2\2\2y\u0190\3\2\2\2{\u019d\3\2\2\2}\u01a6\3\2\2\2\177")
        buf.write("\u01b3\3\2\2\2\u0081\u01b6\3\2\2\2\u0083\u01bc\3\2\2\2")
        buf.write("\u0085\u01c7\3\2\2\2\u0087\u01d6\3\2\2\2\u0089\u01d9\3")
        buf.write("\2\2\2\u008b\u01e8\3\2\2\2\u008d\u01f8\3\2\2\2\u008f\u01ff")
        buf.write("\3\2\2\2\u0091\u0092\7\17\2\2\u0092\4\3\2\2\2\u0093\u0094")
        buf.write("\7\f\2\2\u0094\6\3\2\2\2\u0095\u009c\5A!\2\u0096\u009c")
        buf.write("\5C\"\2\u0097\u009c\5E#\2\u0098\u009c\5G$\2\u0099\u009c")
        buf.write("\5=\37\2\u009a\u009c\5? \2\u009b\u0095\3\2\2\2\u009b\u0096")
        buf.write("\3\2\2\2\u009b\u0097\3\2\2\2\u009b\u0098\3\2\2\2\u009b")
        buf.write("\u0099\3\2\2\2\u009b\u009a\3\2\2\2\u009c\b\3\2\2\2\u009d")
        buf.write("\u009e\7k\2\2\u009e\u009f\7h\2\2\u009f\n\3\2\2\2\u00a0")
        buf.write("\u00a1\7g\2\2\u00a1\u00a2\7n\2\2\u00a2\u00a3\7u\2\2\u00a3")
        buf.write("\u00a4\7g\2\2\u00a4\f\3\2\2\2\u00a5\u00a6\7h\2\2\u00a6")
        buf.write("\u00a7\7q\2\2\u00a7\u00a8\7t\2\2\u00a8\16\3\2\2\2\u00a9")
        buf.write("\u00aa\7t\2\2\u00aa\u00ab\7g\2\2\u00ab\u00ac\7v\2\2\u00ac")
        buf.write("\u00ad\7w\2\2\u00ad\u00ae\7t\2\2\u00ae\u00af\7p\2\2\u00af")
        buf.write("\20\3\2\2\2\u00b0\u00b1\7h\2\2\u00b1\u00b2\7w\2\2\u00b2")
        buf.write("\u00b3\7p\2\2\u00b3\u00b4\7e\2\2\u00b4\22\3\2\2\2\u00b5")
        buf.write("\u00b6\7v\2\2\u00b6\u00b7\7{\2\2\u00b7\u00b8\7r\2\2\u00b8")
        buf.write("\u00b9\7g\2\2\u00b9\24\3\2\2\2\u00ba\u00bb\7u\2\2\u00bb")
        buf.write("\u00bc\7v\2\2\u00bc\u00bd\7t\2\2\u00bd\u00be\7w\2\2\u00be")
        buf.write("\u00bf\7e\2\2\u00bf\u00c0\7v\2\2\u00c0\26\3\2\2\2\u00c1")
        buf.write("\u00c2\7k\2\2\u00c2\u00c3\7p\2\2\u00c3\u00c4\7v\2\2\u00c4")
        buf.write("\u00c5\7g\2\2\u00c5\u00c6\7t\2\2\u00c6\u00c7\7h\2\2\u00c7")
        buf.write("\u00c8\7c\2\2\u00c8\u00c9\7e\2\2\u00c9\u00ca\7g\2\2\u00ca")
        buf.write("\30\3\2\2\2\u00cb\u00cc\7u\2\2\u00cc\u00cd\7v\2\2\u00cd")
        buf.write("\u00ce\7t\2\2\u00ce\u00cf\7k\2\2\u00cf\u00d0\7p\2\2\u00d0")
        buf.write("\u00d1\7i\2\2\u00d1\32\3\2\2\2\u00d2\u00d3\7k\2\2\u00d3")
        buf.write("\u00d4\7p\2\2\u00d4\u00d5\7v\2\2\u00d5\34\3\2\2\2\u00d6")
        buf.write("\u00d7\7h\2\2\u00d7\u00d8\7n\2\2\u00d8\u00d9\7q\2\2\u00d9")
        buf.write("\u00da\7c\2\2\u00da\u00db\7v\2\2\u00db\36\3\2\2\2\u00dc")
        buf.write("\u00dd\7d\2\2\u00dd\u00de\7q\2\2\u00de\u00df\7q\2\2\u00df")
        buf.write("\u00e0\7n\2\2\u00e0\u00e1\7g\2\2\u00e1\u00e2\7c\2\2\u00e2")
        buf.write("\u00e3\7p\2\2\u00e3 \3\2\2\2\u00e4\u00e5\7e\2\2\u00e5")
        buf.write("\u00e6\7q\2\2\u00e6\u00e7\7p\2\2\u00e7\u00e8\7u\2\2\u00e8")
        buf.write("\u00e9\7v\2\2\u00e9\"\3\2\2\2\u00ea\u00eb\7x\2\2\u00eb")
        buf.write("\u00ec\7c\2\2\u00ec\u00ed\7t\2\2\u00ed$\3\2\2\2\u00ee")
        buf.write("\u00ef\7e\2\2\u00ef\u00f0\7q\2\2\u00f0\u00f1\7p\2\2\u00f1")
        buf.write("\u00f2\7v\2\2\u00f2\u00f3\7k\2\2\u00f3\u00f4\7p\2\2\u00f4")
        buf.write("\u00f5\7w\2\2\u00f5\u00f6\7g\2\2\u00f6&\3\2\2\2\u00f7")
        buf.write("\u00f8\7d\2\2\u00f8\u00f9\7t\2\2\u00f9\u00fa\7g\2\2\u00fa")
        buf.write("\u00fb\7c\2\2\u00fb\u00fc\7m\2\2\u00fc(\3\2\2\2\u00fd")
        buf.write("\u00fe\7t\2\2\u00fe\u00ff\7c\2\2\u00ff\u0100\7p\2\2\u0100")
        buf.write("\u0101\7i\2\2\u0101\u0102\7g\2\2\u0102*\3\2\2\2\u0103")
        buf.write("\u0104\7p\2\2\u0104\u0105\7k\2\2\u0105\u0106\7n\2\2\u0106")
        buf.write(",\3\2\2\2\u0107\u0108\7v\2\2\u0108\u0109\7t\2\2\u0109")
        buf.write("\u010a\7w\2\2\u010a\u010b\7g\2\2\u010b.\3\2\2\2\u010c")
        buf.write("\u010d\7h\2\2\u010d\u010e\7c\2\2\u010e\u010f\7n\2\2\u010f")
        buf.write("\u0110\7u\2\2\u0110\u0111\7g\2\2\u0111\60\3\2\2\2\u0112")
        buf.write("\u0113\7#\2\2\u0113\62\3\2\2\2\u0114\u0115\7-\2\2\u0115")
        buf.write("\64\3\2\2\2\u0116\u0117\7/\2\2\u0117\66\3\2\2\2\u0118")
        buf.write("\u0119\7,\2\2\u01198\3\2\2\2\u011a\u011b\7\61\2\2\u011b")
        buf.write(":\3\2\2\2\u011c\u011d\7\'\2\2\u011d<\3\2\2\2\u011e\u011f")
        buf.write("\7?\2\2\u011f\u0120\7?\2\2\u0120>\3\2\2\2\u0121\u0122")
        buf.write("\7#\2\2\u0122\u0123\7?\2\2\u0123@\3\2\2\2\u0124\u0125")
        buf.write("\7>\2\2\u0125B\3\2\2\2\u0126\u0127\7@\2\2\u0127D\3\2\2")
        buf.write("\2\u0128\u0129\7>\2\2\u0129\u012a\7?\2\2\u012aF\3\2\2")
        buf.write("\2\u012b\u012c\7@\2\2\u012c\u012d\7?\2\2\u012dH\3\2\2")
        buf.write("\2\u012e\u012f\7~\2\2\u012f\u0130\7~\2\2\u0130J\3\2\2")
        buf.write("\2\u0131\u0132\7(\2\2\u0132\u0133\7(\2\2\u0133L\3\2\2")
        buf.write("\2\u0134\u0135\7?\2\2\u0135N\3\2\2\2\u0136\u0137\7-\2")
        buf.write("\2\u0137\u0138\7?\2\2\u0138P\3\2\2\2\u0139\u013a\7/\2")
        buf.write("\2\u013a\u013b\7?\2\2\u013bR\3\2\2\2\u013c\u013d\7,\2")
        buf.write("\2\u013d\u013e\7?\2\2\u013eT\3\2\2\2\u013f\u0140\7\61")
        buf.write("\2\2\u0140\u0141\7?\2\2\u0141V\3\2\2\2\u0142\u0143\7\'")
        buf.write("\2\2\u0143\u0144\7?\2\2\u0144X\3\2\2\2\u0145\u0146\7\60")
        buf.write("\2\2\u0146Z\3\2\2\2\u0147\u0148\7<\2\2\u0148\\\3\2\2\2")
        buf.write("\u0149\u014a\7*\2\2\u014a^\3\2\2\2\u014b\u014c\7+\2\2")
        buf.write("\u014c`\3\2\2\2\u014d\u014e\7}\2\2\u014eb\3\2\2\2\u014f")
        buf.write("\u0150\7\177\2\2\u0150d\3\2\2\2\u0151\u0152\7]\2\2\u0152")
        buf.write("f\3\2\2\2\u0153\u0154\7_\2\2\u0154h\3\2\2\2\u0155\u0156")
        buf.write("\7=\2\2\u0156j\3\2\2\2\u0157\u0158\7.\2\2\u0158l\3\2\2")
        buf.write("\2\u0159\u015d\t\2\2\2\u015a\u015c\t\3\2\2\u015b\u015a")
        buf.write("\3\2\2\2\u015c\u015f\3\2\2\2\u015d\u015b\3\2\2\2\u015d")
        buf.write("\u015e\3\2\2\2\u015en\3\2\2\2\u015f\u015d\3\2\2\2\u0160")
        buf.write("\u0161\t\4\2\2\u0161p\3\2\2\2\u0162\u0164\t\5\2\2\u0163")
        buf.write("\u0165\t\6\2\2\u0164\u0163\3\2\2\2\u0164\u0165\3\2\2\2")
        buf.write("\u0165\u0166\3\2\2\2\u0166\u0167\5u;\2\u0167r\3\2\2\2")
        buf.write("\u0168\u0170\5u;\2\u0169\u016d\7\60\2\2\u016a\u016c\5")
        buf.write("o8\2\u016b\u016a\3\2\2\2\u016c\u016f\3\2\2\2\u016d\u016b")
        buf.write("\3\2\2\2\u016d\u016e\3\2\2\2\u016e\u0171\3\2\2\2\u016f")
        buf.write("\u016d\3\2\2\2\u0170\u0169\3\2\2\2\u0170\u0171\3\2\2\2")
        buf.write("\u0171\u0173\3\2\2\2\u0172\u0174\5q9\2\u0173\u0172\3\2")
        buf.write("\2\2\u0173\u0174\3\2\2\2\u0174t\3\2\2\2\u0175\u017e\7")
        buf.write("\62\2\2\u0176\u017a\t\7\2\2\u0177\u0179\5o8\2\u0178\u0177")
        buf.write("\3\2\2\2\u0179\u017c\3\2\2\2\u017a\u0178\3\2\2\2\u017a")
        buf.write("\u017b\3\2\2\2\u017b\u017e\3\2\2\2\u017c\u017a\3\2\2\2")
        buf.write("\u017d\u0175\3\2\2\2\u017d\u0176\3\2\2\2\u017ev\3\2\2")
        buf.write("\2\u017f\u0180\7\62\2\2\u0180\u0184\7d\2\2\u0181\u0182")
        buf.write("\7\62\2\2\u0182\u0184\7D\2\2\u0183\u017f\3\2\2\2\u0183")
        buf.write("\u0181\3\2\2\2\u0184\u0186\3\2\2\2\u0185\u0187\t\b\2\2")
        buf.write("\u0186\u0185\3\2\2\2\u0187\u0188\3\2\2\2\u0188\u0186\3")
        buf.write("\2\2\2\u0188\u0189\3\2\2\2\u0189\u018a\3\2\2\2\u018a\u018b")
        buf.write("\b<\2\2\u018bx\3\2\2\2\u018c\u018d\7\62\2\2\u018d\u0191")
        buf.write("\7q\2\2\u018e\u018f\7\62\2\2\u018f\u0191\7Q\2\2\u0190")
        buf.write("\u018c\3\2\2\2\u0190\u018e\3\2\2\2\u0191\u0193\3\2\2\2")
        buf.write("\u0192\u0194\t\t\2\2\u0193\u0192\3\2\2\2\u0194\u0195\3")
        buf.write("\2\2\2\u0195\u0193\3\2\2\2\u0195\u0196\3\2\2\2\u0196\u0197")
        buf.write("\3\2\2\2\u0197\u0198\b=\3\2\u0198z\3\2\2\2\u0199\u019a")
        buf.write("\7\62\2\2\u019a\u019e\7z\2\2\u019b\u019c\7\62\2\2\u019c")
        buf.write("\u019e\7Z\2\2\u019d\u0199\3\2\2\2\u019d\u019b\3\2\2\2")
        buf.write("\u019e\u01a0\3\2\2\2\u019f\u01a1\t\n\2\2\u01a0\u019f\3")
        buf.write("\2\2\2\u01a1\u01a2\3\2\2\2\u01a2\u01a0\3\2\2\2\u01a2\u01a3")
        buf.write("\3\2\2\2\u01a3\u01a4\3\2\2\2\u01a4\u01a5\b>\4\2\u01a5")
        buf.write("|\3\2\2\2\u01a6\u01ab\7$\2\2\u01a7\u01aa\5\u008fH\2\u01a8")
        buf.write("\u01aa\n\13\2\2\u01a9\u01a7\3\2\2\2\u01a9\u01a8\3\2\2")
        buf.write("\2\u01aa\u01ad\3\2\2\2\u01ab\u01a9\3\2\2\2\u01ab\u01ac")
        buf.write("\3\2\2\2\u01ac\u01ae\3\2\2\2\u01ad\u01ab\3\2\2\2\u01ae")
        buf.write("\u01af\7$\2\2\u01af\u01b0\b?\5\2\u01b0~\3\2\2\2\u01b1")
        buf.write("\u01b4\5-\27\2\u01b2\u01b4\5/\30\2\u01b3\u01b1\3\2\2\2")
        buf.write("\u01b3\u01b2\3\2\2\2\u01b4\u0080\3\2\2\2\u01b5\u01b7\t")
        buf.write("\f\2\2\u01b6\u01b5\3\2\2\2\u01b7\u01b8\3\2\2\2\u01b8\u01b6")
        buf.write("\3\2\2\2\u01b8\u01b9\3\2\2\2\u01b9\u01ba\3\2\2\2\u01ba")
        buf.write("\u01bb\bA\6\2\u01bb\u0082\3\2\2\2\u01bc\u01bd\7\61\2\2")
        buf.write("\u01bd\u01be\7\61\2\2\u01be\u01c2\3\2\2\2\u01bf\u01c1")
        buf.write("\n\r\2\2\u01c0\u01bf\3\2\2\2\u01c1\u01c4\3\2\2\2\u01c2")
        buf.write("\u01c0\3\2\2\2\u01c2\u01c3\3\2\2\2\u01c3\u01c5\3\2\2\2")
        buf.write("\u01c4\u01c2\3\2\2\2\u01c5\u01c6\bB\6\2\u01c6\u0084\3")
        buf.write("\2\2\2\u01c7\u01c8\7\61\2\2\u01c8\u01c9\7,\2\2\u01c9\u01ce")
        buf.write("\3\2\2\2\u01ca\u01cd\5\u0085C\2\u01cb\u01cd\13\2\2\2\u01cc")
        buf.write("\u01ca\3\2\2\2\u01cc\u01cb\3\2\2\2\u01cd\u01d0\3\2\2\2")
        buf.write("\u01ce\u01cf\3\2\2\2\u01ce\u01cc\3\2\2\2\u01cf\u01d1\3")
        buf.write("\2\2\2\u01d0\u01ce\3\2\2\2\u01d1\u01d2\7,\2\2\u01d2\u01d3")
        buf.write("\7\61\2\2\u01d3\u01d4\3\2\2\2\u01d4\u01d5\bC\6\2\u01d5")
        buf.write("\u0086\3\2\2\2\u01d6\u01d7\13\2\2\2\u01d7\u01d8\bD\7\2")
        buf.write("\u01d8\u0088\3\2\2\2\u01d9\u01de\7$\2\2\u01da\u01dd\n")
        buf.write("\13\2\2\u01db\u01dd\5\u008fH\2\u01dc\u01da\3\2\2\2\u01dc")
        buf.write("\u01db\3\2\2\2\u01dd\u01e0\3\2\2\2\u01de\u01dc\3\2\2\2")
        buf.write("\u01de\u01df\3\2\2\2\u01df\u01e4\3\2\2\2\u01e0\u01de\3")
        buf.write("\2\2\2\u01e1\u01e5\t\16\2\2\u01e2\u01e3\7\17\2\2\u01e3")
        buf.write("\u01e5\7\f\2\2\u01e4\u01e1\3\2\2\2\u01e4\u01e2\3\2\2\2")
        buf.write("\u01e5\u01e6\3\2\2\2\u01e6\u01e7\bE\b\2\u01e7\u008a\3")
        buf.write("\2\2\2\u01e8\u01ed\7$\2\2\u01e9\u01ec\n\17\2\2\u01ea\u01ec")
        buf.write("\5\u008fH\2\u01eb\u01e9\3\2\2\2\u01eb\u01ea\3\2\2\2\u01ec")
        buf.write("\u01ef\3\2\2\2\u01ed\u01eb\3\2\2\2\u01ed\u01ee\3\2\2\2")
        buf.write("\u01ee\u01f4\3\2\2\2\u01ef\u01ed\3\2\2\2\u01f0\u01f5\t")
        buf.write("\20\2\2\u01f1\u01f5\5\u008dG\2\u01f2\u01f3\t\21\2\2\u01f3")
        buf.write("\u01f5\n\22\2\2\u01f4\u01f0\3\2\2\2\u01f4\u01f1\3\2\2")
        buf.write("\2\u01f4\u01f2\3\2\2\2\u01f5\u01f6\3\2\2\2\u01f6\u01f7")
        buf.write("\bF\t\2\u01f7\u008c\3\2\2\2\u01f8\u01f9\7^\2\2\u01f9\u01fa")
        buf.write("\n\23\2\2\u01fa\u008e\3\2\2\2\u01fb\u01fc\7^\2\2\u01fc")
        buf.write("\u0200\t\23\2\2\u01fd\u01fe\t\21\2\2\u01fe\u0200\t\22")
        buf.write("\2\2\u01ff\u01fb\3\2\2\2\u01ff\u01fd\3\2\2\2\u0200\u0090")
        buf.write("\3\2\2\2\37\2\u009b\u015d\u0164\u016d\u0170\u0173\u017a")
        buf.write("\u017d\u0183\u0188\u0190\u0195\u019d\u01a2\u01a9\u01ab")
        buf.write("\u01b3\u01b8\u01c2\u01cc\u01ce\u01dc\u01de\u01e4\u01eb")
        buf.write("\u01ed\u01f4\u01ff\n\3<\2\3=\3\3>\4\3?\5\b\2\2\3D\6\3")
        buf.write("E\7\3F\b")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    REL = 3
    IF = 4
    ELSE = 5
    FOR = 6
    RETURN = 7
    FUNC = 8
    TYPE = 9
    STRUCT = 10
    INTERFACE = 11
    STRING = 12
    INT = 13
    FLOAT = 14
    BOOLEAN = 15
    CONST = 16
    VAR = 17
    CONTINUE = 18
    BREAK = 19
    RANGE = 20
    NIL = 21
    TRUE = 22
    FALSE = 23
    NOT = 24
    ADD = 25
    MINUS = 26
    MUL = 27
    DIV = 28
    MOD = 29
    EQUAL = 30
    DIFF = 31
    LT = 32
    GT = 33
    LE = 34
    GE = 35
    OR = 36
    AND = 37
    ASSIGN = 38
    ADD_ASSIGN = 39
    MINUS_ASSIGN = 40
    MULT_ASSIGN = 41
    DIV_ASSIGN = 42
    REM_ASSIGN = 43
    DOT = 44
    COLON = 45
    LPAREN = 46
    RPAREN = 47
    LBRACE = 48
    RBRACE = 49
    LBRACK = 50
    RBRACK = 51
    SEMI = 52
    COMMA = 53
    ID = 54
    FLOAT_LIT = 55
    DEC_LIT = 56
    BIN_LIT = 57
    OCT_LIT = 58
    HEX_LIT = 59
    STR_LIT = 60
    BOOL_LIT = 61
    WS = 62
    LINE_COMMENT = 63
    BLOCK_COMMENT = 64
    ERROR_CHAR = 65
    UNCLOSE_STRING = 66
    ILLEGAL_ESCAPE = 67

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'\r'", "'\n'", "'if'", "'else'", "'for'", "'return'", "'func'", 
            "'type'", "'struct'", "'interface'", "'string'", "'int'", "'float'", 
            "'boolean'", "'const'", "'var'", "'continue'", "'break'", "'range'", 
            "'nil'", "'true'", "'false'", "'!'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'||'", 
            "'&&'", "'='", "'+='", "'-='", "'*='", "'/='", "'%='", "'.'", 
            "':'", "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", "','" ]

    symbolicNames = [ "<INVALID>",
            "REL", "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", 
            "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", 
            "CONTINUE", "BREAK", "RANGE", "NIL", "TRUE", "FALSE", "NOT", 
            "ADD", "MINUS", "MUL", "DIV", "MOD", "EQUAL", "DIFF", "LT", 
            "GT", "LE", "GE", "OR", "AND", "ASSIGN", "ADD_ASSIGN", "MINUS_ASSIGN", 
            "MULT_ASSIGN", "DIV_ASSIGN", "REM_ASSIGN", "DOT", "COLON", "LPAREN", 
            "RPAREN", "LBRACE", "RBRACE", "LBRACK", "RBRACK", "SEMI", "COMMA", 
            "ID", "FLOAT_LIT", "DEC_LIT", "BIN_LIT", "OCT_LIT", "HEX_LIT", 
            "STR_LIT", "BOOL_LIT", "WS", "LINE_COMMENT", "BLOCK_COMMENT", 
            "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "T__1", "REL", "IF", "ELSE", "FOR", "RETURN", 
                  "FUNC", "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", 
                  "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", "BREAK", 
                  "RANGE", "NIL", "TRUE", "FALSE", "NOT", "ADD", "MINUS", 
                  "MUL", "DIV", "MOD", "EQUAL", "DIFF", "LT", "GT", "LE", 
                  "GE", "OR", "AND", "ASSIGN", "ADD_ASSIGN", "MINUS_ASSIGN", 
                  "MULT_ASSIGN", "DIV_ASSIGN", "REM_ASSIGN", "DOT", "COLON", 
                  "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACK", "RBRACK", 
                  "SEMI", "COMMA", "ID", "DIGIT", "EXP", "FLOAT_LIT", "DEC_LIT", 
                  "BIN_LIT", "OCT_LIT", "HEX_LIT", "STR_LIT", "BOOL_LIT", 
                  "WS", "LINE_COMMENT", "BLOCK_COMMENT", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "IllegalEscape", "ESCAPE_SEQ" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        if tk == self.UNCLOSE_STRING:       
            result = super().emit();
            raise UncloseString(result.text);
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            raise IllegalEscape(result.text);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text); 
        else:
            return super().emit();


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[58] = self.BIN_LIT_action 
            actions[59] = self.OCT_LIT_action 
            actions[60] = self.HEX_LIT_action 
            actions[61] = self.STR_LIT_action 
            actions[66] = self.ERROR_CHAR_action 
            actions[67] = self.UNCLOSE_STRING_action 
            actions[68] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def BIN_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                        self.text = str(int(self.text[2:], 2))
                    
     

    def OCT_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
               
                        self.text = str(int(self.text[2:], 8))
                    
     

    def HEX_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                        self.text = str(int(self.text[2:], 16))
                    
     

    def STR_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            self.text = self.text[1:-1]
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

                if(len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
                    raise UncloseString(self.text[1:-2])
                elif (self.text[-1] == '\n'):
                    raise UncloseString(self.text[1:-1])
                else:
                    raise UncloseString(self.text[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:

            	raise IllegalEscape(self.text[1:])

     


