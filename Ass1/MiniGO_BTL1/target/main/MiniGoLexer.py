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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2F")
        buf.write("\u0220\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\3\2\3\2\3\3\3\3")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\5\4\u009e\n\4\3\5\3\5\3\5\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3")
        buf.write("\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\32\3\32")
        buf.write("\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3 \3 \3 \3!\3!\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3%\3&")
        buf.write("\3&\3&\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3,")
        buf.write("\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62")
        buf.write("\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\7\66\u015c\n")
        buf.write("\66\f\66\16\66\u015f\13\66\3\67\3\67\38\38\58\u0165\n")
        buf.write("8\38\68\u0168\n8\r8\168\u0169\39\69\u016d\n9\r9\169\u016e")
        buf.write("\39\39\79\u0173\n9\f9\169\u0176\139\39\59\u0179\n9\39")
        buf.write("\39\69\u017d\n9\r9\169\u017e\39\59\u0182\n9\39\69\u0185")
        buf.write("\n9\r9\169\u0186\39\39\59\u018b\n9\3:\3:\3:\7:\u0190\n")
        buf.write(":\f:\16:\u0193\13:\5:\u0195\n:\3;\3;\3;\3;\5;\u019b\n")
        buf.write(";\3;\6;\u019e\n;\r;\16;\u019f\3;\3;\3<\3<\3<\3<\5<\u01a8")
        buf.write("\n<\3<\6<\u01ab\n<\r<\16<\u01ac\3<\3<\3=\3=\3=\3=\5=\u01b5")
        buf.write("\n=\3=\6=\u01b8\n=\r=\16=\u01b9\3=\3=\3>\3>\3>\3>\5>\u01c2")
        buf.write("\n>\3?\3?\3?\7?\u01c7\n?\f?\16?\u01ca\13?\3?\3?\3?\3@")
        buf.write("\3@\5@\u01d1\n@\3A\3A\3B\6B\u01d6\nB\rB\16B\u01d7\3B\3")
        buf.write("B\3C\3C\3C\3C\7C\u01e0\nC\fC\16C\u01e3\13C\3C\3C\3D\3")
        buf.write("D\3D\3D\3D\7D\u01ec\nD\fD\16D\u01ef\13D\3D\3D\3D\3D\3")
        buf.write("D\3E\3E\3E\3F\3F\3F\7F\u01fc\nF\fF\16F\u01ff\13F\3F\3")
        buf.write("F\3F\5F\u0204\nF\3F\3F\3G\3G\3G\7G\u020b\nG\fG\16G\u020e")
        buf.write("\13G\3G\3G\3G\3G\5G\u0214\nG\3G\3G\3H\3H\3H\3I\3I\3I\3")
        buf.write("I\5I\u021f\nI\3\u01ed\2J\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write("\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63")
        buf.write("e\64g\65i\66k\67m\2o\2q8s9u:w;y<{=}>\177?\u0081@\u0083")
        buf.write("A\u0085B\u0087C\u0089D\u008bE\u008dF\u008f\2\u0091\2\3")
        buf.write("\2\24\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\4\2GGgg\4\2--")
        buf.write("//\3\2\63;\3\2\62\63\3\2\629\5\2\62;CHch\7\2\f\f\16\17")
        buf.write("$$))^^\5\2\13\f\16\17\"\"\4\2\f\f\17\17\3\3\f\f\b\2\f")
        buf.write("\f\17\17$$))^^dd\5\2\17\17))^^\3\2))\3\2$$\b\2))^^ddp")
        buf.write("pttvv\2\u0245\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t")
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
        buf.write("\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2q\3\2\2\2\2")
        buf.write("s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2")
        buf.write("\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2")
        buf.write("\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2")
        buf.write("\u008b\3\2\2\2\2\u008d\3\2\2\2\3\u0093\3\2\2\2\5\u0095")
        buf.write("\3\2\2\2\7\u009d\3\2\2\2\t\u009f\3\2\2\2\13\u00a2\3\2")
        buf.write("\2\2\r\u00a7\3\2\2\2\17\u00ab\3\2\2\2\21\u00b2\3\2\2\2")
        buf.write("\23\u00b7\3\2\2\2\25\u00bc\3\2\2\2\27\u00c3\3\2\2\2\31")
        buf.write("\u00cd\3\2\2\2\33\u00d4\3\2\2\2\35\u00d8\3\2\2\2\37\u00de")
        buf.write("\3\2\2\2!\u00e6\3\2\2\2#\u00ec\3\2\2\2%\u00f0\3\2\2\2")
        buf.write("\'\u00f9\3\2\2\2)\u00ff\3\2\2\2+\u0105\3\2\2\2-\u0109")
        buf.write("\3\2\2\2/\u010e\3\2\2\2\61\u0114\3\2\2\2\63\u0116\3\2")
        buf.write("\2\2\65\u0118\3\2\2\2\67\u011a\3\2\2\29\u011c\3\2\2\2")
        buf.write(";\u011e\3\2\2\2=\u0120\3\2\2\2?\u0123\3\2\2\2A\u0126\3")
        buf.write("\2\2\2C\u0128\3\2\2\2E\u012a\3\2\2\2G\u012d\3\2\2\2I\u0130")
        buf.write("\3\2\2\2K\u0133\3\2\2\2M\u0136\3\2\2\2O\u0138\3\2\2\2")
        buf.write("Q\u013b\3\2\2\2S\u013e\3\2\2\2U\u0141\3\2\2\2W\u0144\3")
        buf.write("\2\2\2Y\u0147\3\2\2\2[\u0149\3\2\2\2]\u014b\3\2\2\2_\u014d")
        buf.write("\3\2\2\2a\u014f\3\2\2\2c\u0151\3\2\2\2e\u0153\3\2\2\2")
        buf.write("g\u0155\3\2\2\2i\u0157\3\2\2\2k\u0159\3\2\2\2m\u0160\3")
        buf.write("\2\2\2o\u0162\3\2\2\2q\u018a\3\2\2\2s\u0194\3\2\2\2u\u019a")
        buf.write("\3\2\2\2w\u01a7\3\2\2\2y\u01b4\3\2\2\2{\u01c1\3\2\2\2")
        buf.write("}\u01c3\3\2\2\2\177\u01d0\3\2\2\2\u0081\u01d2\3\2\2\2")
        buf.write("\u0083\u01d5\3\2\2\2\u0085\u01db\3\2\2\2\u0087\u01e6\3")
        buf.write("\2\2\2\u0089\u01f5\3\2\2\2\u008b\u01f8\3\2\2\2\u008d\u0207")
        buf.write("\3\2\2\2\u008f\u0217\3\2\2\2\u0091\u021e\3\2\2\2\u0093")
        buf.write("\u0094\7\17\2\2\u0094\4\3\2\2\2\u0095\u0096\7\f\2\2\u0096")
        buf.write("\6\3\2\2\2\u0097\u009e\5A!\2\u0098\u009e\5C\"\2\u0099")
        buf.write("\u009e\5E#\2\u009a\u009e\5G$\2\u009b\u009e\5=\37\2\u009c")
        buf.write("\u009e\5? \2\u009d\u0097\3\2\2\2\u009d\u0098\3\2\2\2\u009d")
        buf.write("\u0099\3\2\2\2\u009d\u009a\3\2\2\2\u009d\u009b\3\2\2\2")
        buf.write("\u009d\u009c\3\2\2\2\u009e\b\3\2\2\2\u009f\u00a0\7k\2")
        buf.write("\2\u00a0\u00a1\7h\2\2\u00a1\n\3\2\2\2\u00a2\u00a3\7g\2")
        buf.write("\2\u00a3\u00a4\7n\2\2\u00a4\u00a5\7u\2\2\u00a5\u00a6\7")
        buf.write("g\2\2\u00a6\f\3\2\2\2\u00a7\u00a8\7h\2\2\u00a8\u00a9\7")
        buf.write("q\2\2\u00a9\u00aa\7t\2\2\u00aa\16\3\2\2\2\u00ab\u00ac")
        buf.write("\7t\2\2\u00ac\u00ad\7g\2\2\u00ad\u00ae\7v\2\2\u00ae\u00af")
        buf.write("\7w\2\2\u00af\u00b0\7t\2\2\u00b0\u00b1\7p\2\2\u00b1\20")
        buf.write("\3\2\2\2\u00b2\u00b3\7h\2\2\u00b3\u00b4\7w\2\2\u00b4\u00b5")
        buf.write("\7p\2\2\u00b5\u00b6\7e\2\2\u00b6\22\3\2\2\2\u00b7\u00b8")
        buf.write("\7v\2\2\u00b8\u00b9\7{\2\2\u00b9\u00ba\7r\2\2\u00ba\u00bb")
        buf.write("\7g\2\2\u00bb\24\3\2\2\2\u00bc\u00bd\7u\2\2\u00bd\u00be")
        buf.write("\7v\2\2\u00be\u00bf\7t\2\2\u00bf\u00c0\7w\2\2\u00c0\u00c1")
        buf.write("\7e\2\2\u00c1\u00c2\7v\2\2\u00c2\26\3\2\2\2\u00c3\u00c4")
        buf.write("\7k\2\2\u00c4\u00c5\7p\2\2\u00c5\u00c6\7v\2\2\u00c6\u00c7")
        buf.write("\7g\2\2\u00c7\u00c8\7t\2\2\u00c8\u00c9\7h\2\2\u00c9\u00ca")
        buf.write("\7c\2\2\u00ca\u00cb\7e\2\2\u00cb\u00cc\7g\2\2\u00cc\30")
        buf.write("\3\2\2\2\u00cd\u00ce\7u\2\2\u00ce\u00cf\7v\2\2\u00cf\u00d0")
        buf.write("\7t\2\2\u00d0\u00d1\7k\2\2\u00d1\u00d2\7p\2\2\u00d2\u00d3")
        buf.write("\7i\2\2\u00d3\32\3\2\2\2\u00d4\u00d5\7k\2\2\u00d5\u00d6")
        buf.write("\7p\2\2\u00d6\u00d7\7v\2\2\u00d7\34\3\2\2\2\u00d8\u00d9")
        buf.write("\7h\2\2\u00d9\u00da\7n\2\2\u00da\u00db\7q\2\2\u00db\u00dc")
        buf.write("\7c\2\2\u00dc\u00dd\7v\2\2\u00dd\36\3\2\2\2\u00de\u00df")
        buf.write("\7d\2\2\u00df\u00e0\7q\2\2\u00e0\u00e1\7q\2\2\u00e1\u00e2")
        buf.write("\7n\2\2\u00e2\u00e3\7g\2\2\u00e3\u00e4\7c\2\2\u00e4\u00e5")
        buf.write("\7p\2\2\u00e5 \3\2\2\2\u00e6\u00e7\7e\2\2\u00e7\u00e8")
        buf.write("\7q\2\2\u00e8\u00e9\7p\2\2\u00e9\u00ea\7u\2\2\u00ea\u00eb")
        buf.write("\7v\2\2\u00eb\"\3\2\2\2\u00ec\u00ed\7x\2\2\u00ed\u00ee")
        buf.write("\7c\2\2\u00ee\u00ef\7t\2\2\u00ef$\3\2\2\2\u00f0\u00f1")
        buf.write("\7e\2\2\u00f1\u00f2\7q\2\2\u00f2\u00f3\7p\2\2\u00f3\u00f4")
        buf.write("\7v\2\2\u00f4\u00f5\7k\2\2\u00f5\u00f6\7p\2\2\u00f6\u00f7")
        buf.write("\7w\2\2\u00f7\u00f8\7g\2\2\u00f8&\3\2\2\2\u00f9\u00fa")
        buf.write("\7d\2\2\u00fa\u00fb\7t\2\2\u00fb\u00fc\7g\2\2\u00fc\u00fd")
        buf.write("\7c\2\2\u00fd\u00fe\7m\2\2\u00fe(\3\2\2\2\u00ff\u0100")
        buf.write("\7t\2\2\u0100\u0101\7c\2\2\u0101\u0102\7p\2\2\u0102\u0103")
        buf.write("\7i\2\2\u0103\u0104\7g\2\2\u0104*\3\2\2\2\u0105\u0106")
        buf.write("\7p\2\2\u0106\u0107\7k\2\2\u0107\u0108\7n\2\2\u0108,\3")
        buf.write("\2\2\2\u0109\u010a\7v\2\2\u010a\u010b\7t\2\2\u010b\u010c")
        buf.write("\7w\2\2\u010c\u010d\7g\2\2\u010d.\3\2\2\2\u010e\u010f")
        buf.write("\7h\2\2\u010f\u0110\7c\2\2\u0110\u0111\7n\2\2\u0111\u0112")
        buf.write("\7u\2\2\u0112\u0113\7g\2\2\u0113\60\3\2\2\2\u0114\u0115")
        buf.write("\7#\2\2\u0115\62\3\2\2\2\u0116\u0117\7-\2\2\u0117\64\3")
        buf.write("\2\2\2\u0118\u0119\7/\2\2\u0119\66\3\2\2\2\u011a\u011b")
        buf.write("\7,\2\2\u011b8\3\2\2\2\u011c\u011d\7\61\2\2\u011d:\3\2")
        buf.write("\2\2\u011e\u011f\7\'\2\2\u011f<\3\2\2\2\u0120\u0121\7")
        buf.write("?\2\2\u0121\u0122\7?\2\2\u0122>\3\2\2\2\u0123\u0124\7")
        buf.write("#\2\2\u0124\u0125\7?\2\2\u0125@\3\2\2\2\u0126\u0127\7")
        buf.write(">\2\2\u0127B\3\2\2\2\u0128\u0129\7@\2\2\u0129D\3\2\2\2")
        buf.write("\u012a\u012b\7>\2\2\u012b\u012c\7?\2\2\u012cF\3\2\2\2")
        buf.write("\u012d\u012e\7@\2\2\u012e\u012f\7?\2\2\u012fH\3\2\2\2")
        buf.write("\u0130\u0131\7~\2\2\u0131\u0132\7~\2\2\u0132J\3\2\2\2")
        buf.write("\u0133\u0134\7(\2\2\u0134\u0135\7(\2\2\u0135L\3\2\2\2")
        buf.write("\u0136\u0137\7?\2\2\u0137N\3\2\2\2\u0138\u0139\7-\2\2")
        buf.write("\u0139\u013a\7?\2\2\u013aP\3\2\2\2\u013b\u013c\7/\2\2")
        buf.write("\u013c\u013d\7?\2\2\u013dR\3\2\2\2\u013e\u013f\7,\2\2")
        buf.write("\u013f\u0140\7?\2\2\u0140T\3\2\2\2\u0141\u0142\7\61\2")
        buf.write("\2\u0142\u0143\7?\2\2\u0143V\3\2\2\2\u0144\u0145\7\'\2")
        buf.write("\2\u0145\u0146\7?\2\2\u0146X\3\2\2\2\u0147\u0148\7\60")
        buf.write("\2\2\u0148Z\3\2\2\2\u0149\u014a\7*\2\2\u014a\\\3\2\2\2")
        buf.write("\u014b\u014c\7+\2\2\u014c^\3\2\2\2\u014d\u014e\7}\2\2")
        buf.write("\u014e`\3\2\2\2\u014f\u0150\7\177\2\2\u0150b\3\2\2\2\u0151")
        buf.write("\u0152\7]\2\2\u0152d\3\2\2\2\u0153\u0154\7_\2\2\u0154")
        buf.write("f\3\2\2\2\u0155\u0156\7=\2\2\u0156h\3\2\2\2\u0157\u0158")
        buf.write("\7.\2\2\u0158j\3\2\2\2\u0159\u015d\t\2\2\2\u015a\u015c")
        buf.write("\t\3\2\2\u015b\u015a\3\2\2\2\u015c\u015f\3\2\2\2\u015d")
        buf.write("\u015b\3\2\2\2\u015d\u015e\3\2\2\2\u015el\3\2\2\2\u015f")
        buf.write("\u015d\3\2\2\2\u0160\u0161\t\4\2\2\u0161n\3\2\2\2\u0162")
        buf.write("\u0164\t\5\2\2\u0163\u0165\t\6\2\2\u0164\u0163\3\2\2\2")
        buf.write("\u0164\u0165\3\2\2\2\u0165\u0167\3\2\2\2\u0166\u0168\5")
        buf.write("m\67\2\u0167\u0166\3\2\2\2\u0168\u0169\3\2\2\2\u0169\u0167")
        buf.write("\3\2\2\2\u0169\u016a\3\2\2\2\u016ap\3\2\2\2\u016b\u016d")
        buf.write("\5m\67\2\u016c\u016b\3\2\2\2\u016d\u016e\3\2\2\2\u016e")
        buf.write("\u016c\3\2\2\2\u016e\u016f\3\2\2\2\u016f\u0170\3\2\2\2")
        buf.write("\u0170\u0174\7\60\2\2\u0171\u0173\5m\67\2\u0172\u0171")
        buf.write("\3\2\2\2\u0173\u0176\3\2\2\2\u0174\u0172\3\2\2\2\u0174")
        buf.write("\u0175\3\2\2\2\u0175\u0178\3\2\2\2\u0176\u0174\3\2\2\2")
        buf.write("\u0177\u0179\5o8\2\u0178\u0177\3\2\2\2\u0178\u0179\3\2")
        buf.write("\2\2\u0179\u018b\3\2\2\2\u017a\u017c\7\60\2\2\u017b\u017d")
        buf.write("\5m\67\2\u017c\u017b\3\2\2\2\u017d\u017e\3\2\2\2\u017e")
        buf.write("\u017c\3\2\2\2\u017e\u017f\3\2\2\2\u017f\u0181\3\2\2\2")
        buf.write("\u0180\u0182\5o8\2\u0181\u0180\3\2\2\2\u0181\u0182\3\2")
        buf.write("\2\2\u0182\u018b\3\2\2\2\u0183\u0185\5m\67\2\u0184\u0183")
        buf.write("\3\2\2\2\u0185\u0186\3\2\2\2\u0186\u0184\3\2\2\2\u0186")
        buf.write("\u0187\3\2\2\2\u0187\u0188\3\2\2\2\u0188\u0189\5o8\2\u0189")
        buf.write("\u018b\3\2\2\2\u018a\u016c\3\2\2\2\u018a\u017a\3\2\2\2")
        buf.write("\u018a\u0184\3\2\2\2\u018br\3\2\2\2\u018c\u0195\7\62\2")
        buf.write("\2\u018d\u0191\t\7\2\2\u018e\u0190\5m\67\2\u018f\u018e")
        buf.write("\3\2\2\2\u0190\u0193\3\2\2\2\u0191\u018f\3\2\2\2\u0191")
        buf.write("\u0192\3\2\2\2\u0192\u0195\3\2\2\2\u0193\u0191\3\2\2\2")
        buf.write("\u0194\u018c\3\2\2\2\u0194\u018d\3\2\2\2\u0195t\3\2\2")
        buf.write("\2\u0196\u0197\7\62\2\2\u0197\u019b\7d\2\2\u0198\u0199")
        buf.write("\7\62\2\2\u0199\u019b\7D\2\2\u019a\u0196\3\2\2\2\u019a")
        buf.write("\u0198\3\2\2\2\u019b\u019d\3\2\2\2\u019c\u019e\t\b\2\2")
        buf.write("\u019d\u019c\3\2\2\2\u019e\u019f\3\2\2\2\u019f\u019d\3")
        buf.write("\2\2\2\u019f\u01a0\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1\u01a2")
        buf.write("\b;\2\2\u01a2v\3\2\2\2\u01a3\u01a4\7\62\2\2\u01a4\u01a8")
        buf.write("\7q\2\2\u01a5\u01a6\7\62\2\2\u01a6\u01a8\7Q\2\2\u01a7")
        buf.write("\u01a3\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a8\u01aa\3\2\2\2")
        buf.write("\u01a9\u01ab\t\t\2\2\u01aa\u01a9\3\2\2\2\u01ab\u01ac\3")
        buf.write("\2\2\2\u01ac\u01aa\3\2\2\2\u01ac\u01ad\3\2\2\2\u01ad\u01ae")
        buf.write("\3\2\2\2\u01ae\u01af\b<\3\2\u01afx\3\2\2\2\u01b0\u01b1")
        buf.write("\7\62\2\2\u01b1\u01b5\7z\2\2\u01b2\u01b3\7\62\2\2\u01b3")
        buf.write("\u01b5\7Z\2\2\u01b4\u01b0\3\2\2\2\u01b4\u01b2\3\2\2\2")
        buf.write("\u01b5\u01b7\3\2\2\2\u01b6\u01b8\t\n\2\2\u01b7\u01b6\3")
        buf.write("\2\2\2\u01b8\u01b9\3\2\2\2\u01b9\u01b7\3\2\2\2\u01b9\u01ba")
        buf.write("\3\2\2\2\u01ba\u01bb\3\2\2\2\u01bb\u01bc\b=\4\2\u01bc")
        buf.write("z\3\2\2\2\u01bd\u01c2\5s:\2\u01be\u01c2\5u;\2\u01bf\u01c2")
        buf.write("\5w<\2\u01c0\u01c2\5y=\2\u01c1\u01bd\3\2\2\2\u01c1\u01be")
        buf.write("\3\2\2\2\u01c1\u01bf\3\2\2\2\u01c1\u01c0\3\2\2\2\u01c2")
        buf.write("|\3\2\2\2\u01c3\u01c8\7$\2\2\u01c4\u01c7\5\u0091I\2\u01c5")
        buf.write("\u01c7\n\13\2\2\u01c6\u01c4\3\2\2\2\u01c6\u01c5\3\2\2")
        buf.write("\2\u01c7\u01ca\3\2\2\2\u01c8\u01c6\3\2\2\2\u01c8\u01c9")
        buf.write("\3\2\2\2\u01c9\u01cb\3\2\2\2\u01ca\u01c8\3\2\2\2\u01cb")
        buf.write("\u01cc\7$\2\2\u01cc\u01cd\b?\5\2\u01cd~\3\2\2\2\u01ce")
        buf.write("\u01d1\5-\27\2\u01cf\u01d1\5/\30\2\u01d0\u01ce\3\2\2\2")
        buf.write("\u01d0\u01cf\3\2\2\2\u01d1\u0080\3\2\2\2\u01d2\u01d3\5")
        buf.write("+\26\2\u01d3\u0082\3\2\2\2\u01d4\u01d6\t\f\2\2\u01d5\u01d4")
        buf.write("\3\2\2\2\u01d6\u01d7\3\2\2\2\u01d7\u01d5\3\2\2\2\u01d7")
        buf.write("\u01d8\3\2\2\2\u01d8\u01d9\3\2\2\2\u01d9\u01da\bB\6\2")
        buf.write("\u01da\u0084\3\2\2\2\u01db\u01dc\7\61\2\2\u01dc\u01dd")
        buf.write("\7\61\2\2\u01dd\u01e1\3\2\2\2\u01de\u01e0\n\r\2\2\u01df")
        buf.write("\u01de\3\2\2\2\u01e0\u01e3\3\2\2\2\u01e1\u01df\3\2\2\2")
        buf.write("\u01e1\u01e2\3\2\2\2\u01e2\u01e4\3\2\2\2\u01e3\u01e1\3")
        buf.write("\2\2\2\u01e4\u01e5\bC\6\2\u01e5\u0086\3\2\2\2\u01e6\u01e7")
        buf.write("\7\61\2\2\u01e7\u01e8\7,\2\2\u01e8\u01ed\3\2\2\2\u01e9")
        buf.write("\u01ec\5\u0087D\2\u01ea\u01ec\13\2\2\2\u01eb\u01e9\3\2")
        buf.write("\2\2\u01eb\u01ea\3\2\2\2\u01ec\u01ef\3\2\2\2\u01ed\u01ee")
        buf.write("\3\2\2\2\u01ed\u01eb\3\2\2\2\u01ee\u01f0\3\2\2\2\u01ef")
        buf.write("\u01ed\3\2\2\2\u01f0\u01f1\7,\2\2\u01f1\u01f2\7\61\2\2")
        buf.write("\u01f2\u01f3\3\2\2\2\u01f3\u01f4\bD\6\2\u01f4\u0088\3")
        buf.write("\2\2\2\u01f5\u01f6\13\2\2\2\u01f6\u01f7\bE\7\2\u01f7\u008a")
        buf.write("\3\2\2\2\u01f8\u01fd\7$\2\2\u01f9\u01fc\n\13\2\2\u01fa")
        buf.write("\u01fc\5\u0091I\2\u01fb\u01f9\3\2\2\2\u01fb\u01fa\3\2")
        buf.write("\2\2\u01fc\u01ff\3\2\2\2\u01fd\u01fb\3\2\2\2\u01fd\u01fe")
        buf.write("\3\2\2\2\u01fe\u0203\3\2\2\2\u01ff\u01fd\3\2\2\2\u0200")
        buf.write("\u0204\t\16\2\2\u0201\u0202\7\17\2\2\u0202\u0204\7\f\2")
        buf.write("\2\u0203\u0200\3\2\2\2\u0203\u0201\3\2\2\2\u0204\u0205")
        buf.write("\3\2\2\2\u0205\u0206\bF\b\2\u0206\u008c\3\2\2\2\u0207")
        buf.write("\u020c\7$\2\2\u0208\u020b\n\17\2\2\u0209\u020b\5\u0091")
        buf.write("I\2\u020a\u0208\3\2\2\2\u020a\u0209\3\2\2\2\u020b\u020e")
        buf.write("\3\2\2\2\u020c\u020a\3\2\2\2\u020c\u020d\3\2\2\2\u020d")
        buf.write("\u0213\3\2\2\2\u020e\u020c\3\2\2\2\u020f\u0214\t\20\2")
        buf.write("\2\u0210\u0214\5\u008fH\2\u0211\u0212\t\21\2\2\u0212\u0214")
        buf.write("\n\22\2\2\u0213\u020f\3\2\2\2\u0213\u0210\3\2\2\2\u0213")
        buf.write("\u0211\3\2\2\2\u0214\u0215\3\2\2\2\u0215\u0216\bG\t\2")
        buf.write("\u0216\u008e\3\2\2\2\u0217\u0218\7^\2\2\u0218\u0219\n")
        buf.write("\23\2\2\u0219\u0090\3\2\2\2\u021a\u021b\7^\2\2\u021b\u021f")
        buf.write("\t\23\2\2\u021c\u021d\t\21\2\2\u021d\u021f\t\22\2\2\u021e")
        buf.write("\u021a\3\2\2\2\u021e\u021c\3\2\2\2\u021f\u0092\3\2\2\2")
        buf.write("%\2\u009d\u015d\u0164\u0169\u016e\u0174\u0178\u017e\u0181")
        buf.write("\u0186\u018a\u0191\u0194\u019a\u019f\u01a7\u01ac\u01b4")
        buf.write("\u01b9\u01c1\u01c6\u01c8\u01d0\u01d7\u01e1\u01eb\u01ed")
        buf.write("\u01fb\u01fd\u0203\u020a\u020c\u0213\u021e\n\3;\2\3<\3")
        buf.write("\3=\4\3?\5\b\2\2\3E\6\3F\7\3G\b")
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
    LPAREN = 45
    RPAREN = 46
    LBRACE = 47
    RBRACE = 48
    LBRACK = 49
    RBRACK = 50
    SEMI = 51
    COMMA = 52
    ID = 53
    FLOAT_LIT = 54
    DEC_LIT = 55
    BIN_LIT = 56
    OCT_LIT = 57
    HEX_LIT = 58
    INT_LIT = 59
    STR_LIT = 60
    BOOL_LIT = 61
    NIL_LIT = 62
    WS = 63
    LINE_COMMENT = 64
    BLOCK_COMMENT = 65
    ERROR_CHAR = 66
    UNCLOSE_STRING = 67
    ILLEGAL_ESCAPE = 68

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'\r'", "'\n'", "'if'", "'else'", "'for'", "'return'", "'func'", 
            "'type'", "'struct'", "'interface'", "'string'", "'int'", "'float'", 
            "'boolean'", "'const'", "'var'", "'continue'", "'break'", "'range'", 
            "'nil'", "'true'", "'false'", "'!'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'||'", 
            "'&&'", "'='", "'+='", "'-='", "'*='", "'/='", "'%='", "'.'", 
            "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", "','" ]

    symbolicNames = [ "<INVALID>",
            "REL", "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", 
            "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", 
            "CONTINUE", "BREAK", "RANGE", "NIL", "TRUE", "FALSE", "NOT", 
            "ADD", "MINUS", "MUL", "DIV", "MOD", "EQUAL", "DIFF", "LT", 
            "GT", "LE", "GE", "OR", "AND", "ASSIGN", "ADD_ASSIGN", "MINUS_ASSIGN", 
            "MULT_ASSIGN", "DIV_ASSIGN", "REM_ASSIGN", "DOT", "LPAREN", 
            "RPAREN", "LBRACE", "RBRACE", "LBRACK", "RBRACK", "SEMI", "COMMA", 
            "ID", "FLOAT_LIT", "DEC_LIT", "BIN_LIT", "OCT_LIT", "HEX_LIT", 
            "INT_LIT", "STR_LIT", "BOOL_LIT", "NIL_LIT", "WS", "LINE_COMMENT", 
            "BLOCK_COMMENT", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "T__1", "REL", "IF", "ELSE", "FOR", "RETURN", 
                  "FUNC", "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", 
                  "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", "BREAK", 
                  "RANGE", "NIL", "TRUE", "FALSE", "NOT", "ADD", "MINUS", 
                  "MUL", "DIV", "MOD", "EQUAL", "DIFF", "LT", "GT", "LE", 
                  "GE", "OR", "AND", "ASSIGN", "ADD_ASSIGN", "MINUS_ASSIGN", 
                  "MULT_ASSIGN", "DIV_ASSIGN", "REM_ASSIGN", "DOT", "LPAREN", 
                  "RPAREN", "LBRACE", "RBRACE", "LBRACK", "RBRACK", "SEMI", 
                  "COMMA", "ID", "DIGIT", "EXP", "FLOAT_LIT", "DEC_LIT", 
                  "BIN_LIT", "OCT_LIT", "HEX_LIT", "INT_LIT", "STR_LIT", 
                  "BOOL_LIT", "NIL_LIT", "WS", "LINE_COMMENT", "BLOCK_COMMENT", 
                  "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "IllegalEscape", 
                  "ESCAPE_SEQ" ]

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
            actions[57] = self.BIN_LIT_action 
            actions[58] = self.OCT_LIT_action 
            actions[59] = self.HEX_LIT_action 
            actions[61] = self.STR_LIT_action 
            actions[67] = self.ERROR_CHAR_action 
            actions[68] = self.UNCLOSE_STRING_action 
            actions[69] = self.ILLEGAL_ESCAPE_action 
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

     


