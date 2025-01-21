# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\64")
        buf.write("\u01a3\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\3\2\7\2Z\n\2\f")
        buf.write("\2\16\2]\13\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3f\n\3\3\4")
        buf.write("\3\4\3\4\3\4\5\4l\n\4\3\5\3\5\3\5\3\5\5\5r\n\5\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\b\5\b\177\n\b\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\5\t\u0088\n\t\3\n\3\n\3\n\3\n\5")
        buf.write("\n\u008e\n\n\3\13\3\13\3\13\3\13\5\13\u0094\n\13\3\13")
        buf.write("\3\13\5\13\u0098\n\13\3\13\3\13\5\13\u009c\n\13\3\13\3")
        buf.write("\13\5\13\u00a0\n\13\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00a8")
        buf.write("\n\f\3\r\3\r\3\r\3\r\3\r\5\r\u00af\n\r\3\16\3\16\3\16")
        buf.write("\3\16\5\16\u00b5\n\16\3\17\3\17\3\17\3\17\3\17\5\17\u00bc")
        buf.write("\n\17\3\20\3\20\3\20\3\20\3\20\5\20\u00c3\n\20\3\21\3")
        buf.write("\21\3\21\3\21\3\21\3\21\7\21\u00cb\n\21\f\21\16\21\u00ce")
        buf.write("\13\21\3\22\3\22\3\22\3\22\3\22\3\22\7\22\u00d6\n\22\f")
        buf.write("\22\16\22\u00d9\13\22\3\23\3\23\3\23\3\23\3\23\3\23\7")
        buf.write("\23\u00e1\n\23\f\23\16\23\u00e4\13\23\3\24\3\24\3\24\5")
        buf.write("\24\u00e9\n\24\3\25\3\25\3\25\5\25\u00ee\n\25\3\26\3\26")
        buf.write("\3\26\3\26\5\26\u00f4\n\26\3\26\5\26\u00f7\n\26\3\26\3")
        buf.write("\26\3\26\3\26\3\26\5\26\u00fe\n\26\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\5\27\u0107\n\27\3\30\3\30\3\30\5\30\u010c")
        buf.write("\n\30\3\30\3\30\3\31\3\31\3\31\3\31\5\31\u0114\n\31\3")
        buf.write("\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\5\33\u011f")
        buf.write("\n\33\3\34\3\34\3\34\3\34\3\34\5\34\u0126\n\34\3\35\3")
        buf.write("\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\5\36\u0135\n\36\3\37\3\37\3\37\3 \3 \3 \3 \3 \3")
        buf.write("!\3!\3!\3!\3!\3!\5!\u0145\n!\3\"\3\"\3\"\3\"\3\"\5\"\u014c")
        buf.write("\n\"\3\"\3\"\5\"\u0150\n\"\3\"\3\"\5\"\u0154\n\"\3#\3")
        buf.write("#\3#\3#\3#\5#\u015b\n#\3#\3#\5#\u015f\n#\3#\3#\3#\5#\u0164")
        buf.write("\n#\3$\3$\5$\u0168\n$\3$\3$\5$\u016c\n$\3%\3%\3%\3%\3")
        buf.write("%\3%\3%\5%\u0175\n%\3%\3%\5%\u0179\n%\3&\3&\3&\3\'\3\'")
        buf.write("\3\'\3(\3(\5(\u0183\n(\3(\3(\3)\3)\3)\5)\u018a\n)\3)\3")
        buf.write(")\3)\3*\3*\3*\3*\3*\3*\3+\3+\5+\u0197\n+\3+\3+\3+\5+\u019c")
        buf.write("\n+\3,\6,\u019f\n,\r,\16,\u01a0\3,\2\5 \"$-\2\4\6\b\n")
        buf.write("\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<")
        buf.write(">@BDFHJLNPRTV\2\7\3\2\5\7\4\2\36\36 %\3\2\27\30\3\2\31")
        buf.write("\32\3\2\33\35\2\u01b4\2[\3\2\2\2\4e\3\2\2\2\6k\3\2\2\2")
        buf.write("\bq\3\2\2\2\ns\3\2\2\2\fx\3\2\2\2\16z\3\2\2\2\20\u0080")
        buf.write("\3\2\2\2\22\u0089\3\2\2\2\24\u008f\3\2\2\2\26\u00a1\3")
        buf.write("\2\2\2\30\u00ae\3\2\2\2\32\u00b4\3\2\2\2\34\u00bb\3\2")
        buf.write("\2\2\36\u00c2\3\2\2\2 \u00c4\3\2\2\2\"\u00cf\3\2\2\2$")
        buf.write("\u00da\3\2\2\2&\u00e8\3\2\2\2(\u00ed\3\2\2\2*\u00fd\3")
        buf.write("\2\2\2,\u0106\3\2\2\2.\u0108\3\2\2\2\60\u0113\3\2\2\2")
        buf.write("\62\u0115\3\2\2\2\64\u011e\3\2\2\2\66\u0125\3\2\2\28\u0127")
        buf.write("\3\2\2\2:\u0134\3\2\2\2<\u0136\3\2\2\2>\u0139\3\2\2\2")
        buf.write("@\u0144\3\2\2\2B\u0146\3\2\2\2D\u0163\3\2\2\2F\u0165\3")
        buf.write("\2\2\2H\u016d\3\2\2\2J\u017a\3\2\2\2L\u017d\3\2\2\2N\u0180")
        buf.write("\3\2\2\2P\u0186\3\2\2\2R\u018e\3\2\2\2T\u019b\3\2\2\2")
        buf.write("V\u019e\3\2\2\2XZ\7/\2\2YX\3\2\2\2Z]\3\2\2\2[Y\3\2\2\2")
        buf.write("[\\\3\2\2\2\\^\3\2\2\2][\3\2\2\2^_\5\4\3\2_`\7\2\2\3`")
        buf.write("\3\3\2\2\2ab\5\6\4\2bc\5\4\3\2cf\3\2\2\2df\5\6\4\2ea\3")
        buf.write("\2\2\2ed\3\2\2\2f\5\3\2\2\2gl\5\24\13\2hi\5\b\5\2ij\5")
        buf.write("V,\2jl\3\2\2\2kg\3\2\2\2kh\3\2\2\2l\7\3\2\2\2mr\5\n\6")
        buf.write("\2nr\5\16\b\2or\5\20\t\2pr\5\22\n\2qm\3\2\2\2qn\3\2\2")
        buf.write("\2qo\3\2\2\2qp\3\2\2\2r\t\3\2\2\2st\7\t\2\2tu\7,\2\2u")
        buf.write("v\7\37\2\2vw\5\34\17\2w\13\3\2\2\2xy\t\2\2\2y\r\3\2\2")
        buf.write("\2z{\5\f\7\2{~\7,\2\2|}\7\37\2\2}\177\5\34\17\2~|\3\2")
        buf.write("\2\2~\177\3\2\2\2\177\17\3\2\2\2\u0080\u0081\5\f\7\2\u0081")
        buf.write("\u0082\7,\2\2\u0082\u0083\7\'\2\2\u0083\u0084\5\32\16")
        buf.write("\2\u0084\u0087\7(\2\2\u0085\u0086\7\37\2\2\u0086\u0088")
        buf.write("\5\34\17\2\u0087\u0085\3\2\2\2\u0087\u0088\3\2\2\2\u0088")
        buf.write("\21\3\2\2\2\u0089\u008a\7\n\2\2\u008a\u008d\7,\2\2\u008b")
        buf.write("\u008c\7\37\2\2\u008c\u008e\5\34\17\2\u008d\u008b\3\2")
        buf.write("\2\2\u008d\u008e\3\2\2\2\u008e\23\3\2\2\2\u008f\u0090")
        buf.write("\7\13\2\2\u0090\u0091\7,\2\2\u0091\u0093\7)\2\2\u0092")
        buf.write("\u0094\5\30\r\2\u0093\u0092\3\2\2\2\u0093\u0094\3\2\2")
        buf.write("\2\u0094\u0095\3\2\2\2\u0095\u009f\7*\2\2\u0096\u0098")
        buf.write("\5V,\2\u0097\u0096\3\2\2\2\u0097\u0098\3\2\2\2\u0098\u0099")
        buf.write("\3\2\2\2\u0099\u00a0\5N(\2\u009a\u009c\5V,\2\u009b\u009a")
        buf.write("\3\2\2\2\u009b\u009c\3\2\2\2\u009c\u009d\3\2\2\2\u009d")
        buf.write("\u00a0\5R*\2\u009e\u00a0\5V,\2\u009f\u0097\3\2\2\2\u009f")
        buf.write("\u009b\3\2\2\2\u009f\u009e\3\2\2\2\u00a0\25\3\2\2\2\u00a1")
        buf.write("\u00a2\5\f\7\2\u00a2\u00a7\7,\2\2\u00a3\u00a4\7\'\2\2")
        buf.write("\u00a4\u00a5\5\32\16\2\u00a5\u00a6\7(\2\2\u00a6\u00a8")
        buf.write("\3\2\2\2\u00a7\u00a3\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8")
        buf.write("\27\3\2\2\2\u00a9\u00aa\5\26\f\2\u00aa\u00ab\7+\2\2\u00ab")
        buf.write("\u00ac\5\30\r\2\u00ac\u00af\3\2\2\2\u00ad\u00af\5\26\f")
        buf.write("\2\u00ae\u00a9\3\2\2\2\u00ae\u00ad\3\2\2\2\u00af\31\3")
        buf.write("\2\2\2\u00b0\u00b1\7-\2\2\u00b1\u00b2\7+\2\2\u00b2\u00b5")
        buf.write("\5\32\16\2\u00b3\u00b5\7-\2\2\u00b4\u00b0\3\2\2\2\u00b4")
        buf.write("\u00b3\3\2\2\2\u00b5\33\3\2\2\2\u00b6\u00b7\5\36\20\2")
        buf.write("\u00b7\u00b8\7&\2\2\u00b8\u00b9\5\36\20\2\u00b9\u00bc")
        buf.write("\3\2\2\2\u00ba\u00bc\5\36\20\2\u00bb\u00b6\3\2\2\2\u00bb")
        buf.write("\u00ba\3\2\2\2\u00bc\35\3\2\2\2\u00bd\u00be\5 \21\2\u00be")
        buf.write("\u00bf\t\3\2\2\u00bf\u00c0\5 \21\2\u00c0\u00c3\3\2\2\2")
        buf.write("\u00c1\u00c3\5 \21\2\u00c2\u00bd\3\2\2\2\u00c2\u00c1\3")
        buf.write("\2\2\2\u00c3\37\3\2\2\2\u00c4\u00c5\b\21\1\2\u00c5\u00c6")
        buf.write("\5\"\22\2\u00c6\u00cc\3\2\2\2\u00c7\u00c8\f\4\2\2\u00c8")
        buf.write("\u00c9\t\4\2\2\u00c9\u00cb\5\"\22\2\u00ca\u00c7\3\2\2")
        buf.write("\2\u00cb\u00ce\3\2\2\2\u00cc\u00ca\3\2\2\2\u00cc\u00cd")
        buf.write("\3\2\2\2\u00cd!\3\2\2\2\u00ce\u00cc\3\2\2\2\u00cf\u00d0")
        buf.write("\b\22\1\2\u00d0\u00d1\5$\23\2\u00d1\u00d7\3\2\2\2\u00d2")
        buf.write("\u00d3\f\4\2\2\u00d3\u00d4\t\5\2\2\u00d4\u00d6\5$\23\2")
        buf.write("\u00d5\u00d2\3\2\2\2\u00d6\u00d9\3\2\2\2\u00d7\u00d5\3")
        buf.write("\2\2\2\u00d7\u00d8\3\2\2\2\u00d8#\3\2\2\2\u00d9\u00d7")
        buf.write("\3\2\2\2\u00da\u00db\b\23\1\2\u00db\u00dc\5&\24\2\u00dc")
        buf.write("\u00e2\3\2\2\2\u00dd\u00de\f\4\2\2\u00de\u00df\t\6\2\2")
        buf.write("\u00df\u00e1\5&\24\2\u00e0\u00dd\3\2\2\2\u00e1\u00e4\3")
        buf.write("\2\2\2\u00e2\u00e0\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3%")
        buf.write("\3\2\2\2\u00e4\u00e2\3\2\2\2\u00e5\u00e6\7\26\2\2\u00e6")
        buf.write("\u00e9\5&\24\2\u00e7\u00e9\5(\25\2\u00e8\u00e5\3\2\2\2")
        buf.write("\u00e8\u00e7\3\2\2\2\u00e9\'\3\2\2\2\u00ea\u00eb\t\5\2")
        buf.write("\2\u00eb\u00ee\5(\25\2\u00ec\u00ee\5*\26\2\u00ed\u00ea")
        buf.write("\3\2\2\2\u00ed\u00ec\3\2\2\2\u00ee)\3\2\2\2\u00ef\u00f7")
        buf.write("\7,\2\2\u00f0\u00f1\7,\2\2\u00f1\u00f3\7)\2\2\u00f2\u00f4")
        buf.write("\5\64\33\2\u00f3\u00f2\3\2\2\2\u00f3\u00f4\3\2\2\2\u00f4")
        buf.write("\u00f5\3\2\2\2\u00f5\u00f7\7*\2\2\u00f6\u00ef\3\2\2\2")
        buf.write("\u00f6\u00f0\3\2\2\2\u00f7\u00f8\3\2\2\2\u00f8\u00f9\7")
        buf.write("\'\2\2\u00f9\u00fa\5\64\33\2\u00fa\u00fb\7(\2\2\u00fb")
        buf.write("\u00fe\3\2\2\2\u00fc\u00fe\5,\27\2\u00fd\u00f6\3\2\2\2")
        buf.write("\u00fd\u00fc\3\2\2\2\u00fe+\3\2\2\2\u00ff\u0107\7,\2\2")
        buf.write("\u0100\u0107\5\66\34\2\u0101\u0107\5.\30\2\u0102\u0103")
        buf.write("\7)\2\2\u0103\u0104\5\34\17\2\u0104\u0105\7*\2\2\u0105")
        buf.write("\u0107\3\2\2\2\u0106\u00ff\3\2\2\2\u0106\u0100\3\2\2\2")
        buf.write("\u0106\u0101\3\2\2\2\u0106\u0102\3\2\2\2\u0107-\3\2\2")
        buf.write("\2\u0108\u0109\7,\2\2\u0109\u010b\7)\2\2\u010a\u010c\5")
        buf.write("\64\33\2\u010b\u010a\3\2\2\2\u010b\u010c\3\2\2\2\u010c")
        buf.write("\u010d\3\2\2\2\u010d\u010e\7*\2\2\u010e/\3\2\2\2\u010f")
        buf.write("\u0110\5\62\32\2\u0110\u0111\5\60\31\2\u0111\u0114\3\2")
        buf.write("\2\2\u0112\u0114\5\62\32\2\u0113\u010f\3\2\2\2\u0113\u0112")
        buf.write("\3\2\2\2\u0114\61\3\2\2\2\u0115\u0116\7\'\2\2\u0116\u0117")
        buf.write("\5\64\33\2\u0117\u0118\7(\2\2\u0118\63\3\2\2\2\u0119\u011a")
        buf.write("\5\34\17\2\u011a\u011b\7+\2\2\u011b\u011c\5\64\33\2\u011c")
        buf.write("\u011f\3\2\2\2\u011d\u011f\5\34\17\2\u011e\u0119\3\2\2")
        buf.write("\2\u011e\u011d\3\2\2\2\u011f\65\3\2\2\2\u0120\u0126\7")
        buf.write("-\2\2\u0121\u0126\7.\2\2\u0122\u0126\7\3\2\2\u0123\u0126")
        buf.write("\7\4\2\2\u0124\u0126\58\35\2\u0125\u0120\3\2\2\2\u0125")
        buf.write("\u0121\3\2\2\2\u0125\u0122\3\2\2\2\u0125\u0123\3\2\2\2")
        buf.write("\u0125\u0124\3\2\2\2\u0126\67\3\2\2\2\u0127\u0128\7\'")
        buf.write("\2\2\u0128\u0129\5\64\33\2\u0129\u012a\7(\2\2\u012a9\3")
        buf.write("\2\2\2\u012b\u0135\5<\37\2\u012c\u0135\5> \2\u012d\u0135")
        buf.write("\5B\"\2\u012e\u0135\5H%\2\u012f\u0135\5J&\2\u0130\u0135")
        buf.write("\5L\'\2\u0131\u0135\5N(\2\u0132\u0135\5P)\2\u0133\u0135")
        buf.write("\5R*\2\u0134\u012b\3\2\2\2\u0134\u012c\3\2\2\2\u0134\u012d")
        buf.write("\3\2\2\2\u0134\u012e\3\2\2\2\u0134\u012f\3\2\2\2\u0134")
        buf.write("\u0130\3\2\2\2\u0134\u0131\3\2\2\2\u0134\u0132\3\2\2\2")
        buf.write("\u0134\u0133\3\2\2\2\u0135;\3\2\2\2\u0136\u0137\5\b\5")
        buf.write("\2\u0137\u0138\5V,\2\u0138=\3\2\2\2\u0139\u013a\5@!\2")
        buf.write("\u013a\u013b\7\37\2\2\u013b\u013c\5\34\17\2\u013c\u013d")
        buf.write("\5V,\2\u013d?\3\2\2\2\u013e\u013f\7,\2\2\u013f\u0140\7")
        buf.write("\'\2\2\u0140\u0141\5\64\33\2\u0141\u0142\7(\2\2\u0142")
        buf.write("\u0145\3\2\2\2\u0143\u0145\7,\2\2\u0144\u013e\3\2\2\2")
        buf.write("\u0144\u0143\3\2\2\2\u0145A\3\2\2\2\u0146\u0147\7\21\2")
        buf.write("\2\u0147\u0148\7)\2\2\u0148\u0149\5\34\17\2\u0149\u014b")
        buf.write("\7*\2\2\u014a\u014c\5V,\2\u014b\u014a\3\2\2\2\u014b\u014c")
        buf.write("\3\2\2\2\u014c\u014f\3\2\2\2\u014d\u0150\5:\36\2\u014e")
        buf.write("\u0150\5R*\2\u014f\u014d\3\2\2\2\u014f\u014e\3\2\2\2\u0150")
        buf.write("\u0151\3\2\2\2\u0151\u0153\5D#\2\u0152\u0154\5F$\2\u0153")
        buf.write("\u0152\3\2\2\2\u0153\u0154\3\2\2\2\u0154C\3\2\2\2\u0155")
        buf.write("\u0156\7\23\2\2\u0156\u0157\7)\2\2\u0157\u0158\5\34\17")
        buf.write("\2\u0158\u015a\7*\2\2\u0159\u015b\5V,\2\u015a\u0159\3")
        buf.write("\2\2\2\u015a\u015b\3\2\2\2\u015b\u015e\3\2\2\2\u015c\u015f")
        buf.write("\5:\36\2\u015d\u015f\5R*\2\u015e\u015c\3\2\2\2\u015e\u015d")
        buf.write("\3\2\2\2\u015f\u0160\3\2\2\2\u0160\u0161\5D#\2\u0161\u0164")
        buf.write("\3\2\2\2\u0162\u0164\3\2\2\2\u0163\u0155\3\2\2\2\u0163")
        buf.write("\u0162\3\2\2\2\u0164E\3\2\2\2\u0165\u0167\7\22\2\2\u0166")
        buf.write("\u0168\5V,\2\u0167\u0166\3\2\2\2\u0167\u0168\3\2\2\2\u0168")
        buf.write("\u016b\3\2\2\2\u0169\u016c\5:\36\2\u016a\u016c\5R*\2\u016b")
        buf.write("\u0169\3\2\2\2\u016b\u016a\3\2\2\2\u016cG\3\2\2\2\u016d")
        buf.write("\u016e\7\f\2\2\u016e\u016f\7,\2\2\u016f\u0170\7\r\2\2")
        buf.write("\u0170\u0171\5\34\17\2\u0171\u0172\7\16\2\2\u0172\u0174")
        buf.write("\5\34\17\2\u0173\u0175\5V,\2\u0174\u0173\3\2\2\2\u0174")
        buf.write("\u0175\3\2\2\2\u0175\u0178\3\2\2\2\u0176\u0179\5:\36\2")
        buf.write("\u0177\u0179\5R*\2\u0178\u0176\3\2\2\2\u0178\u0177\3\2")
        buf.write("\2\2\u0179I\3\2\2\2\u017a\u017b\7\17\2\2\u017b\u017c\5")
        buf.write("V,\2\u017cK\3\2\2\2\u017d\u017e\7\20\2\2\u017e\u017f\5")
        buf.write("V,\2\u017fM\3\2\2\2\u0180\u0182\7\b\2\2\u0181\u0183\5")
        buf.write("\34\17\2\u0182\u0181\3\2\2\2\u0182\u0183\3\2\2\2\u0183")
        buf.write("\u0184\3\2\2\2\u0184\u0185\5V,\2\u0185O\3\2\2\2\u0186")
        buf.write("\u0187\7,\2\2\u0187\u0189\7)\2\2\u0188\u018a\5\64\33\2")
        buf.write("\u0189\u0188\3\2\2\2\u0189\u018a\3\2\2\2\u018a\u018b\3")
        buf.write("\2\2\2\u018b\u018c\7*\2\2\u018c\u018d\5V,\2\u018dQ\3\2")
        buf.write("\2\2\u018e\u018f\7\24\2\2\u018f\u0190\5V,\2\u0190\u0191")
        buf.write("\5T+\2\u0191\u0192\7\25\2\2\u0192\u0193\5V,\2\u0193S\3")
        buf.write("\2\2\2\u0194\u0196\5:\36\2\u0195\u0197\5V,\2\u0196\u0195")
        buf.write("\3\2\2\2\u0196\u0197\3\2\2\2\u0197\u0198\3\2\2\2\u0198")
        buf.write("\u0199\5T+\2\u0199\u019c\3\2\2\2\u019a\u019c\3\2\2\2\u019b")
        buf.write("\u0194\3\2\2\2\u019b\u019a\3\2\2\2\u019cU\3\2\2\2\u019d")
        buf.write("\u019f\7/\2\2\u019e\u019d\3\2\2\2\u019f\u01a0\3\2\2\2")
        buf.write("\u01a0\u019e\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1W\3\2\2")
        buf.write("\2\60[ekq~\u0087\u008d\u0093\u0097\u009b\u009f\u00a7\u00ae")
        buf.write("\u00b4\u00bb\u00c2\u00cc\u00d7\u00e2\u00e8\u00ed\u00f3")
        buf.write("\u00f6\u00fd\u0106\u010b\u0113\u011e\u0125\u0134\u0144")
        buf.write("\u014b\u014f\u0153\u015a\u015e\u0163\u0167\u016b\u0174")
        buf.write("\u0178\u0182\u0189\u0196\u019b\u01a0")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'true'", "'false'", "'number'", "'bool'", 
                     "'string'", "'return'", "'var'", "'dynamic'", "'func'", 
                     "'for'", "'until'", "'by'", "'break'", "'continue'", 
                     "'if'", "'else'", "'elif'", "'begin'", "'end'", "'not'", 
                     "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'='", "'<-'", "'!='", "'<'", "'<='", "'>'", "'>='", 
                     "'=='", "'...'", "'['", "']'", "'('", "')'", "','" ]

    symbolicNames = [ "<INVALID>", "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", 
                      "RETURN", "VAR", "DYNAMIC", "FUNCTION", "FOR", "UNTIL", 
                      "BY", "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", 
                      "END", "NOT", "AND", "OR", "ADD", "SUB", "MULTI", 
                      "DIV", "MOD", "EQUAL", "ASS1", "NOT_EQUAL", "LESS_THAN", 
                      "LESS_EQUAL", "GREATER_THAN", "GREATER_EQUAL", "COMPARE", 
                      "CONCAT", "LBRACKET", "RBRACKET", "LPAREN", "RPAREN", 
                      "COMMA", "IDEN", "NUMBERLIT", "STRINGLIT", "NEWLINE", 
                      "COMMENTS", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_list_decl = 1
    RULE_decl = 2
    RULE_list_vardecl = 3
    RULE_imp_var = 4
    RULE_vartype = 5
    RULE_keyw_var = 6
    RULE_arr_keyw_var = 7
    RULE_dyna_var = 8
    RULE_function = 9
    RULE_parameter = 10
    RULE_list_prameters = 11
    RULE_list_NUMBERLIT = 12
    RULE_expr = 13
    RULE_relational_expr = 14
    RULE_logical_expr = 15
    RULE_adding_expr = 16
    RULE_multiplying_expr = 17
    RULE_not_expr = 18
    RULE_sign_expr = 19
    RULE_indexoper_expr = 20
    RULE_final_expr = 21
    RULE_function_call = 22
    RULE_list_index_operators = 23
    RULE_index_operator = 24
    RULE_list_expression = 25
    RULE_literal = 26
    RULE_array_literal = 27
    RULE_statement = 28
    RULE_decl_stmt = 29
    RULE_ass_stmt = 30
    RULE_lhs = 31
    RULE_if_stmt = 32
    RULE_elif_stmt = 33
    RULE_else_stmt = 34
    RULE_for_stmt = 35
    RULE_break_stmt = 36
    RULE_continue_stmt = 37
    RULE_return_stmt = 38
    RULE_call_stmt = 39
    RULE_block_stmt = 40
    RULE_list_stmt = 41
    RULE_ignore = 42

    ruleNames =  [ "program", "list_decl", "decl", "list_vardecl", "imp_var", 
                   "vartype", "keyw_var", "arr_keyw_var", "dyna_var", "function", 
                   "parameter", "list_prameters", "list_NUMBERLIT", "expr", 
                   "relational_expr", "logical_expr", "adding_expr", "multiplying_expr", 
                   "not_expr", "sign_expr", "indexoper_expr", "final_expr", 
                   "function_call", "list_index_operators", "index_operator", 
                   "list_expression", "literal", "array_literal", "statement", 
                   "decl_stmt", "ass_stmt", "lhs", "if_stmt", "elif_stmt", 
                   "else_stmt", "for_stmt", "break_stmt", "continue_stmt", 
                   "return_stmt", "call_stmt", "block_stmt", "list_stmt", 
                   "ignore" ]

    EOF = Token.EOF
    TRUE=1
    FALSE=2
    NUMBER=3
    BOOL=4
    STRING=5
    RETURN=6
    VAR=7
    DYNAMIC=8
    FUNCTION=9
    FOR=10
    UNTIL=11
    BY=12
    BREAK=13
    CONTINUE=14
    IF=15
    ELSE=16
    ELIF=17
    BEGIN=18
    END=19
    NOT=20
    AND=21
    OR=22
    ADD=23
    SUB=24
    MULTI=25
    DIV=26
    MOD=27
    EQUAL=28
    ASS1=29
    NOT_EQUAL=30
    LESS_THAN=31
    LESS_EQUAL=32
    GREATER_THAN=33
    GREATER_EQUAL=34
    COMPARE=35
    CONCAT=36
    LBRACKET=37
    RBRACKET=38
    LPAREN=39
    RPAREN=40
    COMMA=41
    IDEN=42
    NUMBERLIT=43
    STRINGLIT=44
    NEWLINE=45
    COMMENTS=46
    WS=47
    ERROR_CHAR=48
    UNCLOSE_STRING=49
    ILLEGAL_ESCAPE=50

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_decl(self):
            return self.getTypedRuleContext(ZCodeParser.List_declContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NEWLINE:
                self.state = 86
                self.match(ZCodeParser.NEWLINE)
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 92
            self.list_decl()
            self.state = 93
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(ZCodeParser.DeclContext,0)


        def list_decl(self):
            return self.getTypedRuleContext(ZCodeParser.List_declContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_list_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_decl" ):
                return visitor.visitList_decl(self)
            else:
                return visitor.visitChildren(self)




    def list_decl(self):

        localctx = ZCodeParser.List_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_list_decl)
        try:
            self.state = 99
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.decl()
                self.state = 96
                self.list_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 98
                self.decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function(self):
            return self.getTypedRuleContext(ZCodeParser.FunctionContext,0)


        def list_vardecl(self):
            return self.getTypedRuleContext(ZCodeParser.List_vardeclContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = ZCodeParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 105
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.FUNCTION]:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                self.function()
                pass
            elif token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                self.list_vardecl()
                self.state = 103
                self.ignore()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_vardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def imp_var(self):
            return self.getTypedRuleContext(ZCodeParser.Imp_varContext,0)


        def keyw_var(self):
            return self.getTypedRuleContext(ZCodeParser.Keyw_varContext,0)


        def arr_keyw_var(self):
            return self.getTypedRuleContext(ZCodeParser.Arr_keyw_varContext,0)


        def dyna_var(self):
            return self.getTypedRuleContext(ZCodeParser.Dyna_varContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_list_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_vardecl" ):
                return visitor.visitList_vardecl(self)
            else:
                return visitor.visitChildren(self)




    def list_vardecl(self):

        localctx = ZCodeParser.List_vardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_list_vardecl)
        try:
            self.state = 111
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 107
                self.imp_var()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 108
                self.keyw_var()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 109
                self.arr_keyw_var()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 110
                self.dyna_var()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Imp_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def IDEN(self):
            return self.getToken(ZCodeParser.IDEN, 0)

        def ASS1(self):
            return self.getToken(ZCodeParser.ASS1, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_imp_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImp_var" ):
                return visitor.visitImp_var(self)
            else:
                return visitor.visitChildren(self)




    def imp_var(self):

        localctx = ZCodeParser.Imp_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_imp_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(ZCodeParser.VAR)
            self.state = 114
            self.match(ZCodeParser.IDEN)
            self.state = 115
            self.match(ZCodeParser.ASS1)
            self.state = 116
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VartypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOL(self):
            return self.getToken(ZCodeParser.BOOL, 0)

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_vartype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVartype" ):
                return visitor.visitVartype(self)
            else:
                return visitor.visitChildren(self)




    def vartype(self):

        localctx = ZCodeParser.VartypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_vartype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Keyw_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vartype(self):
            return self.getTypedRuleContext(ZCodeParser.VartypeContext,0)


        def IDEN(self):
            return self.getToken(ZCodeParser.IDEN, 0)

        def ASS1(self):
            return self.getToken(ZCodeParser.ASS1, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_keyw_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKeyw_var" ):
                return visitor.visitKeyw_var(self)
            else:
                return visitor.visitChildren(self)




    def keyw_var(self):

        localctx = ZCodeParser.Keyw_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_keyw_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.vartype()
            self.state = 121
            self.match(ZCodeParser.IDEN)
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASS1:
                self.state = 122
                self.match(ZCodeParser.ASS1)
                self.state = 123
                self.expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_keyw_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vartype(self):
            return self.getTypedRuleContext(ZCodeParser.VartypeContext,0)


        def IDEN(self):
            return self.getToken(ZCodeParser.IDEN, 0)

        def LBRACKET(self):
            return self.getToken(ZCodeParser.LBRACKET, 0)

        def list_NUMBERLIT(self):
            return self.getTypedRuleContext(ZCodeParser.List_NUMBERLITContext,0)


        def RBRACKET(self):
            return self.getToken(ZCodeParser.RBRACKET, 0)

        def ASS1(self):
            return self.getToken(ZCodeParser.ASS1, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arr_keyw_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_keyw_var" ):
                return visitor.visitArr_keyw_var(self)
            else:
                return visitor.visitChildren(self)




    def arr_keyw_var(self):

        localctx = ZCodeParser.Arr_keyw_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_arr_keyw_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.vartype()
            self.state = 127
            self.match(ZCodeParser.IDEN)
            self.state = 128
            self.match(ZCodeParser.LBRACKET)
            self.state = 129
            self.list_NUMBERLIT()
            self.state = 130
            self.match(ZCodeParser.RBRACKET)
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASS1:
                self.state = 131
                self.match(ZCodeParser.ASS1)
                self.state = 132
                self.expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dyna_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def IDEN(self):
            return self.getToken(ZCodeParser.IDEN, 0)

        def ASS1(self):
            return self.getToken(ZCodeParser.ASS1, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_dyna_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDyna_var" ):
                return visitor.visitDyna_var(self)
            else:
                return visitor.visitChildren(self)




    def dyna_var(self):

        localctx = ZCodeParser.Dyna_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_dyna_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(ZCodeParser.DYNAMIC)
            self.state = 136
            self.match(ZCodeParser.IDEN)
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASS1:
                self.state = 137
                self.match(ZCodeParser.ASS1)
                self.state = 138
                self.expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(ZCodeParser.FUNCTION, 0)

        def IDEN(self):
            return self.getToken(ZCodeParser.IDEN, 0)

        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def return_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Return_stmtContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Block_stmtContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def list_prameters(self):
            return self.getTypedRuleContext(ZCodeParser.List_prametersContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_function

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = ZCodeParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(ZCodeParser.FUNCTION)
            self.state = 142
            self.match(ZCodeParser.IDEN)
            self.state = 143
            self.match(ZCodeParser.LPAREN)
            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0):
                self.state = 144
                self.list_prameters()


            self.state = 147
            self.match(ZCodeParser.RPAREN)
            self.state = 157
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 149
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 148
                    self.ignore()


                self.state = 151
                self.return_stmt()
                pass

            elif la_ == 2:
                self.state = 153
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 152
                    self.ignore()


                self.state = 155
                self.block_stmt()
                pass

            elif la_ == 3:
                self.state = 156
                self.ignore()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vartype(self):
            return self.getTypedRuleContext(ZCodeParser.VartypeContext,0)


        def IDEN(self):
            return self.getToken(ZCodeParser.IDEN, 0)

        def LBRACKET(self):
            return self.getToken(ZCodeParser.LBRACKET, 0)

        def list_NUMBERLIT(self):
            return self.getTypedRuleContext(ZCodeParser.List_NUMBERLITContext,0)


        def RBRACKET(self):
            return self.getToken(ZCodeParser.RBRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_parameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = ZCodeParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.vartype()
            self.state = 160
            self.match(ZCodeParser.IDEN)
            self.state = 165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.LBRACKET:
                self.state = 161
                self.match(ZCodeParser.LBRACKET)
                self.state = 162
                self.list_NUMBERLIT()
                self.state = 163
                self.match(ZCodeParser.RBRACKET)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_prametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self):
            return self.getTypedRuleContext(ZCodeParser.ParameterContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def list_prameters(self):
            return self.getTypedRuleContext(ZCodeParser.List_prametersContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_list_prameters

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_prameters" ):
                return visitor.visitList_prameters(self)
            else:
                return visitor.visitChildren(self)




    def list_prameters(self):

        localctx = ZCodeParser.List_prametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_list_prameters)
        try:
            self.state = 172
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.parameter()
                self.state = 168
                self.match(ZCodeParser.COMMA)
                self.state = 169
                self.list_prameters()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 171
                self.parameter()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_NUMBERLITContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBERLIT(self):
            return self.getToken(ZCodeParser.NUMBERLIT, 0)

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def list_NUMBERLIT(self):
            return self.getTypedRuleContext(ZCodeParser.List_NUMBERLITContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_list_NUMBERLIT

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_NUMBERLIT" ):
                return visitor.visitList_NUMBERLIT(self)
            else:
                return visitor.visitChildren(self)




    def list_NUMBERLIT(self):

        localctx = ZCodeParser.List_NUMBERLITContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_list_NUMBERLIT)
        try:
            self.state = 178
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.match(ZCodeParser.NUMBERLIT)
                self.state = 175
                self.match(ZCodeParser.COMMA)
                self.state = 176
                self.list_NUMBERLIT()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 177
                self.match(ZCodeParser.NUMBERLIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relational_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Relational_exprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Relational_exprContext,i)


        def CONCAT(self):
            return self.getToken(ZCodeParser.CONCAT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = ZCodeParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_expr)
        try:
            self.state = 185
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 180
                self.relational_expr()
                self.state = 181
                self.match(ZCodeParser.CONCAT)
                self.state = 182
                self.relational_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 184
                self.relational_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relational_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logical_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Logical_exprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Logical_exprContext,i)


        def COMPARE(self):
            return self.getToken(ZCodeParser.COMPARE, 0)

        def EQUAL(self):
            return self.getToken(ZCodeParser.EQUAL, 0)

        def LESS_THAN(self):
            return self.getToken(ZCodeParser.LESS_THAN, 0)

        def GREATER_THAN(self):
            return self.getToken(ZCodeParser.GREATER_THAN, 0)

        def LESS_EQUAL(self):
            return self.getToken(ZCodeParser.LESS_EQUAL, 0)

        def GREATER_EQUAL(self):
            return self.getToken(ZCodeParser.GREATER_EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(ZCodeParser.NOT_EQUAL, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_relational_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational_expr" ):
                return visitor.visitRelational_expr(self)
            else:
                return visitor.visitChildren(self)




    def relational_expr(self):

        localctx = ZCodeParser.Relational_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_relational_expr)
        self._la = 0 # Token type
        try:
            self.state = 192
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 187
                self.logical_expr(0)
                self.state = 188
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.EQUAL) | (1 << ZCodeParser.NOT_EQUAL) | (1 << ZCodeParser.LESS_THAN) | (1 << ZCodeParser.LESS_EQUAL) | (1 << ZCodeParser.GREATER_THAN) | (1 << ZCodeParser.GREATER_EQUAL) | (1 << ZCodeParser.COMPARE))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 189
                self.logical_expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 191
                self.logical_expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logical_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def adding_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Adding_exprContext,0)


        def logical_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Logical_exprContext,0)


        def AND(self):
            return self.getToken(ZCodeParser.AND, 0)

        def OR(self):
            return self.getToken(ZCodeParser.OR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_logical_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_expr" ):
                return visitor.visitLogical_expr(self)
            else:
                return visitor.visitChildren(self)



    def logical_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Logical_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_logical_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.adding_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 202
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Logical_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_expr)
                    self.state = 197
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 198
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 199
                    self.adding_expr(0) 
                self.state = 204
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Adding_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplying_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Multiplying_exprContext,0)


        def adding_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Adding_exprContext,0)


        def ADD(self):
            return self.getToken(ZCodeParser.ADD, 0)

        def SUB(self):
            return self.getToken(ZCodeParser.SUB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_adding_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdding_expr" ):
                return visitor.visitAdding_expr(self)
            else:
                return visitor.visitChildren(self)



    def adding_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Adding_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_adding_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.multiplying_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 213
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Adding_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_adding_expr)
                    self.state = 208
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 209
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.ADD or _la==ZCodeParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 210
                    self.multiplying_expr(0) 
                self.state = 215
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Multiplying_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def not_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Not_exprContext,0)


        def multiplying_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Multiplying_exprContext,0)


        def MULTI(self):
            return self.getToken(ZCodeParser.MULTI, 0)

        def DIV(self):
            return self.getToken(ZCodeParser.DIV, 0)

        def MOD(self):
            return self.getToken(ZCodeParser.MOD, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_multiplying_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplying_expr" ):
                return visitor.visitMultiplying_expr(self)
            else:
                return visitor.visitChildren(self)



    def multiplying_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Multiplying_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_multiplying_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.not_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 224
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Multiplying_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplying_expr)
                    self.state = 219
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 220
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MULTI) | (1 << ZCodeParser.DIV) | (1 << ZCodeParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 221
                    self.not_expr() 
                self.state = 226
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Not_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(ZCodeParser.NOT, 0)

        def not_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Not_exprContext,0)


        def sign_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Sign_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_not_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNot_expr" ):
                return visitor.visitNot_expr(self)
            else:
                return visitor.visitChildren(self)




    def not_expr(self):

        localctx = ZCodeParser.Not_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_not_expr)
        try:
            self.state = 230
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 227
                self.match(ZCodeParser.NOT)
                self.state = 228
                self.not_expr()
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.ADD, ZCodeParser.SUB, ZCodeParser.LBRACKET, ZCodeParser.LPAREN, ZCodeParser.IDEN, ZCodeParser.NUMBERLIT, ZCodeParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 229
                self.sign_expr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sign_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sign_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Sign_exprContext,0)


        def ADD(self):
            return self.getToken(ZCodeParser.ADD, 0)

        def SUB(self):
            return self.getToken(ZCodeParser.SUB, 0)

        def indexoper_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Indexoper_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_sign_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSign_expr" ):
                return visitor.visitSign_expr(self)
            else:
                return visitor.visitChildren(self)




    def sign_expr(self):

        localctx = ZCodeParser.Sign_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_sign_expr)
        self._la = 0 # Token type
        try:
            self.state = 235
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.ADD, ZCodeParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                _la = self._input.LA(1)
                if not(_la==ZCodeParser.ADD or _la==ZCodeParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 233
                self.sign_expr()
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.LBRACKET, ZCodeParser.LPAREN, ZCodeParser.IDEN, ZCodeParser.NUMBERLIT, ZCodeParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 234
                self.indexoper_expr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Indexoper_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(ZCodeParser.LBRACKET, 0)

        def list_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.List_expressionContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.List_expressionContext,i)


        def RBRACKET(self):
            return self.getToken(ZCodeParser.RBRACKET, 0)

        def IDEN(self):
            return self.getToken(ZCodeParser.IDEN, 0)

        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def final_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Final_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_indexoper_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexoper_expr" ):
                return visitor.visitIndexoper_expr(self)
            else:
                return visitor.visitChildren(self)




    def indexoper_expr(self):

        localctx = ZCodeParser.Indexoper_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_indexoper_expr)
        self._la = 0 # Token type
        try:
            self.state = 251
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 244
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                if la_ == 1:
                    self.state = 237
                    self.match(ZCodeParser.IDEN)
                    pass

                elif la_ == 2:
                    self.state = 238
                    self.match(ZCodeParser.IDEN)
                    self.state = 239
                    self.match(ZCodeParser.LPAREN)
                    self.state = 241
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TRUE) | (1 << ZCodeParser.FALSE) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.ADD) | (1 << ZCodeParser.SUB) | (1 << ZCodeParser.LBRACKET) | (1 << ZCodeParser.LPAREN) | (1 << ZCodeParser.IDEN) | (1 << ZCodeParser.NUMBERLIT) | (1 << ZCodeParser.STRINGLIT))) != 0):
                        self.state = 240
                        self.list_expression()


                    self.state = 243
                    self.match(ZCodeParser.RPAREN)
                    pass


                self.state = 246
                self.match(ZCodeParser.LBRACKET)
                self.state = 247
                self.list_expression()
                self.state = 248
                self.match(ZCodeParser.RBRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 250
                self.final_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Final_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDEN(self):
            return self.getToken(ZCodeParser.IDEN, 0)

        def literal(self):
            return self.getTypedRuleContext(ZCodeParser.LiteralContext,0)


        def function_call(self):
            return self.getTypedRuleContext(ZCodeParser.Function_callContext,0)


        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_final_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFinal_expr" ):
                return visitor.visitFinal_expr(self)
            else:
                return visitor.visitChildren(self)




    def final_expr(self):

        localctx = ZCodeParser.Final_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_final_expr)
        try:
            self.state = 260
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 253
                self.match(ZCodeParser.IDEN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 254
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 255
                self.function_call()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 256
                self.match(ZCodeParser.LPAREN)
                self.state = 257
                self.expr()
                self.state = 258
                self.match(ZCodeParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDEN(self):
            return self.getToken(ZCodeParser.IDEN, 0)

        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def list_expression(self):
            return self.getTypedRuleContext(ZCodeParser.List_expressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_function_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call" ):
                return visitor.visitFunction_call(self)
            else:
                return visitor.visitChildren(self)




    def function_call(self):

        localctx = ZCodeParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.match(ZCodeParser.IDEN)
            self.state = 263
            self.match(ZCodeParser.LPAREN)
            self.state = 265
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TRUE) | (1 << ZCodeParser.FALSE) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.ADD) | (1 << ZCodeParser.SUB) | (1 << ZCodeParser.LBRACKET) | (1 << ZCodeParser.LPAREN) | (1 << ZCodeParser.IDEN) | (1 << ZCodeParser.NUMBERLIT) | (1 << ZCodeParser.STRINGLIT))) != 0):
                self.state = 264
                self.list_expression()


            self.state = 267
            self.match(ZCodeParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_index_operatorsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def index_operator(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operatorContext,0)


        def list_index_operators(self):
            return self.getTypedRuleContext(ZCodeParser.List_index_operatorsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_list_index_operators

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_index_operators" ):
                return visitor.visitList_index_operators(self)
            else:
                return visitor.visitChildren(self)




    def list_index_operators(self):

        localctx = ZCodeParser.List_index_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_list_index_operators)
        try:
            self.state = 273
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 269
                self.index_operator()
                self.state = 270
                self.list_index_operators()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 272
                self.index_operator()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(ZCodeParser.LBRACKET, 0)

        def list_expression(self):
            return self.getTypedRuleContext(ZCodeParser.List_expressionContext,0)


        def RBRACKET(self):
            return self.getToken(ZCodeParser.RBRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_index_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operator" ):
                return visitor.visitIndex_operator(self)
            else:
                return visitor.visitChildren(self)




    def index_operator(self):

        localctx = ZCodeParser.Index_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_index_operator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.match(ZCodeParser.LBRACKET)
            self.state = 276
            self.list_expression()
            self.state = 277
            self.match(ZCodeParser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def list_expression(self):
            return self.getTypedRuleContext(ZCodeParser.List_expressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_list_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_expression" ):
                return visitor.visitList_expression(self)
            else:
                return visitor.visitChildren(self)




    def list_expression(self):

        localctx = ZCodeParser.List_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_list_expression)
        try:
            self.state = 284
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 279
                self.expr()
                self.state = 280
                self.match(ZCodeParser.COMMA)
                self.state = 281
                self.list_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 283
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBERLIT(self):
            return self.getToken(ZCodeParser.NUMBERLIT, 0)

        def STRINGLIT(self):
            return self.getToken(ZCodeParser.STRINGLIT, 0)

        def TRUE(self):
            return self.getToken(ZCodeParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(ZCodeParser.FALSE, 0)

        def array_literal(self):
            return self.getTypedRuleContext(ZCodeParser.Array_literalContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = ZCodeParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_literal)
        try:
            self.state = 291
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBERLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 286
                self.match(ZCodeParser.NUMBERLIT)
                pass
            elif token in [ZCodeParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 287
                self.match(ZCodeParser.STRINGLIT)
                pass
            elif token in [ZCodeParser.TRUE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 288
                self.match(ZCodeParser.TRUE)
                pass
            elif token in [ZCodeParser.FALSE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 289
                self.match(ZCodeParser.FALSE)
                pass
            elif token in [ZCodeParser.LBRACKET]:
                self.enterOuterAlt(localctx, 5)
                self.state = 290
                self.array_literal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(ZCodeParser.LBRACKET, 0)

        def list_expression(self):
            return self.getTypedRuleContext(ZCodeParser.List_expressionContext,0)


        def RBRACKET(self):
            return self.getToken(ZCodeParser.RBRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal" ):
                return visitor.visitArray_literal(self)
            else:
                return visitor.visitChildren(self)




    def array_literal(self):

        localctx = ZCodeParser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.match(ZCodeParser.LBRACKET)
            self.state = 294
            self.list_expression()
            self.state = 295
            self.match(ZCodeParser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Decl_stmtContext,0)


        def ass_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Ass_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.For_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Continue_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Return_stmtContext,0)


        def call_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Call_stmtContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ZCodeParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_statement)
        try:
            self.state = 306
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 297
                self.decl_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 298
                self.ass_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 299
                self.if_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 300
                self.for_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 301
                self.break_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 302
                self.continue_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 303
                self.return_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 304
                self.call_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 305
                self.block_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_vardecl(self):
            return self.getTypedRuleContext(ZCodeParser.List_vardeclContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decl_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_stmt" ):
                return visitor.visitDecl_stmt(self)
            else:
                return visitor.visitChildren(self)




    def decl_stmt(self):

        localctx = ZCodeParser.Decl_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_decl_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.list_vardecl()
            self.state = 309
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ass_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(ZCodeParser.LhsContext,0)


        def ASS1(self):
            return self.getToken(ZCodeParser.ASS1, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_ass_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAss_stmt" ):
                return visitor.visitAss_stmt(self)
            else:
                return visitor.visitChildren(self)




    def ass_stmt(self):

        localctx = ZCodeParser.Ass_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_ass_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            self.lhs()
            self.state = 312
            self.match(ZCodeParser.ASS1)
            self.state = 313
            self.expr()
            self.state = 314
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDEN(self):
            return self.getToken(ZCodeParser.IDEN, 0)

        def LBRACKET(self):
            return self.getToken(ZCodeParser.LBRACKET, 0)

        def list_expression(self):
            return self.getTypedRuleContext(ZCodeParser.List_expressionContext,0)


        def RBRACKET(self):
            return self.getToken(ZCodeParser.RBRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = ZCodeParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_lhs)
        try:
            self.state = 322
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 316
                self.match(ZCodeParser.IDEN)
                self.state = 317
                self.match(ZCodeParser.LBRACKET)
                self.state = 318
                self.list_expression()
                self.state = 319
                self.match(ZCodeParser.RBRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 321
                self.match(ZCodeParser.IDEN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ZCodeParser.IF, 0)

        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def elif_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_stmtContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Block_stmtContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def else_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Else_stmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = ZCodeParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.match(ZCodeParser.IF)
            self.state = 325
            self.match(ZCodeParser.LPAREN)
            self.state = 326
            self.expr()
            self.state = 327
            self.match(ZCodeParser.RPAREN)
            self.state = 329
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 328
                self.ignore()


            self.state = 333
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 331
                self.statement()
                pass

            elif la_ == 2:
                self.state = 332
                self.block_stmt()
                pass


            self.state = 335
            self.elif_stmt()
            self.state = 337
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 336
                self.else_stmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def elif_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_stmtContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Block_stmtContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_stmt" ):
                return visitor.visitElif_stmt(self)
            else:
                return visitor.visitChildren(self)




    def elif_stmt(self):

        localctx = ZCodeParser.Elif_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_elif_stmt)
        self._la = 0 # Token type
        try:
            self.state = 353
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 339
                self.match(ZCodeParser.ELIF)
                self.state = 340
                self.match(ZCodeParser.LPAREN)
                self.state = 341
                self.expr()
                self.state = 342
                self.match(ZCodeParser.RPAREN)

                self.state = 344
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 343
                    self.ignore()


                self.state = 348
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
                if la_ == 1:
                    self.state = 346
                    self.statement()
                    pass

                elif la_ == 2:
                    self.state = 347
                    self.block_stmt()
                    pass


                self.state = 350
                self.elif_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Block_stmtContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_else_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_stmt" ):
                return visitor.visitElse_stmt(self)
            else:
                return visitor.visitChildren(self)




    def else_stmt(self):

        localctx = ZCodeParser.Else_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_else_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            self.match(ZCodeParser.ELSE)
            self.state = 357
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 356
                self.ignore()


            self.state = 361
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.state = 359
                self.statement()
                pass

            elif la_ == 2:
                self.state = 360
                self.block_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ZCodeParser.FOR, 0)

        def IDEN(self):
            return self.getToken(ZCodeParser.IDEN, 0)

        def UNTIL(self):
            return self.getToken(ZCodeParser.UNTIL, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExprContext,i)


        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Block_stmtContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = ZCodeParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_for_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            self.match(ZCodeParser.FOR)
            self.state = 364
            self.match(ZCodeParser.IDEN)
            self.state = 365
            self.match(ZCodeParser.UNTIL)
            self.state = 366
            self.expr()
            self.state = 367
            self.match(ZCodeParser.BY)
            self.state = 368
            self.expr()
            self.state = 370
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 369
                self.ignore()


            self.state = 374
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.state = 372
                self.statement()
                pass

            elif la_ == 2:
                self.state = 373
                self.block_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(ZCodeParser.BREAK, 0)

        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = ZCodeParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self.match(ZCodeParser.BREAK)
            self.state = 377
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(ZCodeParser.CONTINUE, 0)

        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = ZCodeParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
            self.match(ZCodeParser.CONTINUE)
            self.state = 380
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ZCodeParser.RETURN, 0)

        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = ZCodeParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
            self.match(ZCodeParser.RETURN)
            self.state = 384
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TRUE) | (1 << ZCodeParser.FALSE) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.ADD) | (1 << ZCodeParser.SUB) | (1 << ZCodeParser.LBRACKET) | (1 << ZCodeParser.LPAREN) | (1 << ZCodeParser.IDEN) | (1 << ZCodeParser.NUMBERLIT) | (1 << ZCodeParser.STRINGLIT))) != 0):
                self.state = 383
                self.expr()


            self.state = 386
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDEN(self):
            return self.getToken(ZCodeParser.IDEN, 0)

        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def list_expression(self):
            return self.getTypedRuleContext(ZCodeParser.List_expressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_call_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_stmt" ):
                return visitor.visitCall_stmt(self)
            else:
                return visitor.visitChildren(self)




    def call_stmt(self):

        localctx = ZCodeParser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_call_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            self.match(ZCodeParser.IDEN)
            self.state = 389
            self.match(ZCodeParser.LPAREN)
            self.state = 391
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TRUE) | (1 << ZCodeParser.FALSE) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.ADD) | (1 << ZCodeParser.SUB) | (1 << ZCodeParser.LBRACKET) | (1 << ZCodeParser.LPAREN) | (1 << ZCodeParser.IDEN) | (1 << ZCodeParser.NUMBERLIT) | (1 << ZCodeParser.STRINGLIT))) != 0):
                self.state = 390
                self.list_expression()


            self.state = 393
            self.match(ZCodeParser.RPAREN)
            self.state = 394
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def ignore(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.IgnoreContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.IgnoreContext,i)


        def list_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.List_stmtContext,0)


        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_block_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt" ):
                return visitor.visitBlock_stmt(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt(self):

        localctx = ZCodeParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_block_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 396
            self.match(ZCodeParser.BEGIN)
            self.state = 397
            self.ignore()
            self.state = 398
            self.list_stmt()
            self.state = 399
            self.match(ZCodeParser.END)
            self.state = 400
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def list_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.List_stmtContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_list_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_stmt" ):
                return visitor.visitList_stmt(self)
            else:
                return visitor.visitChildren(self)




    def list_stmt(self):

        localctx = ZCodeParser.List_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_list_stmt)
        self._la = 0 # Token type
        try:
            self.state = 409
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.IDEN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 402
                self.statement()
                self.state = 404
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 403
                    self.ignore()


                self.state = 406
                self.list_stmt()
                pass
            elif token in [ZCodeParser.END]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IgnoreContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_ignore

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIgnore" ):
                return visitor.visitIgnore(self)
            else:
                return visitor.visitChildren(self)




    def ignore(self):

        localctx = ZCodeParser.IgnoreContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_ignore)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 411
                    self.match(ZCodeParser.NEWLINE)

                else:
                    raise NoViableAltException(self)
                self.state = 414 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,45,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[15] = self.logical_expr_sempred
        self._predicates[16] = self.adding_expr_sempred
        self._predicates[17] = self.multiplying_expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def logical_expr_sempred(self, localctx:Logical_exprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def adding_expr_sempred(self, localctx:Adding_exprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def multiplying_expr_sempred(self, localctx:Multiplying_exprContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




