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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2D")
        buf.write("\u0217\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\30")
        buf.write("\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3")
        buf.write("\"\3\"\3#\3#\3$\3$\3$\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3")
        buf.write("(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3")
        buf.write("\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\7\64")
        buf.write("\u0153\n\64\f\64\16\64\u0156\13\64\3\65\3\65\3\66\3\66")
        buf.write("\5\66\u015c\n\66\3\66\6\66\u015f\n\66\r\66\16\66\u0160")
        buf.write("\3\67\6\67\u0164\n\67\r\67\16\67\u0165\3\67\3\67\7\67")
        buf.write("\u016a\n\67\f\67\16\67\u016d\13\67\3\67\5\67\u0170\n\67")
        buf.write("\3\67\3\67\6\67\u0174\n\67\r\67\16\67\u0175\3\67\5\67")
        buf.write("\u0179\n\67\3\67\6\67\u017c\n\67\r\67\16\67\u017d\3\67")
        buf.write("\3\67\5\67\u0182\n\67\38\38\38\78\u0187\n8\f8\168\u018a")
        buf.write("\138\58\u018c\n8\39\39\39\39\59\u0192\n9\39\69\u0195\n")
        buf.write("9\r9\169\u0196\39\39\3:\3:\3:\3:\5:\u019f\n:\3:\6:\u01a2")
        buf.write("\n:\r:\16:\u01a3\3:\3:\3;\3;\3;\3;\5;\u01ac\n;\3;\6;\u01af")
        buf.write("\n;\r;\16;\u01b0\3;\3;\3<\3<\3<\3<\5<\u01b9\n<\3=\3=\3")
        buf.write("=\7=\u01be\n=\f=\16=\u01c1\13=\3=\3=\3=\3>\3>\5>\u01c8")
        buf.write("\n>\3?\3?\3@\6@\u01cd\n@\r@\16@\u01ce\3@\3@\3A\3A\3A\3")
        buf.write("A\7A\u01d7\nA\fA\16A\u01da\13A\3A\3A\3B\3B\3B\3B\3B\7")
        buf.write("B\u01e3\nB\fB\16B\u01e6\13B\3B\3B\3B\3B\3B\3C\3C\3C\3")
        buf.write("D\3D\3D\7D\u01f3\nD\fD\16D\u01f6\13D\3D\3D\3D\5D\u01fb")
        buf.write("\nD\3D\3D\3E\3E\3E\7E\u0202\nE\fE\16E\u0205\13E\3E\3E")
        buf.write("\3E\3E\5E\u020b\nE\3E\3E\3F\3F\3F\3G\3G\3G\3G\5G\u0216")
        buf.write("\nG\3\u01e4\2H\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13")
        buf.write("\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26")
        buf.write("+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#")
        buf.write("E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\2k")
        buf.write("\2m\66o\67q8s9u:w;y<{=}>\177?\u0081@\u0083A\u0085B\u0087")
        buf.write("C\u0089D\u008b\2\u008d\2\3\2\24\5\2C\\aac|\6\2\62;C\\")
        buf.write("aac|\3\2\62;\4\2GGgg\4\2--//\3\2\63;\3\2\62\63\3\2\62")
        buf.write("9\5\2\62;CHch\7\2\f\f\16\17$$))^^\5\2\13\f\16\17\"\"\4")
        buf.write("\2\f\f\17\17\3\3\f\f\b\2\f\f\17\17$$))^^dd\5\2\17\17)")
        buf.write(")^^\3\2))\3\2$$\b\2))^^ddppttvv\2\u0237\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3")
        buf.write("\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2")
        buf.write("\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2")
        buf.write("\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3")
        buf.write("\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2")
        buf.write("\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2m\3\2\2")
        buf.write("\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2")
        buf.write("\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2")
        buf.write("\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087")
        buf.write("\3\2\2\2\2\u0089\3\2\2\2\3\u008f\3\2\2\2\5\u0096\3\2\2")
        buf.write("\2\7\u0099\3\2\2\2\t\u009e\3\2\2\2\13\u00a2\3\2\2\2\r")
        buf.write("\u00a9\3\2\2\2\17\u00ae\3\2\2\2\21\u00b3\3\2\2\2\23\u00ba")
        buf.write("\3\2\2\2\25\u00c4\3\2\2\2\27\u00cb\3\2\2\2\31\u00cf\3")
        buf.write("\2\2\2\33\u00d5\3\2\2\2\35\u00dd\3\2\2\2\37\u00e3\3\2")
        buf.write("\2\2!\u00e7\3\2\2\2#\u00f0\3\2\2\2%\u00f6\3\2\2\2\'\u00fc")
        buf.write("\3\2\2\2)\u0100\3\2\2\2+\u0105\3\2\2\2-\u010b\3\2\2\2")
        buf.write("/\u010d\3\2\2\2\61\u010f\3\2\2\2\63\u0111\3\2\2\2\65\u0113")
        buf.write("\3\2\2\2\67\u0115\3\2\2\29\u0118\3\2\2\2;\u011b\3\2\2")
        buf.write("\2=\u011d\3\2\2\2?\u011f\3\2\2\2A\u0122\3\2\2\2C\u0125")
        buf.write("\3\2\2\2E\u0128\3\2\2\2G\u012a\3\2\2\2I\u012d\3\2\2\2")
        buf.write("K\u012f\3\2\2\2M\u0132\3\2\2\2O\u0135\3\2\2\2Q\u0138\3")
        buf.write("\2\2\2S\u013b\3\2\2\2U\u013e\3\2\2\2W\u0140\3\2\2\2Y\u0142")
        buf.write("\3\2\2\2[\u0144\3\2\2\2]\u0146\3\2\2\2_\u0148\3\2\2\2")
        buf.write("a\u014a\3\2\2\2c\u014c\3\2\2\2e\u014e\3\2\2\2g\u0150\3")
        buf.write("\2\2\2i\u0157\3\2\2\2k\u0159\3\2\2\2m\u0181\3\2\2\2o\u018b")
        buf.write("\3\2\2\2q\u0191\3\2\2\2s\u019e\3\2\2\2u\u01ab\3\2\2\2")
        buf.write("w\u01b8\3\2\2\2y\u01ba\3\2\2\2{\u01c7\3\2\2\2}\u01c9\3")
        buf.write("\2\2\2\177\u01cc\3\2\2\2\u0081\u01d2\3\2\2\2\u0083\u01dd")
        buf.write("\3\2\2\2\u0085\u01ec\3\2\2\2\u0087\u01ef\3\2\2\2\u0089")
        buf.write("\u01fe\3\2\2\2\u008b\u020e\3\2\2\2\u008d\u0215\3\2\2\2")
        buf.write("\u008f\u0090\7x\2\2\u0090\u0091\7q\2\2\u0091\u0092\7v")
        buf.write("\2\2\u0092\u0093\7k\2\2\u0093\u0094\7g\2\2\u0094\u0095")
        buf.write("\7p\2\2\u0095\4\3\2\2\2\u0096\u0097\7k\2\2\u0097\u0098")
        buf.write("\7h\2\2\u0098\6\3\2\2\2\u0099\u009a\7g\2\2\u009a\u009b")
        buf.write("\7n\2\2\u009b\u009c\7u\2\2\u009c\u009d\7g\2\2\u009d\b")
        buf.write("\3\2\2\2\u009e\u009f\7h\2\2\u009f\u00a0\7q\2\2\u00a0\u00a1")
        buf.write("\7t\2\2\u00a1\n\3\2\2\2\u00a2\u00a3\7t\2\2\u00a3\u00a4")
        buf.write("\7g\2\2\u00a4\u00a5\7v\2\2\u00a5\u00a6\7w\2\2\u00a6\u00a7")
        buf.write("\7t\2\2\u00a7\u00a8\7p\2\2\u00a8\f\3\2\2\2\u00a9\u00aa")
        buf.write("\7h\2\2\u00aa\u00ab\7w\2\2\u00ab\u00ac\7p\2\2\u00ac\u00ad")
        buf.write("\7e\2\2\u00ad\16\3\2\2\2\u00ae\u00af\7v\2\2\u00af\u00b0")
        buf.write("\7{\2\2\u00b0\u00b1\7r\2\2\u00b1\u00b2\7g\2\2\u00b2\20")
        buf.write("\3\2\2\2\u00b3\u00b4\7u\2\2\u00b4\u00b5\7v\2\2\u00b5\u00b6")
        buf.write("\7t\2\2\u00b6\u00b7\7w\2\2\u00b7\u00b8\7e\2\2\u00b8\u00b9")
        buf.write("\7v\2\2\u00b9\22\3\2\2\2\u00ba\u00bb\7k\2\2\u00bb\u00bc")
        buf.write("\7p\2\2\u00bc\u00bd\7v\2\2\u00bd\u00be\7g\2\2\u00be\u00bf")
        buf.write("\7t\2\2\u00bf\u00c0\7h\2\2\u00c0\u00c1\7c\2\2\u00c1\u00c2")
        buf.write("\7e\2\2\u00c2\u00c3\7g\2\2\u00c3\24\3\2\2\2\u00c4\u00c5")
        buf.write("\7u\2\2\u00c5\u00c6\7v\2\2\u00c6\u00c7\7t\2\2\u00c7\u00c8")
        buf.write("\7k\2\2\u00c8\u00c9\7p\2\2\u00c9\u00ca\7i\2\2\u00ca\26")
        buf.write("\3\2\2\2\u00cb\u00cc\7k\2\2\u00cc\u00cd\7p\2\2\u00cd\u00ce")
        buf.write("\7v\2\2\u00ce\30\3\2\2\2\u00cf\u00d0\7h\2\2\u00d0\u00d1")
        buf.write("\7n\2\2\u00d1\u00d2\7q\2\2\u00d2\u00d3\7c\2\2\u00d3\u00d4")
        buf.write("\7v\2\2\u00d4\32\3\2\2\2\u00d5\u00d6\7d\2\2\u00d6\u00d7")
        buf.write("\7q\2\2\u00d7\u00d8\7q\2\2\u00d8\u00d9\7n\2\2\u00d9\u00da")
        buf.write("\7g\2\2\u00da\u00db\7c\2\2\u00db\u00dc\7p\2\2\u00dc\34")
        buf.write("\3\2\2\2\u00dd\u00de\7e\2\2\u00de\u00df\7q\2\2\u00df\u00e0")
        buf.write("\7p\2\2\u00e0\u00e1\7u\2\2\u00e1\u00e2\7v\2\2\u00e2\36")
        buf.write("\3\2\2\2\u00e3\u00e4\7x\2\2\u00e4\u00e5\7c\2\2\u00e5\u00e6")
        buf.write("\7t\2\2\u00e6 \3\2\2\2\u00e7\u00e8\7e\2\2\u00e8\u00e9")
        buf.write("\7q\2\2\u00e9\u00ea\7p\2\2\u00ea\u00eb\7v\2\2\u00eb\u00ec")
        buf.write("\7k\2\2\u00ec\u00ed\7p\2\2\u00ed\u00ee\7w\2\2\u00ee\u00ef")
        buf.write("\7g\2\2\u00ef\"\3\2\2\2\u00f0\u00f1\7d\2\2\u00f1\u00f2")
        buf.write("\7t\2\2\u00f2\u00f3\7g\2\2\u00f3\u00f4\7c\2\2\u00f4\u00f5")
        buf.write("\7m\2\2\u00f5$\3\2\2\2\u00f6\u00f7\7t\2\2\u00f7\u00f8")
        buf.write("\7c\2\2\u00f8\u00f9\7p\2\2\u00f9\u00fa\7i\2\2\u00fa\u00fb")
        buf.write("\7g\2\2\u00fb&\3\2\2\2\u00fc\u00fd\7p\2\2\u00fd\u00fe")
        buf.write("\7k\2\2\u00fe\u00ff\7n\2\2\u00ff(\3\2\2\2\u0100\u0101")
        buf.write("\7v\2\2\u0101\u0102\7t\2\2\u0102\u0103\7w\2\2\u0103\u0104")
        buf.write("\7g\2\2\u0104*\3\2\2\2\u0105\u0106\7h\2\2\u0106\u0107")
        buf.write("\7c\2\2\u0107\u0108\7n\2\2\u0108\u0109\7u\2\2\u0109\u010a")
        buf.write("\7g\2\2\u010a,\3\2\2\2\u010b\u010c\7-\2\2\u010c.\3\2\2")
        buf.write("\2\u010d\u010e\7/\2\2\u010e\60\3\2\2\2\u010f\u0110\7,")
        buf.write("\2\2\u0110\62\3\2\2\2\u0111\u0112\7\61\2\2\u0112\64\3")
        buf.write("\2\2\2\u0113\u0114\7\'\2\2\u0114\66\3\2\2\2\u0115\u0116")
        buf.write("\7?\2\2\u0116\u0117\7?\2\2\u01178\3\2\2\2\u0118\u0119")
        buf.write("\7#\2\2\u0119\u011a\7?\2\2\u011a:\3\2\2\2\u011b\u011c")
        buf.write("\7>\2\2\u011c<\3\2\2\2\u011d\u011e\7@\2\2\u011e>\3\2\2")
        buf.write("\2\u011f\u0120\7>\2\2\u0120\u0121\7?\2\2\u0121@\3\2\2")
        buf.write("\2\u0122\u0123\7@\2\2\u0123\u0124\7?\2\2\u0124B\3\2\2")
        buf.write("\2\u0125\u0126\7~\2\2\u0126\u0127\7~\2\2\u0127D\3\2\2")
        buf.write("\2\u0128\u0129\7#\2\2\u0129F\3\2\2\2\u012a\u012b\7(\2")
        buf.write("\2\u012b\u012c\7(\2\2\u012cH\3\2\2\2\u012d\u012e\7?\2")
        buf.write("\2\u012eJ\3\2\2\2\u012f\u0130\7-\2\2\u0130\u0131\7?\2")
        buf.write("\2\u0131L\3\2\2\2\u0132\u0133\7/\2\2\u0133\u0134\7?\2")
        buf.write("\2\u0134N\3\2\2\2\u0135\u0136\7,\2\2\u0136\u0137\7?\2")
        buf.write("\2\u0137P\3\2\2\2\u0138\u0139\7\61\2\2\u0139\u013a\7?")
        buf.write("\2\2\u013aR\3\2\2\2\u013b\u013c\7\'\2\2\u013c\u013d\7")
        buf.write("?\2\2\u013dT\3\2\2\2\u013e\u013f\7\60\2\2\u013fV\3\2\2")
        buf.write("\2\u0140\u0141\7*\2\2\u0141X\3\2\2\2\u0142\u0143\7+\2")
        buf.write("\2\u0143Z\3\2\2\2\u0144\u0145\7}\2\2\u0145\\\3\2\2\2\u0146")
        buf.write("\u0147\7\177\2\2\u0147^\3\2\2\2\u0148\u0149\7]\2\2\u0149")
        buf.write("`\3\2\2\2\u014a\u014b\7_\2\2\u014bb\3\2\2\2\u014c\u014d")
        buf.write("\7=\2\2\u014dd\3\2\2\2\u014e\u014f\7.\2\2\u014ff\3\2\2")
        buf.write("\2\u0150\u0154\t\2\2\2\u0151\u0153\t\3\2\2\u0152\u0151")
        buf.write("\3\2\2\2\u0153\u0156\3\2\2\2\u0154\u0152\3\2\2\2\u0154")
        buf.write("\u0155\3\2\2\2\u0155h\3\2\2\2\u0156\u0154\3\2\2\2\u0157")
        buf.write("\u0158\t\4\2\2\u0158j\3\2\2\2\u0159\u015b\t\5\2\2\u015a")
        buf.write("\u015c\t\6\2\2\u015b\u015a\3\2\2\2\u015b\u015c\3\2\2\2")
        buf.write("\u015c\u015e\3\2\2\2\u015d\u015f\5i\65\2\u015e\u015d\3")
        buf.write("\2\2\2\u015f\u0160\3\2\2\2\u0160\u015e\3\2\2\2\u0160\u0161")
        buf.write("\3\2\2\2\u0161l\3\2\2\2\u0162\u0164\5i\65\2\u0163\u0162")
        buf.write("\3\2\2\2\u0164\u0165\3\2\2\2\u0165\u0163\3\2\2\2\u0165")
        buf.write("\u0166\3\2\2\2\u0166\u0167\3\2\2\2\u0167\u016b\7\60\2")
        buf.write("\2\u0168\u016a\5i\65\2\u0169\u0168\3\2\2\2\u016a\u016d")
        buf.write("\3\2\2\2\u016b\u0169\3\2\2\2\u016b\u016c\3\2\2\2\u016c")
        buf.write("\u016f\3\2\2\2\u016d\u016b\3\2\2\2\u016e\u0170\5k\66\2")
        buf.write("\u016f\u016e\3\2\2\2\u016f\u0170\3\2\2\2\u0170\u0182\3")
        buf.write("\2\2\2\u0171\u0173\7\60\2\2\u0172\u0174\5i\65\2\u0173")
        buf.write("\u0172\3\2\2\2\u0174\u0175\3\2\2\2\u0175\u0173\3\2\2\2")
        buf.write("\u0175\u0176\3\2\2\2\u0176\u0178\3\2\2\2\u0177\u0179\5")
        buf.write("k\66\2\u0178\u0177\3\2\2\2\u0178\u0179\3\2\2\2\u0179\u0182")
        buf.write("\3\2\2\2\u017a\u017c\5i\65\2\u017b\u017a\3\2\2\2\u017c")
        buf.write("\u017d\3\2\2\2\u017d\u017b\3\2\2\2\u017d\u017e\3\2\2\2")
        buf.write("\u017e\u017f\3\2\2\2\u017f\u0180\5k\66\2\u0180\u0182\3")
        buf.write("\2\2\2\u0181\u0163\3\2\2\2\u0181\u0171\3\2\2\2\u0181\u017b")
        buf.write("\3\2\2\2\u0182n\3\2\2\2\u0183\u018c\7\62\2\2\u0184\u0188")
        buf.write("\t\7\2\2\u0185\u0187\5i\65\2\u0186\u0185\3\2\2\2\u0187")
        buf.write("\u018a\3\2\2\2\u0188\u0186\3\2\2\2\u0188\u0189\3\2\2\2")
        buf.write("\u0189\u018c\3\2\2\2\u018a\u0188\3\2\2\2\u018b\u0183\3")
        buf.write("\2\2\2\u018b\u0184\3\2\2\2\u018cp\3\2\2\2\u018d\u018e")
        buf.write("\7\62\2\2\u018e\u0192\7d\2\2\u018f\u0190\7\62\2\2\u0190")
        buf.write("\u0192\7D\2\2\u0191\u018d\3\2\2\2\u0191\u018f\3\2\2\2")
        buf.write("\u0192\u0194\3\2\2\2\u0193\u0195\t\b\2\2\u0194\u0193\3")
        buf.write("\2\2\2\u0195\u0196\3\2\2\2\u0196\u0194\3\2\2\2\u0196\u0197")
        buf.write("\3\2\2\2\u0197\u0198\3\2\2\2\u0198\u0199\b9\2\2\u0199")
        buf.write("r\3\2\2\2\u019a\u019b\7\62\2\2\u019b\u019f\7q\2\2\u019c")
        buf.write("\u019d\7\62\2\2\u019d\u019f\7Q\2\2\u019e\u019a\3\2\2\2")
        buf.write("\u019e\u019c\3\2\2\2\u019f\u01a1\3\2\2\2\u01a0\u01a2\t")
        buf.write("\t\2\2\u01a1\u01a0\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3\u01a1")
        buf.write("\3\2\2\2\u01a3\u01a4\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5")
        buf.write("\u01a6\b:\3\2\u01a6t\3\2\2\2\u01a7\u01a8\7\62\2\2\u01a8")
        buf.write("\u01ac\7z\2\2\u01a9\u01aa\7\62\2\2\u01aa\u01ac\7Z\2\2")
        buf.write("\u01ab\u01a7\3\2\2\2\u01ab\u01a9\3\2\2\2\u01ac\u01ae\3")
        buf.write("\2\2\2\u01ad\u01af\t\n\2\2\u01ae\u01ad\3\2\2\2\u01af\u01b0")
        buf.write("\3\2\2\2\u01b0\u01ae\3\2\2\2\u01b0\u01b1\3\2\2\2\u01b1")
        buf.write("\u01b2\3\2\2\2\u01b2\u01b3\b;\4\2\u01b3v\3\2\2\2\u01b4")
        buf.write("\u01b9\5o8\2\u01b5\u01b9\5q9\2\u01b6\u01b9\5s:\2\u01b7")
        buf.write("\u01b9\5u;\2\u01b8\u01b4\3\2\2\2\u01b8\u01b5\3\2\2\2\u01b8")
        buf.write("\u01b6\3\2\2\2\u01b8\u01b7\3\2\2\2\u01b9x\3\2\2\2\u01ba")
        buf.write("\u01bf\7$\2\2\u01bb\u01be\5\u008dG\2\u01bc\u01be\n\13")
        buf.write("\2\2\u01bd\u01bb\3\2\2\2\u01bd\u01bc\3\2\2\2\u01be\u01c1")
        buf.write("\3\2\2\2\u01bf\u01bd\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0")
        buf.write("\u01c2\3\2\2\2\u01c1\u01bf\3\2\2\2\u01c2\u01c3\7$\2\2")
        buf.write("\u01c3\u01c4\b=\5\2\u01c4z\3\2\2\2\u01c5\u01c8\5)\25\2")
        buf.write("\u01c6\u01c8\5+\26\2\u01c7\u01c5\3\2\2\2\u01c7\u01c6\3")
        buf.write("\2\2\2\u01c8|\3\2\2\2\u01c9\u01ca\5\'\24\2\u01ca~\3\2")
        buf.write("\2\2\u01cb\u01cd\t\f\2\2\u01cc\u01cb\3\2\2\2\u01cd\u01ce")
        buf.write("\3\2\2\2\u01ce\u01cc\3\2\2\2\u01ce\u01cf\3\2\2\2\u01cf")
        buf.write("\u01d0\3\2\2\2\u01d0\u01d1\b@\6\2\u01d1\u0080\3\2\2\2")
        buf.write("\u01d2\u01d3\7\61\2\2\u01d3\u01d4\7\61\2\2\u01d4\u01d8")
        buf.write("\3\2\2\2\u01d5\u01d7\n\r\2\2\u01d6\u01d5\3\2\2\2\u01d7")
        buf.write("\u01da\3\2\2\2\u01d8\u01d6\3\2\2\2\u01d8\u01d9\3\2\2\2")
        buf.write("\u01d9\u01db\3\2\2\2\u01da\u01d8\3\2\2\2\u01db\u01dc\b")
        buf.write("A\6\2\u01dc\u0082\3\2\2\2\u01dd\u01de\7\61\2\2\u01de\u01df")
        buf.write("\7,\2\2\u01df\u01e4\3\2\2\2\u01e0\u01e3\5\u0083B\2\u01e1")
        buf.write("\u01e3\13\2\2\2\u01e2\u01e0\3\2\2\2\u01e2\u01e1\3\2\2")
        buf.write("\2\u01e3\u01e6\3\2\2\2\u01e4\u01e5\3\2\2\2\u01e4\u01e2")
        buf.write("\3\2\2\2\u01e5\u01e7\3\2\2\2\u01e6\u01e4\3\2\2\2\u01e7")
        buf.write("\u01e8\7,\2\2\u01e8\u01e9\7\61\2\2\u01e9\u01ea\3\2\2\2")
        buf.write("\u01ea\u01eb\bB\6\2\u01eb\u0084\3\2\2\2\u01ec\u01ed\13")
        buf.write("\2\2\2\u01ed\u01ee\bC\7\2\u01ee\u0086\3\2\2\2\u01ef\u01f4")
        buf.write("\7$\2\2\u01f0\u01f3\n\13\2\2\u01f1\u01f3\5\u008dG\2\u01f2")
        buf.write("\u01f0\3\2\2\2\u01f2\u01f1\3\2\2\2\u01f3\u01f6\3\2\2\2")
        buf.write("\u01f4\u01f2\3\2\2\2\u01f4\u01f5\3\2\2\2\u01f5\u01fa\3")
        buf.write("\2\2\2\u01f6\u01f4\3\2\2\2\u01f7\u01fb\t\16\2\2\u01f8")
        buf.write("\u01f9\7\17\2\2\u01f9\u01fb\7\f\2\2\u01fa\u01f7\3\2\2")
        buf.write("\2\u01fa\u01f8\3\2\2\2\u01fb\u01fc\3\2\2\2\u01fc\u01fd")
        buf.write("\bD\b\2\u01fd\u0088\3\2\2\2\u01fe\u0203\7$\2\2\u01ff\u0202")
        buf.write("\n\17\2\2\u0200\u0202\5\u008dG\2\u0201\u01ff\3\2\2\2\u0201")
        buf.write("\u0200\3\2\2\2\u0202\u0205\3\2\2\2\u0203\u0201\3\2\2\2")
        buf.write("\u0203\u0204\3\2\2\2\u0204\u020a\3\2\2\2\u0205\u0203\3")
        buf.write("\2\2\2\u0206\u020b\t\20\2\2\u0207\u020b\5\u008bF\2\u0208")
        buf.write("\u0209\t\21\2\2\u0209\u020b\n\22\2\2\u020a\u0206\3\2\2")
        buf.write("\2\u020a\u0207\3\2\2\2\u020a\u0208\3\2\2\2\u020b\u020c")
        buf.write("\3\2\2\2\u020c\u020d\bE\t\2\u020d\u008a\3\2\2\2\u020e")
        buf.write("\u020f\7^\2\2\u020f\u0210\n\23\2\2\u0210\u008c\3\2\2\2")
        buf.write("\u0211\u0212\7^\2\2\u0212\u0216\t\23\2\2\u0213\u0214\t")
        buf.write("\21\2\2\u0214\u0216\t\22\2\2\u0215\u0211\3\2\2\2\u0215")
        buf.write("\u0213\3\2\2\2\u0216\u008e\3\2\2\2$\2\u0154\u015b\u0160")
        buf.write("\u0165\u016b\u016f\u0175\u0178\u017d\u0181\u0188\u018b")
        buf.write("\u0191\u0196\u019e\u01a3\u01ab\u01b0\u01b8\u01bd\u01bf")
        buf.write("\u01c7\u01ce\u01d8\u01e2\u01e4\u01f2\u01f4\u01fa\u0201")
        buf.write("\u0203\u020a\u0215\n\39\2\3:\3\3;\4\3=\5\b\2\2\3C\6\3")
        buf.write("D\7\3E\b")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    IF = 2
    ELSE = 3
    FOR = 4
    RETURN = 5
    FUNC = 6
    TYPE = 7
    STRUCT = 8
    INTERFACE = 9
    STRING = 10
    INT = 11
    FLOAT = 12
    BOOLEAN = 13
    CONST = 14
    VAR = 15
    CONTINUE = 16
    BREAK = 17
    RANGE = 18
    NIL = 19
    TRUE = 20
    FALSE = 21
    ADD = 22
    MINUS = 23
    MULT = 24
    DIV = 25
    REM = 26
    EQUAL = 27
    DIFF = 28
    LT = 29
    GT = 30
    LE = 31
    GE = 32
    OR = 33
    FACT = 34
    AND = 35
    ASSIGN = 36
    ADD_ASSIGN = 37
    MINUS_ASSIGN = 38
    MULT_ASSIGN = 39
    DIV_ASSIGN = 40
    REM_ASSIGN = 41
    DOT = 42
    LPAREN = 43
    RPAREN = 44
    LBRACE = 45
    RBRACE = 46
    LBRACK = 47
    RBRACK = 48
    SEMI = 49
    COMMA = 50
    ID = 51
    FLOAT_LIT = 52
    DEC_LIT = 53
    BIN_LIT = 54
    OCT_LIT = 55
    HEX_LIT = 56
    INT_LIT = 57
    STR_LIT = 58
    BOOL_LIT = 59
    NIL_LIT = 60
    WS = 61
    LINE_COMMENT = 62
    BLOCK_COMMENT = 63
    ERROR_CHAR = 64
    UNCLOSE_STRING = 65
    ILLEGAL_ESCAPE = 66

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'votien'", "'if'", "'else'", "'for'", "'return'", "'func'", 
            "'type'", "'struct'", "'interface'", "'string'", "'int'", "'float'", 
            "'boolean'", "'const'", "'var'", "'continue'", "'break'", "'range'", 
            "'nil'", "'true'", "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", 
            "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'||'", "'!'", 
            "'&&'", "'='", "'+='", "'-='", "'*='", "'/='", "'%='", "'.'", 
            "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", "','" ]

    symbolicNames = [ "<INVALID>",
            "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", 
            "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", 
            "BREAK", "RANGE", "NIL", "TRUE", "FALSE", "ADD", "MINUS", "MULT", 
            "DIV", "REM", "EQUAL", "DIFF", "LT", "GT", "LE", "GE", "OR", 
            "FACT", "AND", "ASSIGN", "ADD_ASSIGN", "MINUS_ASSIGN", "MULT_ASSIGN", 
            "DIV_ASSIGN", "REM_ASSIGN", "DOT", "LPAREN", "RPAREN", "LBRACE", 
            "RBRACE", "LBRACK", "RBRACK", "SEMI", "COMMA", "ID", "FLOAT_LIT", 
            "DEC_LIT", "BIN_LIT", "OCT_LIT", "HEX_LIT", "INT_LIT", "STR_LIT", 
            "BOOL_LIT", "NIL_LIT", "WS", "LINE_COMMENT", "BLOCK_COMMENT", 
            "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", 
                  "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", 
                  "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", "NIL", "TRUE", 
                  "FALSE", "ADD", "MINUS", "MULT", "DIV", "REM", "EQUAL", 
                  "DIFF", "LT", "GT", "LE", "GE", "OR", "FACT", "AND", "ASSIGN", 
                  "ADD_ASSIGN", "MINUS_ASSIGN", "MULT_ASSIGN", "DIV_ASSIGN", 
                  "REM_ASSIGN", "DOT", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                  "LBRACK", "RBRACK", "SEMI", "COMMA", "ID", "DIGIT", "EXP", 
                  "FLOAT_LIT", "DEC_LIT", "BIN_LIT", "OCT_LIT", "HEX_LIT", 
                  "INT_LIT", "STR_LIT", "BOOL_LIT", "NIL_LIT", "WS", "LINE_COMMENT", 
                  "BLOCK_COMMENT", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "IllegalEscape", "ESCAPE_SEQ" ]

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
            actions[55] = self.BIN_LIT_action 
            actions[56] = self.OCT_LIT_action 
            actions[57] = self.HEX_LIT_action 
            actions[59] = self.STR_LIT_action 
            actions[65] = self.ERROR_CHAR_action 
            actions[66] = self.UNCLOSE_STRING_action 
            actions[67] = self.ILLEGAL_ESCAPE_action 
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

     


