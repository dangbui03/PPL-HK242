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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2G")
        buf.write("\u020d\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\3\2\3\2\3")
        buf.write("\2\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\5\5\u00a3\n")
        buf.write("\5\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37")
        buf.write("\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3#\3#\3$\3$\3$\3%\3%\3")
        buf.write("%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3")
        buf.write("+\3,\3,\3,\3-\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3")
        buf.write("\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67")
        buf.write("\3\67\38\38\78\u0163\n8\f8\168\u0166\138\39\39\3:\3:\5")
        buf.write(":\u016c\n:\3:\3:\3;\3;\3;\7;\u0173\n;\f;\16;\u0176\13")
        buf.write(";\5;\u0178\n;\3;\5;\u017b\n;\3<\3<\3<\7<\u0180\n<\f<\16")
        buf.write("<\u0183\13<\5<\u0185\n<\3=\3=\3=\3=\5=\u018b\n=\3=\6=")
        buf.write("\u018e\n=\r=\16=\u018f\3=\3=\3>\3>\3>\3>\5>\u0198\n>\3")
        buf.write(">\6>\u019b\n>\r>\16>\u019c\3>\3>\3?\3?\3?\3?\5?\u01a5")
        buf.write("\n?\3?\6?\u01a8\n?\r?\16?\u01a9\3?\3?\3@\3@\3@\7@\u01b1")
        buf.write("\n@\f@\16@\u01b4\13@\3@\3@\3@\3A\3A\5A\u01bb\nA\3B\6B")
        buf.write("\u01be\nB\rB\16B\u01bf\3C\6C\u01c3\nC\rC\16C\u01c4\3C")
        buf.write("\3C\3D\3D\3D\3D\7D\u01cd\nD\fD\16D\u01d0\13D\3D\3D\3E")
        buf.write("\3E\3E\3E\3E\7E\u01d9\nE\fE\16E\u01dc\13E\3E\3E\3E\3E")
        buf.write("\3E\3F\3F\3F\3G\3G\3G\7G\u01e9\nG\fG\16G\u01ec\13G\3G")
        buf.write("\3G\3G\5G\u01f1\nG\3G\3G\3H\3H\3H\7H\u01f8\nH\fH\16H\u01fb")
        buf.write("\13H\3H\3H\3H\3H\5H\u0201\nH\3H\3H\3I\3I\3I\3J\3J\3J\3")
        buf.write("J\5J\u020c\nJ\3\u01da\2K\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write("\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63")
        buf.write("e\64g\65i\66k\67m8o9q\2s\2u:w;y<{=}>\177?\u0081@\u0083")
        buf.write("A\u0085B\u0087C\u0089D\u008bE\u008dF\u008fG\u0091\2\u0093")
        buf.write("\2\3\2\24\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\4\2GGgg\4")
        buf.write("\2--//\3\2\63;\3\2\62\63\3\2\629\5\2\62;CHch\7\2\f\f\16")
        buf.write("\17$$))^^\5\2\13\13\16\17\"\"\4\2\f\f\17\17\3\3\f\f\b")
        buf.write("\2\f\f\17\17$$))^^dd\5\2\17\17))^^\3\2))\3\2$$\b\2))^")
        buf.write("^ddppttvv\2\u022a\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
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
        buf.write("\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\3\u0095")
        buf.write("\3\2\2\2\5\u0098\3\2\2\2\7\u009a\3\2\2\2\t\u00a2\3\2\2")
        buf.write("\2\13\u00a4\3\2\2\2\r\u00a7\3\2\2\2\17\u00ac\3\2\2\2\21")
        buf.write("\u00b0\3\2\2\2\23\u00b7\3\2\2\2\25\u00bc\3\2\2\2\27\u00c1")
        buf.write("\3\2\2\2\31\u00c8\3\2\2\2\33\u00d2\3\2\2\2\35\u00d9\3")
        buf.write("\2\2\2\37\u00dd\3\2\2\2!\u00e3\3\2\2\2#\u00eb\3\2\2\2")
        buf.write("%\u00f1\3\2\2\2\'\u00f5\3\2\2\2)\u00fe\3\2\2\2+\u0104")
        buf.write("\3\2\2\2-\u010a\3\2\2\2/\u010e\3\2\2\2\61\u0113\3\2\2")
        buf.write("\2\63\u0119\3\2\2\2\65\u011b\3\2\2\2\67\u011d\3\2\2\2")
        buf.write("9\u011f\3\2\2\2;\u0121\3\2\2\2=\u0123\3\2\2\2?\u0125\3")
        buf.write("\2\2\2A\u0128\3\2\2\2C\u012b\3\2\2\2E\u012d\3\2\2\2G\u012f")
        buf.write("\3\2\2\2I\u0132\3\2\2\2K\u0135\3\2\2\2M\u0138\3\2\2\2")
        buf.write("O\u013b\3\2\2\2Q\u013d\3\2\2\2S\u0140\3\2\2\2U\u0143\3")
        buf.write("\2\2\2W\u0146\3\2\2\2Y\u0149\3\2\2\2[\u014c\3\2\2\2]\u014e")
        buf.write("\3\2\2\2_\u0150\3\2\2\2a\u0152\3\2\2\2c\u0154\3\2\2\2")
        buf.write("e\u0156\3\2\2\2g\u0158\3\2\2\2i\u015a\3\2\2\2k\u015c\3")
        buf.write("\2\2\2m\u015e\3\2\2\2o\u0160\3\2\2\2q\u0167\3\2\2\2s\u0169")
        buf.write("\3\2\2\2u\u016f\3\2\2\2w\u0184\3\2\2\2y\u018a\3\2\2\2")
        buf.write("{\u0197\3\2\2\2}\u01a4\3\2\2\2\177\u01ad\3\2\2\2\u0081")
        buf.write("\u01ba\3\2\2\2\u0083\u01bd\3\2\2\2\u0085\u01c2\3\2\2\2")
        buf.write("\u0087\u01c8\3\2\2\2\u0089\u01d3\3\2\2\2\u008b\u01e2\3")
        buf.write("\2\2\2\u008d\u01e5\3\2\2\2\u008f\u01f4\3\2\2\2\u0091\u0204")
        buf.write("\3\2\2\2\u0093\u020b\3\2\2\2\u0095\u0096\7<\2\2\u0096")
        buf.write("\u0097\7?\2\2\u0097\4\3\2\2\2\u0098\u0099\7\17\2\2\u0099")
        buf.write("\6\3\2\2\2\u009a\u009b\7\f\2\2\u009b\b\3\2\2\2\u009c\u00a3")
        buf.write("\5C\"\2\u009d\u00a3\5E#\2\u009e\u00a3\5G$\2\u009f\u00a3")
        buf.write("\5I%\2\u00a0\u00a3\5? \2\u00a1\u00a3\5A!\2\u00a2\u009c")
        buf.write("\3\2\2\2\u00a2\u009d\3\2\2\2\u00a2\u009e\3\2\2\2\u00a2")
        buf.write("\u009f\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a2\u00a1\3\2\2\2")
        buf.write("\u00a3\n\3\2\2\2\u00a4\u00a5\7k\2\2\u00a5\u00a6\7h\2\2")
        buf.write("\u00a6\f\3\2\2\2\u00a7\u00a8\7g\2\2\u00a8\u00a9\7n\2\2")
        buf.write("\u00a9\u00aa\7u\2\2\u00aa\u00ab\7g\2\2\u00ab\16\3\2\2")
        buf.write("\2\u00ac\u00ad\7h\2\2\u00ad\u00ae\7q\2\2\u00ae\u00af\7")
        buf.write("t\2\2\u00af\20\3\2\2\2\u00b0\u00b1\7t\2\2\u00b1\u00b2")
        buf.write("\7g\2\2\u00b2\u00b3\7v\2\2\u00b3\u00b4\7w\2\2\u00b4\u00b5")
        buf.write("\7t\2\2\u00b5\u00b6\7p\2\2\u00b6\22\3\2\2\2\u00b7\u00b8")
        buf.write("\7h\2\2\u00b8\u00b9\7w\2\2\u00b9\u00ba\7p\2\2\u00ba\u00bb")
        buf.write("\7e\2\2\u00bb\24\3\2\2\2\u00bc\u00bd\7v\2\2\u00bd\u00be")
        buf.write("\7{\2\2\u00be\u00bf\7r\2\2\u00bf\u00c0\7g\2\2\u00c0\26")
        buf.write("\3\2\2\2\u00c1\u00c2\7u\2\2\u00c2\u00c3\7v\2\2\u00c3\u00c4")
        buf.write("\7t\2\2\u00c4\u00c5\7w\2\2\u00c5\u00c6\7e\2\2\u00c6\u00c7")
        buf.write("\7v\2\2\u00c7\30\3\2\2\2\u00c8\u00c9\7k\2\2\u00c9\u00ca")
        buf.write("\7p\2\2\u00ca\u00cb\7v\2\2\u00cb\u00cc\7g\2\2\u00cc\u00cd")
        buf.write("\7t\2\2\u00cd\u00ce\7h\2\2\u00ce\u00cf\7c\2\2\u00cf\u00d0")
        buf.write("\7e\2\2\u00d0\u00d1\7g\2\2\u00d1\32\3\2\2\2\u00d2\u00d3")
        buf.write("\7u\2\2\u00d3\u00d4\7v\2\2\u00d4\u00d5\7t\2\2\u00d5\u00d6")
        buf.write("\7k\2\2\u00d6\u00d7\7p\2\2\u00d7\u00d8\7i\2\2\u00d8\34")
        buf.write("\3\2\2\2\u00d9\u00da\7k\2\2\u00da\u00db\7p\2\2\u00db\u00dc")
        buf.write("\7v\2\2\u00dc\36\3\2\2\2\u00dd\u00de\7h\2\2\u00de\u00df")
        buf.write("\7n\2\2\u00df\u00e0\7q\2\2\u00e0\u00e1\7c\2\2\u00e1\u00e2")
        buf.write("\7v\2\2\u00e2 \3\2\2\2\u00e3\u00e4\7d\2\2\u00e4\u00e5")
        buf.write("\7q\2\2\u00e5\u00e6\7q\2\2\u00e6\u00e7\7n\2\2\u00e7\u00e8")
        buf.write("\7g\2\2\u00e8\u00e9\7c\2\2\u00e9\u00ea\7p\2\2\u00ea\"")
        buf.write("\3\2\2\2\u00eb\u00ec\7e\2\2\u00ec\u00ed\7q\2\2\u00ed\u00ee")
        buf.write("\7p\2\2\u00ee\u00ef\7u\2\2\u00ef\u00f0\7v\2\2\u00f0$\3")
        buf.write("\2\2\2\u00f1\u00f2\7x\2\2\u00f2\u00f3\7c\2\2\u00f3\u00f4")
        buf.write("\7t\2\2\u00f4&\3\2\2\2\u00f5\u00f6\7e\2\2\u00f6\u00f7")
        buf.write("\7q\2\2\u00f7\u00f8\7p\2\2\u00f8\u00f9\7v\2\2\u00f9\u00fa")
        buf.write("\7k\2\2\u00fa\u00fb\7p\2\2\u00fb\u00fc\7w\2\2\u00fc\u00fd")
        buf.write("\7g\2\2\u00fd(\3\2\2\2\u00fe\u00ff\7d\2\2\u00ff\u0100")
        buf.write("\7t\2\2\u0100\u0101\7g\2\2\u0101\u0102\7c\2\2\u0102\u0103")
        buf.write("\7m\2\2\u0103*\3\2\2\2\u0104\u0105\7t\2\2\u0105\u0106")
        buf.write("\7c\2\2\u0106\u0107\7p\2\2\u0107\u0108\7i\2\2\u0108\u0109")
        buf.write("\7g\2\2\u0109,\3\2\2\2\u010a\u010b\7p\2\2\u010b\u010c")
        buf.write("\7k\2\2\u010c\u010d\7n\2\2\u010d.\3\2\2\2\u010e\u010f")
        buf.write("\7v\2\2\u010f\u0110\7t\2\2\u0110\u0111\7w\2\2\u0111\u0112")
        buf.write("\7g\2\2\u0112\60\3\2\2\2\u0113\u0114\7h\2\2\u0114\u0115")
        buf.write("\7c\2\2\u0115\u0116\7n\2\2\u0116\u0117\7u\2\2\u0117\u0118")
        buf.write("\7g\2\2\u0118\62\3\2\2\2\u0119\u011a\7#\2\2\u011a\64\3")
        buf.write("\2\2\2\u011b\u011c\7-\2\2\u011c\66\3\2\2\2\u011d\u011e")
        buf.write("\7/\2\2\u011e8\3\2\2\2\u011f\u0120\7,\2\2\u0120:\3\2\2")
        buf.write("\2\u0121\u0122\7\61\2\2\u0122<\3\2\2\2\u0123\u0124\7\'")
        buf.write("\2\2\u0124>\3\2\2\2\u0125\u0126\7?\2\2\u0126\u0127\7?")
        buf.write("\2\2\u0127@\3\2\2\2\u0128\u0129\7#\2\2\u0129\u012a\7?")
        buf.write("\2\2\u012aB\3\2\2\2\u012b\u012c\7>\2\2\u012cD\3\2\2\2")
        buf.write("\u012d\u012e\7@\2\2\u012eF\3\2\2\2\u012f\u0130\7>\2\2")
        buf.write("\u0130\u0131\7?\2\2\u0131H\3\2\2\2\u0132\u0133\7@\2\2")
        buf.write("\u0133\u0134\7?\2\2\u0134J\3\2\2\2\u0135\u0136\7~\2\2")
        buf.write("\u0136\u0137\7~\2\2\u0137L\3\2\2\2\u0138\u0139\7(\2\2")
        buf.write("\u0139\u013a\7(\2\2\u013aN\3\2\2\2\u013b\u013c\7?\2\2")
        buf.write("\u013cP\3\2\2\2\u013d\u013e\7-\2\2\u013e\u013f\7?\2\2")
        buf.write("\u013fR\3\2\2\2\u0140\u0141\7/\2\2\u0141\u0142\7?\2\2")
        buf.write("\u0142T\3\2\2\2\u0143\u0144\7,\2\2\u0144\u0145\7?\2\2")
        buf.write("\u0145V\3\2\2\2\u0146\u0147\7\61\2\2\u0147\u0148\7?\2")
        buf.write("\2\u0148X\3\2\2\2\u0149\u014a\7\'\2\2\u014a\u014b\7?\2")
        buf.write("\2\u014bZ\3\2\2\2\u014c\u014d\7\60\2\2\u014d\\\3\2\2\2")
        buf.write("\u014e\u014f\7<\2\2\u014f^\3\2\2\2\u0150\u0151\7*\2\2")
        buf.write("\u0151`\3\2\2\2\u0152\u0153\7+\2\2\u0153b\3\2\2\2\u0154")
        buf.write("\u0155\7}\2\2\u0155d\3\2\2\2\u0156\u0157\7\177\2\2\u0157")
        buf.write("f\3\2\2\2\u0158\u0159\7]\2\2\u0159h\3\2\2\2\u015a\u015b")
        buf.write("\7_\2\2\u015bj\3\2\2\2\u015c\u015d\7=\2\2\u015dl\3\2\2")
        buf.write("\2\u015e\u015f\7.\2\2\u015fn\3\2\2\2\u0160\u0164\t\2\2")
        buf.write("\2\u0161\u0163\t\3\2\2\u0162\u0161\3\2\2\2\u0163\u0166")
        buf.write("\3\2\2\2\u0164\u0162\3\2\2\2\u0164\u0165\3\2\2\2\u0165")
        buf.write("p\3\2\2\2\u0166\u0164\3\2\2\2\u0167\u0168\t\4\2\2\u0168")
        buf.write("r\3\2\2\2\u0169\u016b\t\5\2\2\u016a\u016c\t\6\2\2\u016b")
        buf.write("\u016a\3\2\2\2\u016b\u016c\3\2\2\2\u016c\u016d\3\2\2\2")
        buf.write("\u016d\u016e\5w<\2\u016et\3\2\2\2\u016f\u0177\5w<\2\u0170")
        buf.write("\u0174\7\60\2\2\u0171\u0173\5q9\2\u0172\u0171\3\2\2\2")
        buf.write("\u0173\u0176\3\2\2\2\u0174\u0172\3\2\2\2\u0174\u0175\3")
        buf.write("\2\2\2\u0175\u0178\3\2\2\2\u0176\u0174\3\2\2\2\u0177\u0170")
        buf.write("\3\2\2\2\u0177\u0178\3\2\2\2\u0178\u017a\3\2\2\2\u0179")
        buf.write("\u017b\5s:\2\u017a\u0179\3\2\2\2\u017a\u017b\3\2\2\2\u017b")
        buf.write("v\3\2\2\2\u017c\u0185\7\62\2\2\u017d\u0181\t\7\2\2\u017e")
        buf.write("\u0180\5q9\2\u017f\u017e\3\2\2\2\u0180\u0183\3\2\2\2\u0181")
        buf.write("\u017f\3\2\2\2\u0181\u0182\3\2\2\2\u0182\u0185\3\2\2\2")
        buf.write("\u0183\u0181\3\2\2\2\u0184\u017c\3\2\2\2\u0184\u017d\3")
        buf.write("\2\2\2\u0185x\3\2\2\2\u0186\u0187\7\62\2\2\u0187\u018b")
        buf.write("\7d\2\2\u0188\u0189\7\62\2\2\u0189\u018b\7D\2\2\u018a")
        buf.write("\u0186\3\2\2\2\u018a\u0188\3\2\2\2\u018b\u018d\3\2\2\2")
        buf.write("\u018c\u018e\t\b\2\2\u018d\u018c\3\2\2\2\u018e\u018f\3")
        buf.write("\2\2\2\u018f\u018d\3\2\2\2\u018f\u0190\3\2\2\2\u0190\u0191")
        buf.write("\3\2\2\2\u0191\u0192\b=\2\2\u0192z\3\2\2\2\u0193\u0194")
        buf.write("\7\62\2\2\u0194\u0198\7q\2\2\u0195\u0196\7\62\2\2\u0196")
        buf.write("\u0198\7Q\2\2\u0197\u0193\3\2\2\2\u0197\u0195\3\2\2\2")
        buf.write("\u0198\u019a\3\2\2\2\u0199\u019b\t\t\2\2\u019a\u0199\3")
        buf.write("\2\2\2\u019b\u019c\3\2\2\2\u019c\u019a\3\2\2\2\u019c\u019d")
        buf.write("\3\2\2\2\u019d\u019e\3\2\2\2\u019e\u019f\b>\3\2\u019f")
        buf.write("|\3\2\2\2\u01a0\u01a1\7\62\2\2\u01a1\u01a5\7z\2\2\u01a2")
        buf.write("\u01a3\7\62\2\2\u01a3\u01a5\7Z\2\2\u01a4\u01a0\3\2\2\2")
        buf.write("\u01a4\u01a2\3\2\2\2\u01a5\u01a7\3\2\2\2\u01a6\u01a8\t")
        buf.write("\n\2\2\u01a7\u01a6\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9\u01a7")
        buf.write("\3\2\2\2\u01a9\u01aa\3\2\2\2\u01aa\u01ab\3\2\2\2\u01ab")
        buf.write("\u01ac\b?\4\2\u01ac~\3\2\2\2\u01ad\u01b2\7$\2\2\u01ae")
        buf.write("\u01b1\5\u0093J\2\u01af\u01b1\n\13\2\2\u01b0\u01ae\3\2")
        buf.write("\2\2\u01b0\u01af\3\2\2\2\u01b1\u01b4\3\2\2\2\u01b2\u01b0")
        buf.write("\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3\u01b5\3\2\2\2\u01b4")
        buf.write("\u01b2\3\2\2\2\u01b5\u01b6\7$\2\2\u01b6\u01b7\b@\5\2\u01b7")
        buf.write("\u0080\3\2\2\2\u01b8\u01bb\5/\30\2\u01b9\u01bb\5\61\31")
        buf.write("\2\u01ba\u01b8\3\2\2\2\u01ba\u01b9\3\2\2\2\u01bb\u0082")
        buf.write("\3\2\2\2\u01bc\u01be\t\4\2\2\u01bd\u01bc\3\2\2\2\u01be")
        buf.write("\u01bf\3\2\2\2\u01bf\u01bd\3\2\2\2\u01bf\u01c0\3\2\2\2")
        buf.write("\u01c0\u0084\3\2\2\2\u01c1\u01c3\t\f\2\2\u01c2\u01c1\3")
        buf.write("\2\2\2\u01c3\u01c4\3\2\2\2\u01c4\u01c2\3\2\2\2\u01c4\u01c5")
        buf.write("\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6\u01c7\bC\6\2\u01c7")
        buf.write("\u0086\3\2\2\2\u01c8\u01c9\7\61\2\2\u01c9\u01ca\7\61\2")
        buf.write("\2\u01ca\u01ce\3\2\2\2\u01cb\u01cd\n\r\2\2\u01cc\u01cb")
        buf.write("\3\2\2\2\u01cd\u01d0\3\2\2\2\u01ce\u01cc\3\2\2\2\u01ce")
        buf.write("\u01cf\3\2\2\2\u01cf\u01d1\3\2\2\2\u01d0\u01ce\3\2\2\2")
        buf.write("\u01d1\u01d2\bD\6\2\u01d2\u0088\3\2\2\2\u01d3\u01d4\7")
        buf.write("\61\2\2\u01d4\u01d5\7,\2\2\u01d5\u01da\3\2\2\2\u01d6\u01d9")
        buf.write("\5\u0089E\2\u01d7\u01d9\13\2\2\2\u01d8\u01d6\3\2\2\2\u01d8")
        buf.write("\u01d7\3\2\2\2\u01d9\u01dc\3\2\2\2\u01da\u01db\3\2\2\2")
        buf.write("\u01da\u01d8\3\2\2\2\u01db\u01dd\3\2\2\2\u01dc\u01da\3")
        buf.write("\2\2\2\u01dd\u01de\7,\2\2\u01de\u01df\7\61\2\2\u01df\u01e0")
        buf.write("\3\2\2\2\u01e0\u01e1\bE\6\2\u01e1\u008a\3\2\2\2\u01e2")
        buf.write("\u01e3\13\2\2\2\u01e3\u01e4\bF\7\2\u01e4\u008c\3\2\2\2")
        buf.write("\u01e5\u01ea\7$\2\2\u01e6\u01e9\n\13\2\2\u01e7\u01e9\5")
        buf.write("\u0093J\2\u01e8\u01e6\3\2\2\2\u01e8\u01e7\3\2\2\2\u01e9")
        buf.write("\u01ec\3\2\2\2\u01ea\u01e8\3\2\2\2\u01ea\u01eb\3\2\2\2")
        buf.write("\u01eb\u01f0\3\2\2\2\u01ec\u01ea\3\2\2\2\u01ed\u01f1\t")
        buf.write("\16\2\2\u01ee\u01ef\7\17\2\2\u01ef\u01f1\7\f\2\2\u01f0")
        buf.write("\u01ed\3\2\2\2\u01f0\u01ee\3\2\2\2\u01f1\u01f2\3\2\2\2")
        buf.write("\u01f2\u01f3\bG\b\2\u01f3\u008e\3\2\2\2\u01f4\u01f9\7")
        buf.write("$\2\2\u01f5\u01f8\n\17\2\2\u01f6\u01f8\5\u0093J\2\u01f7")
        buf.write("\u01f5\3\2\2\2\u01f7\u01f6\3\2\2\2\u01f8\u01fb\3\2\2\2")
        buf.write("\u01f9\u01f7\3\2\2\2\u01f9\u01fa\3\2\2\2\u01fa\u0200\3")
        buf.write("\2\2\2\u01fb\u01f9\3\2\2\2\u01fc\u0201\t\20\2\2\u01fd")
        buf.write("\u0201\5\u0091I\2\u01fe\u01ff\t\21\2\2\u01ff\u0201\n\22")
        buf.write("\2\2\u0200\u01fc\3\2\2\2\u0200\u01fd\3\2\2\2\u0200\u01fe")
        buf.write("\3\2\2\2\u0201\u0202\3\2\2\2\u0202\u0203\bH\t\2\u0203")
        buf.write("\u0090\3\2\2\2\u0204\u0205\7^\2\2\u0205\u0206\n\23\2\2")
        buf.write("\u0206\u0092\3\2\2\2\u0207\u0208\7^\2\2\u0208\u020c\t")
        buf.write("\23\2\2\u0209\u020a\t\21\2\2\u020a\u020c\t\22\2\2\u020b")
        buf.write("\u0207\3\2\2\2\u020b\u0209\3\2\2\2\u020c\u0094\3\2\2\2")
        buf.write(" \2\u00a2\u0164\u016b\u0174\u0177\u017a\u0181\u0184\u018a")
        buf.write("\u018f\u0197\u019c\u01a4\u01a9\u01b0\u01b2\u01ba\u01bf")
        buf.write("\u01c4\u01ce\u01d8\u01da\u01e8\u01ea\u01f0\u01f7\u01f9")
        buf.write("\u0200\u020b\n\3=\2\3>\3\3?\4\3@\5\b\2\2\3F\6\3G\7\3H")
        buf.write("\b")
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
    FLOAT_LIT = 56
    DEC_LIT = 57
    BIN_LIT = 58
    OCT_LIT = 59
    HEX_LIT = 60
    STR_LIT = 61
    BOOL_LIT = 62
    INT_LIT = 63
    WS = 64
    LINE_COMMENT = 65
    BLOCK_COMMENT = 66
    ERROR_CHAR = 67
    UNCLOSE_STRING = 68
    ILLEGAL_ESCAPE = 69

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
            "ID", "FLOAT_LIT", "DEC_LIT", "BIN_LIT", "OCT_LIT", "HEX_LIT", 
            "STR_LIT", "BOOL_LIT", "INT_LIT", "WS", "LINE_COMMENT", "BLOCK_COMMENT", 
            "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "REL", "IF", "ELSE", "FOR", "RETURN", 
                  "FUNC", "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", 
                  "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", "BREAK", 
                  "RANGE", "NIL", "TRUE", "FALSE", "NOT", "ADD", "MINUS", 
                  "MUL", "DIV", "MOD", "EQUAL", "DIFF", "LT", "GT", "LE", 
                  "GE", "OR", "AND", "ASSIGN", "ADD_ASSIGN", "MINUS_ASSIGN", 
                  "MULT_ASSIGN", "DIV_ASSIGN", "REM_ASSIGN", "DOT", "COLON", 
                  "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACK", "RBRACK", 
                  "SEMI", "COMMA", "ID", "DIGIT", "EXP", "FLOAT_LIT", "DEC_LIT", 
                  "BIN_LIT", "OCT_LIT", "HEX_LIT", "STR_LIT", "BOOL_LIT", 
                  "INT_LIT", "WS", "LINE_COMMENT", "BLOCK_COMMENT", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "IllegalEscape", "ESCAPE_SEQ" ]

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
            actions[59] = self.BIN_LIT_action 
            actions[60] = self.OCT_LIT_action 
            actions[61] = self.HEX_LIT_action 
            actions[62] = self.STR_LIT_action 
            actions[68] = self.ERROR_CHAR_action 
            actions[69] = self.UNCLOSE_STRING_action 
            actions[70] = self.ILLEGAL_ESCAPE_action 
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

     


