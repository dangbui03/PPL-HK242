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
        buf.write("\u0218\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("9\69\u0168\n9\r9\169\u0169\3:\6:\u016d\n:\r:\16:\u016e")
        buf.write("\3:\3:\7:\u0173\n:\f:\16:\u0176\13:\3:\5:\u0179\n:\3:")
        buf.write("\3:\6:\u017d\n:\r:\16:\u017e\3:\5:\u0182\n:\3:\6:\u0185")
        buf.write("\n:\r:\16:\u0186\3:\3:\5:\u018b\n:\3;\3;\3;\7;\u0190\n")
        buf.write(";\f;\16;\u0193\13;\5;\u0195\n;\3<\3<\3<\3<\5<\u019b\n")
        buf.write("<\3<\6<\u019e\n<\r<\16<\u019f\3<\3<\3=\3=\3=\3=\5=\u01a8")
        buf.write("\n=\3=\6=\u01ab\n=\r=\16=\u01ac\3=\3=\3>\3>\3>\3>\5>\u01b5")
        buf.write("\n>\3>\6>\u01b8\n>\r>\16>\u01b9\3>\3>\3?\3?\3?\7?\u01c1")
        buf.write("\n?\f?\16?\u01c4\13?\3?\3?\3?\3@\3@\5@\u01cb\n@\3A\6A")
        buf.write("\u01ce\nA\rA\16A\u01cf\3A\3A\3B\3B\3B\3B\7B\u01d8\nB\f")
        buf.write("B\16B\u01db\13B\3B\3B\3C\3C\3C\3C\3C\7C\u01e4\nC\fC\16")
        buf.write("C\u01e7\13C\3C\3C\3C\3C\3C\3D\3D\3D\3E\3E\3E\7E\u01f4")
        buf.write("\nE\fE\16E\u01f7\13E\3E\3E\3E\5E\u01fc\nE\3E\3E\3F\3F")
        buf.write("\3F\7F\u0203\nF\fF\16F\u0206\13F\3F\3F\3F\3F\5F\u020c")
        buf.write("\nF\3F\3F\3G\3G\3G\3H\3H\3H\3H\5H\u0217\nH\3\u01e5\2I")
        buf.write("\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write("\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31")
        buf.write("\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O")
        buf.write(")Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o\2q\2")
        buf.write("s9u:w;y<{=}>\177?\u0081@\u0083A\u0085B\u0087C\u0089D\u008b")
        buf.write("E\u008d\2\u008f\2\3\2\24\5\2C\\aac|\6\2\62;C\\aac|\3\2")
        buf.write("\62;\4\2GGgg\4\2--//\3\2\63;\3\2\62\63\3\2\629\5\2\62")
        buf.write(";CHch\7\2\f\f\16\17$$))^^\5\2\13\13\16\17\"\"\3\2\17\17")
        buf.write("\3\3\f\f\b\2\f\f\17\17$$))^^dd\5\2\17\17))^^\3\2))\3\2")
        buf.write("$$\b\2))^^ddppttvv\2\u023a\2\3\3\2\2\2\2\5\3\2\2\2\2\7")
        buf.write("\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2")
        buf.write("\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2")
        buf.write("\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2")
        buf.write("\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2")
        buf.write("\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y")
        buf.write("\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2")
        buf.write("c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2")
        buf.write("\2m\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2")
        buf.write("\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2")
        buf.write("\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089")
        buf.write("\3\2\2\2\2\u008b\3\2\2\2\3\u0091\3\2\2\2\5\u0093\3\2\2")
        buf.write("\2\7\u009b\3\2\2\2\t\u009d\3\2\2\2\13\u00a0\3\2\2\2\r")
        buf.write("\u00a5\3\2\2\2\17\u00a9\3\2\2\2\21\u00b0\3\2\2\2\23\u00b5")
        buf.write("\3\2\2\2\25\u00ba\3\2\2\2\27\u00c1\3\2\2\2\31\u00cb\3")
        buf.write("\2\2\2\33\u00d2\3\2\2\2\35\u00d6\3\2\2\2\37\u00dc\3\2")
        buf.write("\2\2!\u00e4\3\2\2\2#\u00ea\3\2\2\2%\u00ee\3\2\2\2\'\u00f7")
        buf.write("\3\2\2\2)\u00fd\3\2\2\2+\u0103\3\2\2\2-\u0107\3\2\2\2")
        buf.write("/\u010c\3\2\2\2\61\u0112\3\2\2\2\63\u0114\3\2\2\2\65\u0116")
        buf.write("\3\2\2\2\67\u0118\3\2\2\29\u011a\3\2\2\2;\u011c\3\2\2")
        buf.write("\2=\u011e\3\2\2\2?\u0121\3\2\2\2A\u0124\3\2\2\2C\u0126")
        buf.write("\3\2\2\2E\u0128\3\2\2\2G\u012b\3\2\2\2I\u012e\3\2\2\2")
        buf.write("K\u0131\3\2\2\2M\u0134\3\2\2\2O\u0136\3\2\2\2Q\u0139\3")
        buf.write("\2\2\2S\u013c\3\2\2\2U\u013f\3\2\2\2W\u0142\3\2\2\2Y\u0145")
        buf.write("\3\2\2\2[\u0147\3\2\2\2]\u0149\3\2\2\2_\u014b\3\2\2\2")
        buf.write("a\u014d\3\2\2\2c\u014f\3\2\2\2e\u0151\3\2\2\2g\u0153\3")
        buf.write("\2\2\2i\u0155\3\2\2\2k\u0157\3\2\2\2m\u0159\3\2\2\2o\u0160")
        buf.write("\3\2\2\2q\u0162\3\2\2\2s\u018a\3\2\2\2u\u0194\3\2\2\2")
        buf.write("w\u019a\3\2\2\2y\u01a7\3\2\2\2{\u01b4\3\2\2\2}\u01bd\3")
        buf.write("\2\2\2\177\u01ca\3\2\2\2\u0081\u01cd\3\2\2\2\u0083\u01d3")
        buf.write("\3\2\2\2\u0085\u01de\3\2\2\2\u0087\u01ed\3\2\2\2\u0089")
        buf.write("\u01f0\3\2\2\2\u008b\u01ff\3\2\2\2\u008d\u020f\3\2\2\2")
        buf.write("\u008f\u0216\3\2\2\2\u0091\u0092\7\17\2\2\u0092\4\3\2")
        buf.write("\2\2\u0093\u0094\7\f\2\2\u0094\6\3\2\2\2\u0095\u009c\5")
        buf.write("A!\2\u0096\u009c\5C\"\2\u0097\u009c\5E#\2\u0098\u009c")
        buf.write("\5G$\2\u0099\u009c\5=\37\2\u009a\u009c\5? \2\u009b\u0095")
        buf.write("\3\2\2\2\u009b\u0096\3\2\2\2\u009b\u0097\3\2\2\2\u009b")
        buf.write("\u0098\3\2\2\2\u009b\u0099\3\2\2\2\u009b\u009a\3\2\2\2")
        buf.write("\u009c\b\3\2\2\2\u009d\u009e\7k\2\2\u009e\u009f\7h\2\2")
        buf.write("\u009f\n\3\2\2\2\u00a0\u00a1\7g\2\2\u00a1\u00a2\7n\2\2")
        buf.write("\u00a2\u00a3\7u\2\2\u00a3\u00a4\7g\2\2\u00a4\f\3\2\2\2")
        buf.write("\u00a5\u00a6\7h\2\2\u00a6\u00a7\7q\2\2\u00a7\u00a8\7t")
        buf.write("\2\2\u00a8\16\3\2\2\2\u00a9\u00aa\7t\2\2\u00aa\u00ab\7")
        buf.write("g\2\2\u00ab\u00ac\7v\2\2\u00ac\u00ad\7w\2\2\u00ad\u00ae")
        buf.write("\7t\2\2\u00ae\u00af\7p\2\2\u00af\20\3\2\2\2\u00b0\u00b1")
        buf.write("\7h\2\2\u00b1\u00b2\7w\2\2\u00b2\u00b3\7p\2\2\u00b3\u00b4")
        buf.write("\7e\2\2\u00b4\22\3\2\2\2\u00b5\u00b6\7v\2\2\u00b6\u00b7")
        buf.write("\7{\2\2\u00b7\u00b8\7r\2\2\u00b8\u00b9\7g\2\2\u00b9\24")
        buf.write("\3\2\2\2\u00ba\u00bb\7u\2\2\u00bb\u00bc\7v\2\2\u00bc\u00bd")
        buf.write("\7t\2\2\u00bd\u00be\7w\2\2\u00be\u00bf\7e\2\2\u00bf\u00c0")
        buf.write("\7v\2\2\u00c0\26\3\2\2\2\u00c1\u00c2\7k\2\2\u00c2\u00c3")
        buf.write("\7p\2\2\u00c3\u00c4\7v\2\2\u00c4\u00c5\7g\2\2\u00c5\u00c6")
        buf.write("\7t\2\2\u00c6\u00c7\7h\2\2\u00c7\u00c8\7c\2\2\u00c8\u00c9")
        buf.write("\7e\2\2\u00c9\u00ca\7g\2\2\u00ca\30\3\2\2\2\u00cb\u00cc")
        buf.write("\7u\2\2\u00cc\u00cd\7v\2\2\u00cd\u00ce\7t\2\2\u00ce\u00cf")
        buf.write("\7k\2\2\u00cf\u00d0\7p\2\2\u00d0\u00d1\7i\2\2\u00d1\32")
        buf.write("\3\2\2\2\u00d2\u00d3\7k\2\2\u00d3\u00d4\7p\2\2\u00d4\u00d5")
        buf.write("\7v\2\2\u00d5\34\3\2\2\2\u00d6\u00d7\7h\2\2\u00d7\u00d8")
        buf.write("\7n\2\2\u00d8\u00d9\7q\2\2\u00d9\u00da\7c\2\2\u00da\u00db")
        buf.write("\7v\2\2\u00db\36\3\2\2\2\u00dc\u00dd\7d\2\2\u00dd\u00de")
        buf.write("\7q\2\2\u00de\u00df\7q\2\2\u00df\u00e0\7n\2\2\u00e0\u00e1")
        buf.write("\7g\2\2\u00e1\u00e2\7c\2\2\u00e2\u00e3\7p\2\2\u00e3 \3")
        buf.write("\2\2\2\u00e4\u00e5\7e\2\2\u00e5\u00e6\7q\2\2\u00e6\u00e7")
        buf.write("\7p\2\2\u00e7\u00e8\7u\2\2\u00e8\u00e9\7v\2\2\u00e9\"")
        buf.write("\3\2\2\2\u00ea\u00eb\7x\2\2\u00eb\u00ec\7c\2\2\u00ec\u00ed")
        buf.write("\7t\2\2\u00ed$\3\2\2\2\u00ee\u00ef\7e\2\2\u00ef\u00f0")
        buf.write("\7q\2\2\u00f0\u00f1\7p\2\2\u00f1\u00f2\7v\2\2\u00f2\u00f3")
        buf.write("\7k\2\2\u00f3\u00f4\7p\2\2\u00f4\u00f5\7w\2\2\u00f5\u00f6")
        buf.write("\7g\2\2\u00f6&\3\2\2\2\u00f7\u00f8\7d\2\2\u00f8\u00f9")
        buf.write("\7t\2\2\u00f9\u00fa\7g\2\2\u00fa\u00fb\7c\2\2\u00fb\u00fc")
        buf.write("\7m\2\2\u00fc(\3\2\2\2\u00fd\u00fe\7t\2\2\u00fe\u00ff")
        buf.write("\7c\2\2\u00ff\u0100\7p\2\2\u0100\u0101\7i\2\2\u0101\u0102")
        buf.write("\7g\2\2\u0102*\3\2\2\2\u0103\u0104\7p\2\2\u0104\u0105")
        buf.write("\7k\2\2\u0105\u0106\7n\2\2\u0106,\3\2\2\2\u0107\u0108")
        buf.write("\7v\2\2\u0108\u0109\7t\2\2\u0109\u010a\7w\2\2\u010a\u010b")
        buf.write("\7g\2\2\u010b.\3\2\2\2\u010c\u010d\7h\2\2\u010d\u010e")
        buf.write("\7c\2\2\u010e\u010f\7n\2\2\u010f\u0110\7u\2\2\u0110\u0111")
        buf.write("\7g\2\2\u0111\60\3\2\2\2\u0112\u0113\7#\2\2\u0113\62\3")
        buf.write("\2\2\2\u0114\u0115\7-\2\2\u0115\64\3\2\2\2\u0116\u0117")
        buf.write("\7/\2\2\u0117\66\3\2\2\2\u0118\u0119\7,\2\2\u01198\3\2")
        buf.write("\2\2\u011a\u011b\7\61\2\2\u011b:\3\2\2\2\u011c\u011d\7")
        buf.write("\'\2\2\u011d<\3\2\2\2\u011e\u011f\7?\2\2\u011f\u0120\7")
        buf.write("?\2\2\u0120>\3\2\2\2\u0121\u0122\7#\2\2\u0122\u0123\7")
        buf.write("?\2\2\u0123@\3\2\2\2\u0124\u0125\7>\2\2\u0125B\3\2\2\2")
        buf.write("\u0126\u0127\7@\2\2\u0127D\3\2\2\2\u0128\u0129\7>\2\2")
        buf.write("\u0129\u012a\7?\2\2\u012aF\3\2\2\2\u012b\u012c\7@\2\2")
        buf.write("\u012c\u012d\7?\2\2\u012dH\3\2\2\2\u012e\u012f\7~\2\2")
        buf.write("\u012f\u0130\7~\2\2\u0130J\3\2\2\2\u0131\u0132\7(\2\2")
        buf.write("\u0132\u0133\7(\2\2\u0133L\3\2\2\2\u0134\u0135\7?\2\2")
        buf.write("\u0135N\3\2\2\2\u0136\u0137\7-\2\2\u0137\u0138\7?\2\2")
        buf.write("\u0138P\3\2\2\2\u0139\u013a\7/\2\2\u013a\u013b\7?\2\2")
        buf.write("\u013bR\3\2\2\2\u013c\u013d\7,\2\2\u013d\u013e\7?\2\2")
        buf.write("\u013eT\3\2\2\2\u013f\u0140\7\61\2\2\u0140\u0141\7?\2")
        buf.write("\2\u0141V\3\2\2\2\u0142\u0143\7\'\2\2\u0143\u0144\7?\2")
        buf.write("\2\u0144X\3\2\2\2\u0145\u0146\7\60\2\2\u0146Z\3\2\2\2")
        buf.write("\u0147\u0148\7<\2\2\u0148\\\3\2\2\2\u0149\u014a\7*\2\2")
        buf.write("\u014a^\3\2\2\2\u014b\u014c\7+\2\2\u014c`\3\2\2\2\u014d")
        buf.write("\u014e\7}\2\2\u014eb\3\2\2\2\u014f\u0150\7\177\2\2\u0150")
        buf.write("d\3\2\2\2\u0151\u0152\7]\2\2\u0152f\3\2\2\2\u0153\u0154")
        buf.write("\7_\2\2\u0154h\3\2\2\2\u0155\u0156\7=\2\2\u0156j\3\2\2")
        buf.write("\2\u0157\u0158\7.\2\2\u0158l\3\2\2\2\u0159\u015d\t\2\2")
        buf.write("\2\u015a\u015c\t\3\2\2\u015b\u015a\3\2\2\2\u015c\u015f")
        buf.write("\3\2\2\2\u015d\u015b\3\2\2\2\u015d\u015e\3\2\2\2\u015e")
        buf.write("n\3\2\2\2\u015f\u015d\3\2\2\2\u0160\u0161\t\4\2\2\u0161")
        buf.write("p\3\2\2\2\u0162\u0164\t\5\2\2\u0163\u0165\t\6\2\2\u0164")
        buf.write("\u0163\3\2\2\2\u0164\u0165\3\2\2\2\u0165\u0167\3\2\2\2")
        buf.write("\u0166\u0168\5o8\2\u0167\u0166\3\2\2\2\u0168\u0169\3\2")
        buf.write("\2\2\u0169\u0167\3\2\2\2\u0169\u016a\3\2\2\2\u016ar\3")
        buf.write("\2\2\2\u016b\u016d\5o8\2\u016c\u016b\3\2\2\2\u016d\u016e")
        buf.write("\3\2\2\2\u016e\u016c\3\2\2\2\u016e\u016f\3\2\2\2\u016f")
        buf.write("\u0170\3\2\2\2\u0170\u0174\7\60\2\2\u0171\u0173\5o8\2")
        buf.write("\u0172\u0171\3\2\2\2\u0173\u0176\3\2\2\2\u0174\u0172\3")
        buf.write("\2\2\2\u0174\u0175\3\2\2\2\u0175\u0178\3\2\2\2\u0176\u0174")
        buf.write("\3\2\2\2\u0177\u0179\5q9\2\u0178\u0177\3\2\2\2\u0178\u0179")
        buf.write("\3\2\2\2\u0179\u018b\3\2\2\2\u017a\u017c\7\60\2\2\u017b")
        buf.write("\u017d\5o8\2\u017c\u017b\3\2\2\2\u017d\u017e\3\2\2\2\u017e")
        buf.write("\u017c\3\2\2\2\u017e\u017f\3\2\2\2\u017f\u0181\3\2\2\2")
        buf.write("\u0180\u0182\5q9\2\u0181\u0180\3\2\2\2\u0181\u0182\3\2")
        buf.write("\2\2\u0182\u018b\3\2\2\2\u0183\u0185\5o8\2\u0184\u0183")
        buf.write("\3\2\2\2\u0185\u0186\3\2\2\2\u0186\u0184\3\2\2\2\u0186")
        buf.write("\u0187\3\2\2\2\u0187\u0188\3\2\2\2\u0188\u0189\5q9\2\u0189")
        buf.write("\u018b\3\2\2\2\u018a\u016c\3\2\2\2\u018a\u017a\3\2\2\2")
        buf.write("\u018a\u0184\3\2\2\2\u018bt\3\2\2\2\u018c\u0195\7\62\2")
        buf.write("\2\u018d\u0191\t\7\2\2\u018e\u0190\5o8\2\u018f\u018e\3")
        buf.write("\2\2\2\u0190\u0193\3\2\2\2\u0191\u018f\3\2\2\2\u0191\u0192")
        buf.write("\3\2\2\2\u0192\u0195\3\2\2\2\u0193\u0191\3\2\2\2\u0194")
        buf.write("\u018c\3\2\2\2\u0194\u018d\3\2\2\2\u0195v\3\2\2\2\u0196")
        buf.write("\u0197\7\62\2\2\u0197\u019b\7d\2\2\u0198\u0199\7\62\2")
        buf.write("\2\u0199\u019b\7D\2\2\u019a\u0196\3\2\2\2\u019a\u0198")
        buf.write("\3\2\2\2\u019b\u019d\3\2\2\2\u019c\u019e\t\b\2\2\u019d")
        buf.write("\u019c\3\2\2\2\u019e\u019f\3\2\2\2\u019f\u019d\3\2\2\2")
        buf.write("\u019f\u01a0\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1\u01a2\b")
        buf.write("<\2\2\u01a2x\3\2\2\2\u01a3\u01a4\7\62\2\2\u01a4\u01a8")
        buf.write("\7q\2\2\u01a5\u01a6\7\62\2\2\u01a6\u01a8\7Q\2\2\u01a7")
        buf.write("\u01a3\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a8\u01aa\3\2\2\2")
        buf.write("\u01a9\u01ab\t\t\2\2\u01aa\u01a9\3\2\2\2\u01ab\u01ac\3")
        buf.write("\2\2\2\u01ac\u01aa\3\2\2\2\u01ac\u01ad\3\2\2\2\u01ad\u01ae")
        buf.write("\3\2\2\2\u01ae\u01af\b=\3\2\u01afz\3\2\2\2\u01b0\u01b1")
        buf.write("\7\62\2\2\u01b1\u01b5\7z\2\2\u01b2\u01b3\7\62\2\2\u01b3")
        buf.write("\u01b5\7Z\2\2\u01b4\u01b0\3\2\2\2\u01b4\u01b2\3\2\2\2")
        buf.write("\u01b5\u01b7\3\2\2\2\u01b6\u01b8\t\n\2\2\u01b7\u01b6\3")
        buf.write("\2\2\2\u01b8\u01b9\3\2\2\2\u01b9\u01b7\3\2\2\2\u01b9\u01ba")
        buf.write("\3\2\2\2\u01ba\u01bb\3\2\2\2\u01bb\u01bc\b>\4\2\u01bc")
        buf.write("|\3\2\2\2\u01bd\u01c2\7$\2\2\u01be\u01c1\5\u008fH\2\u01bf")
        buf.write("\u01c1\n\13\2\2\u01c0\u01be\3\2\2\2\u01c0\u01bf\3\2\2")
        buf.write("\2\u01c1\u01c4\3\2\2\2\u01c2\u01c0\3\2\2\2\u01c2\u01c3")
        buf.write("\3\2\2\2\u01c3\u01c5\3\2\2\2\u01c4\u01c2\3\2\2\2\u01c5")
        buf.write("\u01c6\7$\2\2\u01c6\u01c7\b?\5\2\u01c7~\3\2\2\2\u01c8")
        buf.write("\u01cb\5-\27\2\u01c9\u01cb\5/\30\2\u01ca\u01c8\3\2\2\2")
        buf.write("\u01ca\u01c9\3\2\2\2\u01cb\u0080\3\2\2\2\u01cc\u01ce\t")
        buf.write("\f\2\2\u01cd\u01cc\3\2\2\2\u01ce\u01cf\3\2\2\2\u01cf\u01cd")
        buf.write("\3\2\2\2\u01cf\u01d0\3\2\2\2\u01d0\u01d1\3\2\2\2\u01d1")
        buf.write("\u01d2\bA\6\2\u01d2\u0082\3\2\2\2\u01d3\u01d4\7\61\2\2")
        buf.write("\u01d4\u01d5\7\61\2\2\u01d5\u01d9\3\2\2\2\u01d6\u01d8")
        buf.write("\n\r\2\2\u01d7\u01d6\3\2\2\2\u01d8\u01db\3\2\2\2\u01d9")
        buf.write("\u01d7\3\2\2\2\u01d9\u01da\3\2\2\2\u01da\u01dc\3\2\2\2")
        buf.write("\u01db\u01d9\3\2\2\2\u01dc\u01dd\bB\6\2\u01dd\u0084\3")
        buf.write("\2\2\2\u01de\u01df\7\61\2\2\u01df\u01e0\7,\2\2\u01e0\u01e5")
        buf.write("\3\2\2\2\u01e1\u01e4\5\u0085C\2\u01e2\u01e4\13\2\2\2\u01e3")
        buf.write("\u01e1\3\2\2\2\u01e3\u01e2\3\2\2\2\u01e4\u01e7\3\2\2\2")
        buf.write("\u01e5\u01e6\3\2\2\2\u01e5\u01e3\3\2\2\2\u01e6\u01e8\3")
        buf.write("\2\2\2\u01e7\u01e5\3\2\2\2\u01e8\u01e9\7,\2\2\u01e9\u01ea")
        buf.write("\7\61\2\2\u01ea\u01eb\3\2\2\2\u01eb\u01ec\bC\6\2\u01ec")
        buf.write("\u0086\3\2\2\2\u01ed\u01ee\13\2\2\2\u01ee\u01ef\bD\7\2")
        buf.write("\u01ef\u0088\3\2\2\2\u01f0\u01f5\7$\2\2\u01f1\u01f4\n")
        buf.write("\13\2\2\u01f2\u01f4\5\u008fH\2\u01f3\u01f1\3\2\2\2\u01f3")
        buf.write("\u01f2\3\2\2\2\u01f4\u01f7\3\2\2\2\u01f5\u01f3\3\2\2\2")
        buf.write("\u01f5\u01f6\3\2\2\2\u01f6\u01fb\3\2\2\2\u01f7\u01f5\3")
        buf.write("\2\2\2\u01f8\u01fc\t\16\2\2\u01f9\u01fa\7\17\2\2\u01fa")
        buf.write("\u01fc\7\f\2\2\u01fb\u01f8\3\2\2\2\u01fb\u01f9\3\2\2\2")
        buf.write("\u01fc\u01fd\3\2\2\2\u01fd\u01fe\bE\b\2\u01fe\u008a\3")
        buf.write("\2\2\2\u01ff\u0204\7$\2\2\u0200\u0203\n\17\2\2\u0201\u0203")
        buf.write("\5\u008fH\2\u0202\u0200\3\2\2\2\u0202\u0201\3\2\2\2\u0203")
        buf.write("\u0206\3\2\2\2\u0204\u0202\3\2\2\2\u0204\u0205\3\2\2\2")
        buf.write("\u0205\u020b\3\2\2\2\u0206\u0204\3\2\2\2\u0207\u020c\t")
        buf.write("\20\2\2\u0208\u020c\5\u008dG\2\u0209\u020a\t\21\2\2\u020a")
        buf.write("\u020c\n\22\2\2\u020b\u0207\3\2\2\2\u020b\u0208\3\2\2")
        buf.write("\2\u020b\u0209\3\2\2\2\u020c\u020d\3\2\2\2\u020d\u020e")
        buf.write("\bF\t\2\u020e\u008c\3\2\2\2\u020f\u0210\7^\2\2\u0210\u0211")
        buf.write("\n\23\2\2\u0211\u008e\3\2\2\2\u0212\u0213\7^\2\2\u0213")
        buf.write("\u0217\t\23\2\2\u0214\u0215\t\21\2\2\u0215\u0217\t\22")
        buf.write("\2\2\u0216\u0212\3\2\2\2\u0216\u0214\3\2\2\2\u0217\u0090")
        buf.write("\3\2\2\2$\2\u009b\u015d\u0164\u0169\u016e\u0174\u0178")
        buf.write("\u017e\u0181\u0186\u018a\u0191\u0194\u019a\u019f\u01a7")
        buf.write("\u01ac\u01b4\u01b9\u01c0\u01c2\u01ca\u01cf\u01d9\u01e3")
        buf.write("\u01e5\u01f3\u01f5\u01fb\u0202\u0204\u020b\u0216\n\3<")
        buf.write("\2\3=\3\3>\4\3?\5\b\2\2\3D\6\3E\7\3F\b")
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

                        self.text = str(int(self.text, 2))
                    
     

    def OCT_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
               
                        self.text = str(int(self.text, 8))
                    
     

    def HEX_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                        self.text = str(int(self.text, 16))
                    
     

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

     


