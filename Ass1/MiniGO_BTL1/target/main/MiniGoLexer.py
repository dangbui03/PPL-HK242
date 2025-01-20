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
        buf.write("\u0206\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\3\2\3\2\3\2\3\3")
        buf.write("\3\3\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\5\5\u00a1\n\5\3\6")
        buf.write("\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\32")
        buf.write("\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37")
        buf.write("\3 \3 \3 \3!\3!\3!\3\"\3\"\3#\3#\3$\3$\3$\3%\3%\3%\3&")
        buf.write("\3&\3&\3\'\3\'\3\'\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3")
        buf.write(",\3,\3,\3-\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62")
        buf.write("\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67")
        buf.write("\38\38\78\u0161\n8\f8\168\u0164\138\39\39\3:\3:\5:\u016a")
        buf.write("\n:\3:\3:\3;\3;\3;\7;\u0171\n;\f;\16;\u0174\13;\5;\u0176")
        buf.write("\n;\3<\3<\3<\3<\5<\u017c\n<\3<\6<\u017f\n<\r<\16<\u0180")
        buf.write("\3<\3<\3=\3=\3=\3=\5=\u0189\n=\3=\6=\u018c\n=\r=\16=\u018d")
        buf.write("\3=\3=\3>\3>\3>\3>\5>\u0196\n>\3>\6>\u0199\n>\r>\16>\u019a")
        buf.write("\3>\3>\3?\3?\3?\7?\u01a2\n?\f?\16?\u01a5\13?\5?\u01a7")
        buf.write("\n?\3?\5?\u01aa\n?\3@\3@\3@\7@\u01af\n@\f@\16@\u01b2\13")
        buf.write("@\3@\3@\3@\3A\3A\5A\u01b9\nA\3B\6B\u01bc\nB\rB\16B\u01bd")
        buf.write("\3B\3B\3C\3C\3C\3C\7C\u01c6\nC\fC\16C\u01c9\13C\3C\3C")
        buf.write("\3D\3D\3D\3D\3D\7D\u01d2\nD\fD\16D\u01d5\13D\3D\3D\3D")
        buf.write("\3D\3D\3E\3E\3E\3F\3F\3F\7F\u01e2\nF\fF\16F\u01e5\13F")
        buf.write("\3F\3F\3F\5F\u01ea\nF\3F\3F\3G\3G\3G\7G\u01f1\nG\fG\16")
        buf.write("G\u01f4\13G\3G\3G\3G\3G\5G\u01fa\nG\3G\3G\3H\3H\3H\3I")
        buf.write("\3I\3I\3I\5I\u0205\nI\3\u01d3\2J\3\3\5\4\7\5\t\6\13\7")
        buf.write("\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21")
        buf.write("!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67")
        buf.write("\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61")
        buf.write("a\62c\63e\64g\65i\66k\67m8o9q\2s\2u:w;y<{=}>\177?\u0081")
        buf.write("@\u0083A\u0085B\u0087C\u0089D\u008bE\u008dF\u008f\2\u0091")
        buf.write("\2\3\2\24\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\4\2GGgg\4")
        buf.write("\2--//\3\2\63;\3\2\62\63\3\2\629\5\2\62;CHch\7\2\f\f\16")
        buf.write("\17$$))^^\5\2\n\13\16\17\"\"\4\2\f\f\17\17\3\3\f\f\b\2")
        buf.write("\f\f\17\17$$))^^dd\5\2\17\17))^^\3\2))\3\2$$\b\2))^^d")
        buf.write("dppttvv\2\u0222\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q")
        buf.write("\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2")
        buf.write("[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2")
        buf.write("\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2")
        buf.write("\2\2o\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2")
        buf.write("\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083")
        buf.write("\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2")
        buf.write("\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\3\u0093\3\2\2\2\5\u0096")
        buf.write("\3\2\2\2\7\u0098\3\2\2\2\t\u00a0\3\2\2\2\13\u00a2\3\2")
        buf.write("\2\2\r\u00a5\3\2\2\2\17\u00aa\3\2\2\2\21\u00ae\3\2\2\2")
        buf.write("\23\u00b5\3\2\2\2\25\u00ba\3\2\2\2\27\u00bf\3\2\2\2\31")
        buf.write("\u00c6\3\2\2\2\33\u00d0\3\2\2\2\35\u00d7\3\2\2\2\37\u00db")
        buf.write("\3\2\2\2!\u00e1\3\2\2\2#\u00e9\3\2\2\2%\u00ef\3\2\2\2")
        buf.write("\'\u00f3\3\2\2\2)\u00fc\3\2\2\2+\u0102\3\2\2\2-\u0108")
        buf.write("\3\2\2\2/\u010c\3\2\2\2\61\u0111\3\2\2\2\63\u0117\3\2")
        buf.write("\2\2\65\u0119\3\2\2\2\67\u011b\3\2\2\29\u011d\3\2\2\2")
        buf.write(";\u011f\3\2\2\2=\u0121\3\2\2\2?\u0123\3\2\2\2A\u0126\3")
        buf.write("\2\2\2C\u0129\3\2\2\2E\u012b\3\2\2\2G\u012d\3\2\2\2I\u0130")
        buf.write("\3\2\2\2K\u0133\3\2\2\2M\u0136\3\2\2\2O\u0139\3\2\2\2")
        buf.write("Q\u013b\3\2\2\2S\u013e\3\2\2\2U\u0141\3\2\2\2W\u0144\3")
        buf.write("\2\2\2Y\u0147\3\2\2\2[\u014a\3\2\2\2]\u014c\3\2\2\2_\u014e")
        buf.write("\3\2\2\2a\u0150\3\2\2\2c\u0152\3\2\2\2e\u0154\3\2\2\2")
        buf.write("g\u0156\3\2\2\2i\u0158\3\2\2\2k\u015a\3\2\2\2m\u015c\3")
        buf.write("\2\2\2o\u015e\3\2\2\2q\u0165\3\2\2\2s\u0167\3\2\2\2u\u0175")
        buf.write("\3\2\2\2w\u017b\3\2\2\2y\u0188\3\2\2\2{\u0195\3\2\2\2")
        buf.write("}\u019e\3\2\2\2\177\u01ab\3\2\2\2\u0081\u01b8\3\2\2\2")
        buf.write("\u0083\u01bb\3\2\2\2\u0085\u01c1\3\2\2\2\u0087\u01cc\3")
        buf.write("\2\2\2\u0089\u01db\3\2\2\2\u008b\u01de\3\2\2\2\u008d\u01ed")
        buf.write("\3\2\2\2\u008f\u01fd\3\2\2\2\u0091\u0204\3\2\2\2\u0093")
        buf.write("\u0094\7<\2\2\u0094\u0095\7?\2\2\u0095\4\3\2\2\2\u0096")
        buf.write("\u0097\7\17\2\2\u0097\6\3\2\2\2\u0098\u0099\7\f\2\2\u0099")
        buf.write("\b\3\2\2\2\u009a\u00a1\5C\"\2\u009b\u00a1\5E#\2\u009c")
        buf.write("\u00a1\5G$\2\u009d\u00a1\5I%\2\u009e\u00a1\5? \2\u009f")
        buf.write("\u00a1\5A!\2\u00a0\u009a\3\2\2\2\u00a0\u009b\3\2\2\2\u00a0")
        buf.write("\u009c\3\2\2\2\u00a0\u009d\3\2\2\2\u00a0\u009e\3\2\2\2")
        buf.write("\u00a0\u009f\3\2\2\2\u00a1\n\3\2\2\2\u00a2\u00a3\7k\2")
        buf.write("\2\u00a3\u00a4\7h\2\2\u00a4\f\3\2\2\2\u00a5\u00a6\7g\2")
        buf.write("\2\u00a6\u00a7\7n\2\2\u00a7\u00a8\7u\2\2\u00a8\u00a9\7")
        buf.write("g\2\2\u00a9\16\3\2\2\2\u00aa\u00ab\7h\2\2\u00ab\u00ac")
        buf.write("\7q\2\2\u00ac\u00ad\7t\2\2\u00ad\20\3\2\2\2\u00ae\u00af")
        buf.write("\7t\2\2\u00af\u00b0\7g\2\2\u00b0\u00b1\7v\2\2\u00b1\u00b2")
        buf.write("\7w\2\2\u00b2\u00b3\7t\2\2\u00b3\u00b4\7p\2\2\u00b4\22")
        buf.write("\3\2\2\2\u00b5\u00b6\7h\2\2\u00b6\u00b7\7w\2\2\u00b7\u00b8")
        buf.write("\7p\2\2\u00b8\u00b9\7e\2\2\u00b9\24\3\2\2\2\u00ba\u00bb")
        buf.write("\7v\2\2\u00bb\u00bc\7{\2\2\u00bc\u00bd\7r\2\2\u00bd\u00be")
        buf.write("\7g\2\2\u00be\26\3\2\2\2\u00bf\u00c0\7u\2\2\u00c0\u00c1")
        buf.write("\7v\2\2\u00c1\u00c2\7t\2\2\u00c2\u00c3\7w\2\2\u00c3\u00c4")
        buf.write("\7e\2\2\u00c4\u00c5\7v\2\2\u00c5\30\3\2\2\2\u00c6\u00c7")
        buf.write("\7k\2\2\u00c7\u00c8\7p\2\2\u00c8\u00c9\7v\2\2\u00c9\u00ca")
        buf.write("\7g\2\2\u00ca\u00cb\7t\2\2\u00cb\u00cc\7h\2\2\u00cc\u00cd")
        buf.write("\7c\2\2\u00cd\u00ce\7e\2\2\u00ce\u00cf\7g\2\2\u00cf\32")
        buf.write("\3\2\2\2\u00d0\u00d1\7u\2\2\u00d1\u00d2\7v\2\2\u00d2\u00d3")
        buf.write("\7t\2\2\u00d3\u00d4\7k\2\2\u00d4\u00d5\7p\2\2\u00d5\u00d6")
        buf.write("\7i\2\2\u00d6\34\3\2\2\2\u00d7\u00d8\7k\2\2\u00d8\u00d9")
        buf.write("\7p\2\2\u00d9\u00da\7v\2\2\u00da\36\3\2\2\2\u00db\u00dc")
        buf.write("\7h\2\2\u00dc\u00dd\7n\2\2\u00dd\u00de\7q\2\2\u00de\u00df")
        buf.write("\7c\2\2\u00df\u00e0\7v\2\2\u00e0 \3\2\2\2\u00e1\u00e2")
        buf.write("\7d\2\2\u00e2\u00e3\7q\2\2\u00e3\u00e4\7q\2\2\u00e4\u00e5")
        buf.write("\7n\2\2\u00e5\u00e6\7g\2\2\u00e6\u00e7\7c\2\2\u00e7\u00e8")
        buf.write("\7p\2\2\u00e8\"\3\2\2\2\u00e9\u00ea\7e\2\2\u00ea\u00eb")
        buf.write("\7q\2\2\u00eb\u00ec\7p\2\2\u00ec\u00ed\7u\2\2\u00ed\u00ee")
        buf.write("\7v\2\2\u00ee$\3\2\2\2\u00ef\u00f0\7x\2\2\u00f0\u00f1")
        buf.write("\7c\2\2\u00f1\u00f2\7t\2\2\u00f2&\3\2\2\2\u00f3\u00f4")
        buf.write("\7e\2\2\u00f4\u00f5\7q\2\2\u00f5\u00f6\7p\2\2\u00f6\u00f7")
        buf.write("\7v\2\2\u00f7\u00f8\7k\2\2\u00f8\u00f9\7p\2\2\u00f9\u00fa")
        buf.write("\7w\2\2\u00fa\u00fb\7g\2\2\u00fb(\3\2\2\2\u00fc\u00fd")
        buf.write("\7d\2\2\u00fd\u00fe\7t\2\2\u00fe\u00ff\7g\2\2\u00ff\u0100")
        buf.write("\7c\2\2\u0100\u0101\7m\2\2\u0101*\3\2\2\2\u0102\u0103")
        buf.write("\7t\2\2\u0103\u0104\7c\2\2\u0104\u0105\7p\2\2\u0105\u0106")
        buf.write("\7i\2\2\u0106\u0107\7g\2\2\u0107,\3\2\2\2\u0108\u0109")
        buf.write("\7p\2\2\u0109\u010a\7k\2\2\u010a\u010b\7n\2\2\u010b.\3")
        buf.write("\2\2\2\u010c\u010d\7v\2\2\u010d\u010e\7t\2\2\u010e\u010f")
        buf.write("\7w\2\2\u010f\u0110\7g\2\2\u0110\60\3\2\2\2\u0111\u0112")
        buf.write("\7h\2\2\u0112\u0113\7c\2\2\u0113\u0114\7n\2\2\u0114\u0115")
        buf.write("\7u\2\2\u0115\u0116\7g\2\2\u0116\62\3\2\2\2\u0117\u0118")
        buf.write("\7#\2\2\u0118\64\3\2\2\2\u0119\u011a\7-\2\2\u011a\66\3")
        buf.write("\2\2\2\u011b\u011c\7/\2\2\u011c8\3\2\2\2\u011d\u011e\7")
        buf.write(",\2\2\u011e:\3\2\2\2\u011f\u0120\7\61\2\2\u0120<\3\2\2")
        buf.write("\2\u0121\u0122\7\'\2\2\u0122>\3\2\2\2\u0123\u0124\7?\2")
        buf.write("\2\u0124\u0125\7?\2\2\u0125@\3\2\2\2\u0126\u0127\7#\2")
        buf.write("\2\u0127\u0128\7?\2\2\u0128B\3\2\2\2\u0129\u012a\7>\2")
        buf.write("\2\u012aD\3\2\2\2\u012b\u012c\7@\2\2\u012cF\3\2\2\2\u012d")
        buf.write("\u012e\7>\2\2\u012e\u012f\7?\2\2\u012fH\3\2\2\2\u0130")
        buf.write("\u0131\7@\2\2\u0131\u0132\7?\2\2\u0132J\3\2\2\2\u0133")
        buf.write("\u0134\7~\2\2\u0134\u0135\7~\2\2\u0135L\3\2\2\2\u0136")
        buf.write("\u0137\7(\2\2\u0137\u0138\7(\2\2\u0138N\3\2\2\2\u0139")
        buf.write("\u013a\7?\2\2\u013aP\3\2\2\2\u013b\u013c\7-\2\2\u013c")
        buf.write("\u013d\7?\2\2\u013dR\3\2\2\2\u013e\u013f\7/\2\2\u013f")
        buf.write("\u0140\7?\2\2\u0140T\3\2\2\2\u0141\u0142\7,\2\2\u0142")
        buf.write("\u0143\7?\2\2\u0143V\3\2\2\2\u0144\u0145\7\61\2\2\u0145")
        buf.write("\u0146\7?\2\2\u0146X\3\2\2\2\u0147\u0148\7\'\2\2\u0148")
        buf.write("\u0149\7?\2\2\u0149Z\3\2\2\2\u014a\u014b\7\60\2\2\u014b")
        buf.write("\\\3\2\2\2\u014c\u014d\7<\2\2\u014d^\3\2\2\2\u014e\u014f")
        buf.write("\7*\2\2\u014f`\3\2\2\2\u0150\u0151\7+\2\2\u0151b\3\2\2")
        buf.write("\2\u0152\u0153\7}\2\2\u0153d\3\2\2\2\u0154\u0155\7\177")
        buf.write("\2\2\u0155f\3\2\2\2\u0156\u0157\7]\2\2\u0157h\3\2\2\2")
        buf.write("\u0158\u0159\7_\2\2\u0159j\3\2\2\2\u015a\u015b\7=\2\2")
        buf.write("\u015bl\3\2\2\2\u015c\u015d\7.\2\2\u015dn\3\2\2\2\u015e")
        buf.write("\u0162\t\2\2\2\u015f\u0161\t\3\2\2\u0160\u015f\3\2\2\2")
        buf.write("\u0161\u0164\3\2\2\2\u0162\u0160\3\2\2\2\u0162\u0163\3")
        buf.write("\2\2\2\u0163p\3\2\2\2\u0164\u0162\3\2\2\2\u0165\u0166")
        buf.write("\t\4\2\2\u0166r\3\2\2\2\u0167\u0169\t\5\2\2\u0168\u016a")
        buf.write("\t\6\2\2\u0169\u0168\3\2\2\2\u0169\u016a\3\2\2\2\u016a")
        buf.write("\u016b\3\2\2\2\u016b\u016c\5u;\2\u016ct\3\2\2\2\u016d")
        buf.write("\u0176\7\62\2\2\u016e\u0172\t\7\2\2\u016f\u0171\t\4\2")
        buf.write("\2\u0170\u016f\3\2\2\2\u0171\u0174\3\2\2\2\u0172\u0170")
        buf.write("\3\2\2\2\u0172\u0173\3\2\2\2\u0173\u0176\3\2\2\2\u0174")
        buf.write("\u0172\3\2\2\2\u0175\u016d\3\2\2\2\u0175\u016e\3\2\2\2")
        buf.write("\u0176v\3\2\2\2\u0177\u0178\7\62\2\2\u0178\u017c\7d\2")
        buf.write("\2\u0179\u017a\7\62\2\2\u017a\u017c\7D\2\2\u017b\u0177")
        buf.write("\3\2\2\2\u017b\u0179\3\2\2\2\u017c\u017e\3\2\2\2\u017d")
        buf.write("\u017f\t\b\2\2\u017e\u017d\3\2\2\2\u017f\u0180\3\2\2\2")
        buf.write("\u0180\u017e\3\2\2\2\u0180\u0181\3\2\2\2\u0181\u0182\3")
        buf.write("\2\2\2\u0182\u0183\b<\2\2\u0183x\3\2\2\2\u0184\u0185\7")
        buf.write("\62\2\2\u0185\u0189\7q\2\2\u0186\u0187\7\62\2\2\u0187")
        buf.write("\u0189\7Q\2\2\u0188\u0184\3\2\2\2\u0188\u0186\3\2\2\2")
        buf.write("\u0189\u018b\3\2\2\2\u018a\u018c\t\t\2\2\u018b\u018a\3")
        buf.write("\2\2\2\u018c\u018d\3\2\2\2\u018d\u018b\3\2\2\2\u018d\u018e")
        buf.write("\3\2\2\2\u018e\u018f\3\2\2\2\u018f\u0190\b=\3\2\u0190")
        buf.write("z\3\2\2\2\u0191\u0192\7\62\2\2\u0192\u0196\7z\2\2\u0193")
        buf.write("\u0194\7\62\2\2\u0194\u0196\7Z\2\2\u0195\u0191\3\2\2\2")
        buf.write("\u0195\u0193\3\2\2\2\u0196\u0198\3\2\2\2\u0197\u0199\t")
        buf.write("\n\2\2\u0198\u0197\3\2\2\2\u0199\u019a\3\2\2\2\u019a\u0198")
        buf.write("\3\2\2\2\u019a\u019b\3\2\2\2\u019b\u019c\3\2\2\2\u019c")
        buf.write("\u019d\b>\4\2\u019d|\3\2\2\2\u019e\u01a6\5u;\2\u019f\u01a3")
        buf.write("\7\60\2\2\u01a0\u01a2\t\4\2\2\u01a1\u01a0\3\2\2\2\u01a2")
        buf.write("\u01a5\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a3\u01a4\3\2\2\2")
        buf.write("\u01a4\u01a7\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a6\u019f\3")
        buf.write("\2\2\2\u01a6\u01a7\3\2\2\2\u01a7\u01a9\3\2\2\2\u01a8\u01aa")
        buf.write("\5s:\2\u01a9\u01a8\3\2\2\2\u01a9\u01aa\3\2\2\2\u01aa~")
        buf.write("\3\2\2\2\u01ab\u01b0\7$\2\2\u01ac\u01af\5\u0091I\2\u01ad")
        buf.write("\u01af\n\13\2\2\u01ae\u01ac\3\2\2\2\u01ae\u01ad\3\2\2")
        buf.write("\2\u01af\u01b2\3\2\2\2\u01b0\u01ae\3\2\2\2\u01b0\u01b1")
        buf.write("\3\2\2\2\u01b1\u01b3\3\2\2\2\u01b2\u01b0\3\2\2\2\u01b3")
        buf.write("\u01b4\7$\2\2\u01b4\u01b5\b@\5\2\u01b5\u0080\3\2\2\2\u01b6")
        buf.write("\u01b9\5/\30\2\u01b7\u01b9\5\61\31\2\u01b8\u01b6\3\2\2")
        buf.write("\2\u01b8\u01b7\3\2\2\2\u01b9\u0082\3\2\2\2\u01ba\u01bc")
        buf.write("\t\f\2\2\u01bb\u01ba\3\2\2\2\u01bc\u01bd\3\2\2\2\u01bd")
        buf.write("\u01bb\3\2\2\2\u01bd\u01be\3\2\2\2\u01be\u01bf\3\2\2\2")
        buf.write("\u01bf\u01c0\bB\6\2\u01c0\u0084\3\2\2\2\u01c1\u01c2\7")
        buf.write("\61\2\2\u01c2\u01c3\7\61\2\2\u01c3\u01c7\3\2\2\2\u01c4")
        buf.write("\u01c6\n\r\2\2\u01c5\u01c4\3\2\2\2\u01c6\u01c9\3\2\2\2")
        buf.write("\u01c7\u01c5\3\2\2\2\u01c7\u01c8\3\2\2\2\u01c8\u01ca\3")
        buf.write("\2\2\2\u01c9\u01c7\3\2\2\2\u01ca\u01cb\bC\6\2\u01cb\u0086")
        buf.write("\3\2\2\2\u01cc\u01cd\7\61\2\2\u01cd\u01ce\7,\2\2\u01ce")
        buf.write("\u01d3\3\2\2\2\u01cf\u01d2\5\u0087D\2\u01d0\u01d2\13\2")
        buf.write("\2\2\u01d1\u01cf\3\2\2\2\u01d1\u01d0\3\2\2\2\u01d2\u01d5")
        buf.write("\3\2\2\2\u01d3\u01d4\3\2\2\2\u01d3\u01d1\3\2\2\2\u01d4")
        buf.write("\u01d6\3\2\2\2\u01d5\u01d3\3\2\2\2\u01d6\u01d7\7,\2\2")
        buf.write("\u01d7\u01d8\7\61\2\2\u01d8\u01d9\3\2\2\2\u01d9\u01da")
        buf.write("\bD\6\2\u01da\u0088\3\2\2\2\u01db\u01dc\13\2\2\2\u01dc")
        buf.write("\u01dd\bE\7\2\u01dd\u008a\3\2\2\2\u01de\u01e3\7$\2\2\u01df")
        buf.write("\u01e2\n\13\2\2\u01e0\u01e2\5\u0091I\2\u01e1\u01df\3\2")
        buf.write("\2\2\u01e1\u01e0\3\2\2\2\u01e2\u01e5\3\2\2\2\u01e3\u01e1")
        buf.write("\3\2\2\2\u01e3\u01e4\3\2\2\2\u01e4\u01e9\3\2\2\2\u01e5")
        buf.write("\u01e3\3\2\2\2\u01e6\u01ea\t\16\2\2\u01e7\u01e8\7\17\2")
        buf.write("\2\u01e8\u01ea\7\f\2\2\u01e9\u01e6\3\2\2\2\u01e9\u01e7")
        buf.write("\3\2\2\2\u01ea\u01eb\3\2\2\2\u01eb\u01ec\bF\b\2\u01ec")
        buf.write("\u008c\3\2\2\2\u01ed\u01f2\7$\2\2\u01ee\u01f1\n\17\2\2")
        buf.write("\u01ef\u01f1\5\u0091I\2\u01f0\u01ee\3\2\2\2\u01f0\u01ef")
        buf.write("\3\2\2\2\u01f1\u01f4\3\2\2\2\u01f2\u01f0\3\2\2\2\u01f2")
        buf.write("\u01f3\3\2\2\2\u01f3\u01f9\3\2\2\2\u01f4\u01f2\3\2\2\2")
        buf.write("\u01f5\u01fa\t\20\2\2\u01f6\u01fa\5\u008fH\2\u01f7\u01f8")
        buf.write("\t\21\2\2\u01f8\u01fa\n\22\2\2\u01f9\u01f5\3\2\2\2\u01f9")
        buf.write("\u01f6\3\2\2\2\u01f9\u01f7\3\2\2\2\u01fa\u01fb\3\2\2\2")
        buf.write("\u01fb\u01fc\bG\t\2\u01fc\u008e\3\2\2\2\u01fd\u01fe\7")
        buf.write("^\2\2\u01fe\u01ff\n\23\2\2\u01ff\u0090\3\2\2\2\u0200\u0201")
        buf.write("\7^\2\2\u0201\u0205\t\23\2\2\u0202\u0203\t\21\2\2\u0203")
        buf.write("\u0205\t\22\2\2\u0204\u0200\3\2\2\2\u0204\u0202\3\2\2")
        buf.write("\2\u0205\u0092\3\2\2\2\37\2\u00a0\u0162\u0169\u0172\u0175")
        buf.write("\u017b\u0180\u0188\u018d\u0195\u019a\u01a3\u01a6\u01a9")
        buf.write("\u01ae\u01b0\u01b8\u01bd\u01c7\u01d1\u01d3\u01e1\u01e3")
        buf.write("\u01e9\u01f0\u01f2\u01f9\u0204\n\3<\2\3=\3\3>\4\3@\5\b")
        buf.write("\2\2\3E\6\3F\7\3G\b")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    REL = 4
    IF = 5
    ELSE = 6
    FOR = 7
    RETURN = 8
    FUNC = 9
    TYPE = 10
    STRUCT = 11
    INTERFACE = 12
    STRING = 13
    INT = 14
    FLOAT = 15
    BOOLEAN = 16
    CONST = 17
    VAR = 18
    CONTINUE = 19
    BREAK = 20
    RANGE = 21
    NIL = 22
    TRUE = 23
    FALSE = 24
    NOT = 25
    ADD = 26
    MINUS = 27
    MUL = 28
    DIV = 29
    MOD = 30
    EQUAL = 31
    DIFF = 32
    LT = 33
    GT = 34
    LE = 35
    GE = 36
    OR = 37
    AND = 38
    ASSIGN = 39
    ADD_ASSIGN = 40
    MINUS_ASSIGN = 41
    MULT_ASSIGN = 42
    DIV_ASSIGN = 43
    REM_ASSIGN = 44
    DOT = 45
    COLON = 46
    LPAREN = 47
    RPAREN = 48
    LBRACE = 49
    RBRACE = 50
    LBRACK = 51
    RBRACK = 52
    SEMI = 53
    COMMA = 54
    ID = 55
    DEC_LIT = 56
    BIN_LIT = 57
    OCT_LIT = 58
    HEX_LIT = 59
    FLOAT_LIT = 60
    STR_LIT = 61
    BOOL_LIT = 62
    WS = 63
    LINE_COMMENT = 64
    BLOCK_COMMENT = 65
    ERROR_CHAR = 66
    UNCLOSE_STRING = 67
    ILLEGAL_ESCAPE = 68

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':='", "'\r'", "'\n'", "'if'", "'else'", "'for'", "'return'", 
            "'func'", "'type'", "'struct'", "'interface'", "'string'", "'int'", 
            "'float'", "'boolean'", "'const'", "'var'", "'continue'", "'break'", 
            "'range'", "'nil'", "'true'", "'false'", "'!'", "'+'", "'-'", 
            "'*'", "'/'", "'%'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", 
            "'||'", "'&&'", "'='", "'+='", "'-='", "'*='", "'/='", "'%='", 
            "'.'", "':'", "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", 
            "','" ]

    symbolicNames = [ "<INVALID>",
            "REL", "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", 
            "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", 
            "CONTINUE", "BREAK", "RANGE", "NIL", "TRUE", "FALSE", "NOT", 
            "ADD", "MINUS", "MUL", "DIV", "MOD", "EQUAL", "DIFF", "LT", 
            "GT", "LE", "GE", "OR", "AND", "ASSIGN", "ADD_ASSIGN", "MINUS_ASSIGN", 
            "MULT_ASSIGN", "DIV_ASSIGN", "REM_ASSIGN", "DOT", "COLON", "LPAREN", 
            "RPAREN", "LBRACE", "RBRACE", "LBRACK", "RBRACK", "SEMI", "COMMA", 
            "ID", "DEC_LIT", "BIN_LIT", "OCT_LIT", "HEX_LIT", "FLOAT_LIT", 
            "STR_LIT", "BOOL_LIT", "WS", "LINE_COMMENT", "BLOCK_COMMENT", 
            "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "REL", "IF", "ELSE", "FOR", "RETURN", 
                  "FUNC", "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", 
                  "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", "BREAK", 
                  "RANGE", "NIL", "TRUE", "FALSE", "NOT", "ADD", "MINUS", 
                  "MUL", "DIV", "MOD", "EQUAL", "DIFF", "LT", "GT", "LE", 
                  "GE", "OR", "AND", "ASSIGN", "ADD_ASSIGN", "MINUS_ASSIGN", 
                  "MULT_ASSIGN", "DIV_ASSIGN", "REM_ASSIGN", "DOT", "COLON", 
                  "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACK", "RBRACK", 
                  "SEMI", "COMMA", "ID", "DIGIT", "EXP", "DEC_LIT", "BIN_LIT", 
                  "OCT_LIT", "HEX_LIT", "FLOAT_LIT", "STR_LIT", "BOOL_LIT", 
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
            actions[62] = self.STR_LIT_action 
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

     


