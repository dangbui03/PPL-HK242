# Generated from main/MiniGo.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3F")
        buf.write("\u01bb\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\3\2\7\2b\n\2\f\2\16\2e\13\2\3\2\3\2\3\2")
        buf.write("\3\3\3\3\3\3\7\3m\n\3\f\3\16\3p\13\3\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\5\4x\n\4\3\5\3\5\3\5\3\5\5\5~\n\5\3\5\5\5\u0081")
        buf.write("\n\5\3\5\5\5\u0084\n\5\3\6\3\6\3\6\3\6\3\6\5\6\u008b\n")
        buf.write("\6\3\6\5\6\u008e\n\6\3\7\3\7\3\7\3\7\3\7\7\7\u0095\n\7")
        buf.write("\f\7\16\7\u0098\13\7\3\7\3\7\3\7\3\7\7\7\u009e\n\7\f\7")
        buf.write("\16\7\u00a1\13\7\3\b\3\b\3\b\7\b\u00a6\n\b\f\b\16\b\u00a9")
        buf.write("\13\b\3\b\7\b\u00ac\n\b\f\b\16\b\u00af\13\b\3\t\3\t\3")
        buf.write("\t\3\n\3\n\3\13\3\13\3\13\3\13\7\13\u00ba\n\13\f\13\16")
        buf.write("\13\u00bd\13\13\3\13\3\13\3\13\3\13\7\13\u00c3\n\13\f")
        buf.write("\13\16\13\u00c6\13\13\3\f\3\f\3\r\3\r\3\r\3\r\5\r\u00ce")
        buf.write("\n\r\3\16\3\16\3\16\5\16\u00d3\n\16\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\3\21\3\21\5\21\u00de\n\21\3\22\3\22\3")
        buf.write("\23\3\23\3\23\3\23\7\23\u00e6\n\23\f\23\16\23\u00e9\13")
        buf.write("\23\3\24\3\24\3\24\3\24\3\24\5\24\u00f0\n\24\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\7\25\u00f8\n\25\f\25\16\25\u00fb")
        buf.write("\13\25\3\26\3\26\3\26\3\26\3\26\3\26\7\26\u0103\n\26\f")
        buf.write("\26\16\26\u0106\13\26\3\27\3\27\3\27\3\27\3\27\3\27\7")
        buf.write("\27\u010e\n\27\f\27\16\27\u0111\13\27\3\30\3\30\3\30\3")
        buf.write("\30\3\30\3\30\7\30\u0119\n\30\f\30\16\30\u011c\13\30\3")
        buf.write("\31\3\31\3\31\3\31\3\31\3\31\7\31\u0124\n\31\f\31\16\31")
        buf.write("\u0127\13\31\3\32\3\32\3\32\5\32\u012c\n\32\3\33\3\33")
        buf.write("\3\33\5\33\u0131\n\33\3\33\3\33\3\33\3\33\3\33\3\33\3")
        buf.write("\33\3\33\3\33\5\33\u013c\n\33\3\33\5\33\u013f\n\33\3\33")
        buf.write("\5\33\u0142\n\33\7\33\u0144\n\33\f\33\16\33\u0147\13\33")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\5\34\u014f\n\34\3\35\3")
        buf.write("\35\3\35\3\35\3\35\3\35\3\35\5\35\u0158\n\35\3\36\3\36")
        buf.write("\3\36\5\36\u015d\n\36\3\36\3\36\5\36\u0161\n\36\3\37\3")
        buf.write("\37\5\37\u0165\n\37\3 \3 \3!\3!\5!\u016b\n!\3\"\3\"\3")
        buf.write("#\3#\3$\3$\3$\3%\3%\3%\3%\3%\5%\u0179\n%\3&\3&\3&\3&\3")
        buf.write("&\3&\5&\u0181\n&\3\'\3\'\3\'\5\'\u0186\n\'\3\'\3\'\3(")
        buf.write("\3(\5(\u018c\n(\3(\3(\3(\3(\5(\u0192\n(\5(\u0194\n(\3")
        buf.write(")\3)\3)\3)\3*\3*\3*\3*\3*\3+\3+\5+\u01a1\n+\3+\3+\3+\3")
        buf.write("+\3+\5+\u01a8\n+\3+\3+\5+\u01ac\n+\3,\3,\3-\3-\3.\3.\3")
        buf.write("/\3/\3\60\5\60\u01b7\n\60\3\60\3\60\3\60\2\b(*,.\60\64")
        buf.write("\61\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60")
        buf.write("\62\64\668:<>@BDFHJLNPRTVXZ\\^\2\t\4\2\3\3*.\3\2\34\35")
        buf.write("\3\2\36 \4\2\33\33\35\35\4\2\17\22\30\30\3\2;>\3\2\31")
        buf.write("\32\2\u01c5\2c\3\2\2\2\4i\3\2\2\2\6w\3\2\2\2\by\3\2\2")
        buf.write("\2\n\u0085\3\2\2\2\f\u008f\3\2\2\2\16\u00a2\3\2\2\2\20")
        buf.write("\u00b0\3\2\2\2\22\u00b3\3\2\2\2\24\u00b5\3\2\2\2\26\u00c7")
        buf.write("\3\2\2\2\30\u00cd\3\2\2\2\32\u00d2\3\2\2\2\34\u00d4\3")
        buf.write("\2\2\2\36\u00d7\3\2\2\2 \u00dd\3\2\2\2\"\u00df\3\2\2\2")
        buf.write("$\u00e1\3\2\2\2&\u00ef\3\2\2\2(\u00f1\3\2\2\2*\u00fc\3")
        buf.write("\2\2\2,\u0107\3\2\2\2.\u0112\3\2\2\2\60\u011d\3\2\2\2")
        buf.write("\62\u012b\3\2\2\2\64\u0130\3\2\2\2\66\u014e\3\2\2\28\u0157")
        buf.write("\3\2\2\2:\u0159\3\2\2\2<\u0164\3\2\2\2>\u0166\3\2\2\2")
        buf.write("@\u016a\3\2\2\2B\u016c\3\2\2\2D\u016e\3\2\2\2F\u0170\3")
        buf.write("\2\2\2H\u0178\3\2\2\2J\u0180\3\2\2\2L\u0182\3\2\2\2N\u0193")
        buf.write("\3\2\2\2P\u0195\3\2\2\2R\u0199\3\2\2\2T\u01ab\3\2\2\2")
        buf.write("V\u01ad\3\2\2\2X\u01af\3\2\2\2Z\u01b1\3\2\2\2\\\u01b3")
        buf.write("\3\2\2\2^\u01b6\3\2\2\2`b\5^\60\2a`\3\2\2\2be\3\2\2\2")
        buf.write("ca\3\2\2\2cd\3\2\2\2df\3\2\2\2ec\3\2\2\2fg\5\4\3\2gh\7")
        buf.write("\2\2\3h\3\3\2\2\2in\5\6\4\2jm\5\6\4\2km\5^\60\2lj\3\2")
        buf.write("\2\2lk\3\2\2\2mp\3\2\2\2nl\3\2\2\2no\3\2\2\2o\5\3\2\2")
        buf.write("\2pn\3\2\2\2qx\5\b\5\2rx\5\n\6\2sx\5\26\f\2tx\5\f\7\2")
        buf.write("ux\5\24\13\2vx\5\22\n\2wq\3\2\2\2wr\3\2\2\2ws\3\2\2\2")
        buf.write("wt\3\2\2\2wu\3\2\2\2wv\3\2\2\2x\7\3\2\2\2yz\7\24\2\2z")
        buf.write("}\79\2\2{|\7)\2\2|~\5(\25\2}{\3\2\2\2}~\3\2\2\2~\u0080")
        buf.write("\3\2\2\2\177\u0081\5<\37\2\u0080\177\3\2\2\2\u0080\u0081")
        buf.write("\3\2\2\2\u0081\u0083\3\2\2\2\u0082\u0084\7\67\2\2\u0083")
        buf.write("\u0082\3\2\2\2\u0083\u0084\3\2\2\2\u0084\t\3\2\2\2\u0085")
        buf.write("\u0086\7\23\2\2\u0086\u0087\79\2\2\u0087\u0088\7)\2\2")
        buf.write("\u0088\u008a\5(\25\2\u0089\u008b\5<\37\2\u008a\u0089\3")
        buf.write("\2\2\2\u008a\u008b\3\2\2\2\u008b\u008d\3\2\2\2\u008c\u008e")
        buf.write("\7\67\2\2\u008d\u008c\3\2\2\2\u008d\u008e\3\2\2\2\u008e")
        buf.write("\13\3\2\2\2\u008f\u0090\7\f\2\2\u0090\u0091\79\2\2\u0091")
        buf.write("\u0092\7\r\2\2\u0092\u0096\7\63\2\2\u0093\u0095\5^\60")
        buf.write("\2\u0094\u0093\3\2\2\2\u0095\u0098\3\2\2\2\u0096\u0094")
        buf.write("\3\2\2\2\u0096\u0097\3\2\2\2\u0097\u0099\3\2\2\2\u0098")
        buf.write("\u0096\3\2\2\2\u0099\u009a\5\16\b\2\u009a\u009b\7\64\2")
        buf.write("\2\u009b\u009f\7\67\2\2\u009c\u009e\5^\60\2\u009d\u009c")
        buf.write("\3\2\2\2\u009e\u00a1\3\2\2\2\u009f\u009d\3\2\2\2\u009f")
        buf.write("\u00a0\3\2\2\2\u00a0\r\3\2\2\2\u00a1\u009f\3\2\2\2\u00a2")
        buf.write("\u00a3\5\20\t\2\u00a3\u00ad\7\67\2\2\u00a4\u00a6\5^\60")
        buf.write("\2\u00a5\u00a4\3\2\2\2\u00a6\u00a9\3\2\2\2\u00a7\u00a5")
        buf.write("\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8\u00aa\3\2\2\2\u00a9")
        buf.write("\u00a7\3\2\2\2\u00aa\u00ac\5\20\t\2\u00ab\u00a7\3\2\2")
        buf.write("\2\u00ac\u00af\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ad\u00ae")
        buf.write("\3\2\2\2\u00ae\17\3\2\2\2\u00af\u00ad\3\2\2\2\u00b0\u00b1")
        buf.write("\79\2\2\u00b1\u00b2\5<\37\2\u00b2\21\3\2\2\2\u00b3\u00b4")
        buf.write("\7\13\2\2\u00b4\23\3\2\2\2\u00b5\u00b6\7\f\2\2\u00b6\u00b7")
        buf.write("\79\2\2\u00b7\u00bb\7\16\2\2\u00b8\u00ba\5^\60\2\u00b9")
        buf.write("\u00b8\3\2\2\2\u00ba\u00bd\3\2\2\2\u00bb\u00b9\3\2\2\2")
        buf.write("\u00bb\u00bc\3\2\2\2\u00bc\u00be\3\2\2\2\u00bd\u00bb\3")
        buf.write("\2\2\2\u00be\u00bf\7\63\2\2\u00bf\u00c0\7\64\2\2\u00c0")
        buf.write("\u00c4\7\67\2\2\u00c1\u00c3\5^\60\2\u00c2\u00c1\3\2\2")
        buf.write("\2\u00c3\u00c6\3\2\2\2\u00c4\u00c2\3\2\2\2\u00c4\u00c5")
        buf.write("\3\2\2\2\u00c5\25\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c7\u00c8")
        buf.write("\7\13\2\2\u00c8\27\3\2\2\2\u00c9\u00ca\5\32\16\2\u00ca")
        buf.write("\u00cb\5\30\r\2\u00cb\u00ce\3\2\2\2\u00cc\u00ce\5\32\16")
        buf.write("\2\u00cd\u00c9\3\2\2\2\u00cd\u00cc\3\2\2\2\u00ce\31\3")
        buf.write("\2\2\2\u00cf\u00d3\5\34\17\2\u00d0\u00d3\5\36\20\2\u00d1")
        buf.write("\u00d3\5$\23\2\u00d2\u00cf\3\2\2\2\u00d2\u00d0\3\2\2\2")
        buf.write("\u00d2\u00d1\3\2\2\2\u00d3\33\3\2\2\2\u00d4\u00d5\5\b")
        buf.write("\5\2\u00d5\u00d6\5^\60\2\u00d6\35\3\2\2\2\u00d7\u00d8")
        buf.write("\5 \21\2\u00d8\u00d9\5\"\22\2\u00d9\u00da\5(\25\2\u00da")
        buf.write("\37\3\2\2\2\u00db\u00de\5F$\2\u00dc\u00de\79\2\2\u00dd")
        buf.write("\u00db\3\2\2\2\u00dd\u00dc\3\2\2\2\u00de!\3\2\2\2\u00df")
        buf.write("\u00e0\t\2\2\2\u00e0#\3\2\2\2\u00e1\u00e2\7\n\2\2\u00e2")
        buf.write("\u00e3\5(\25\2\u00e3\u00e7\7\67\2\2\u00e4\u00e6\5^\60")
        buf.write("\2\u00e5\u00e4\3\2\2\2\u00e6\u00e9\3\2\2\2\u00e7\u00e5")
        buf.write("\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8%\3\2\2\2\u00e9\u00e7")
        buf.write("\3\2\2\2\u00ea\u00eb\5(\25\2\u00eb\u00ec\78\2\2\u00ec")
        buf.write("\u00ed\5&\24\2\u00ed\u00f0\3\2\2\2\u00ee\u00f0\5(\25\2")
        buf.write("\u00ef\u00ea\3\2\2\2\u00ef\u00ee\3\2\2\2\u00f0\'\3\2\2")
        buf.write("\2\u00f1\u00f2\b\25\1\2\u00f2\u00f3\5*\26\2\u00f3\u00f9")
        buf.write("\3\2\2\2\u00f4\u00f5\f\4\2\2\u00f5\u00f6\7\'\2\2\u00f6")
        buf.write("\u00f8\5*\26\2\u00f7\u00f4\3\2\2\2\u00f8\u00fb\3\2\2\2")
        buf.write("\u00f9\u00f7\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa)\3\2\2")
        buf.write("\2\u00fb\u00f9\3\2\2\2\u00fc\u00fd\b\26\1\2\u00fd\u00fe")
        buf.write("\5,\27\2\u00fe\u0104\3\2\2\2\u00ff\u0100\f\4\2\2\u0100")
        buf.write("\u0101\7(\2\2\u0101\u0103\5,\27\2\u0102\u00ff\3\2\2\2")
        buf.write("\u0103\u0106\3\2\2\2\u0104\u0102\3\2\2\2\u0104\u0105\3")
        buf.write("\2\2\2\u0105+\3\2\2\2\u0106\u0104\3\2\2\2\u0107\u0108")
        buf.write("\b\27\1\2\u0108\u0109\5.\30\2\u0109\u010f\3\2\2\2\u010a")
        buf.write("\u010b\f\4\2\2\u010b\u010c\7\6\2\2\u010c\u010e\5.\30\2")
        buf.write("\u010d\u010a\3\2\2\2\u010e\u0111\3\2\2\2\u010f\u010d\3")
        buf.write("\2\2\2\u010f\u0110\3\2\2\2\u0110-\3\2\2\2\u0111\u010f")
        buf.write("\3\2\2\2\u0112\u0113\b\30\1\2\u0113\u0114\5\60\31\2\u0114")
        buf.write("\u011a\3\2\2\2\u0115\u0116\f\4\2\2\u0116\u0117\t\3\2\2")
        buf.write("\u0117\u0119\5\60\31\2\u0118\u0115\3\2\2\2\u0119\u011c")
        buf.write("\3\2\2\2\u011a\u0118\3\2\2\2\u011a\u011b\3\2\2\2\u011b")
        buf.write("/\3\2\2\2\u011c\u011a\3\2\2\2\u011d\u011e\b\31\1\2\u011e")
        buf.write("\u011f\5\62\32\2\u011f\u0125\3\2\2\2\u0120\u0121\f\4\2")
        buf.write("\2\u0121\u0122\t\4\2\2\u0122\u0124\5\62\32\2\u0123\u0120")
        buf.write("\3\2\2\2\u0124\u0127\3\2\2\2\u0125\u0123\3\2\2\2\u0125")
        buf.write("\u0126\3\2\2\2\u0126\61\3\2\2\2\u0127\u0125\3\2\2\2\u0128")
        buf.write("\u0129\t\5\2\2\u0129\u012c\5\62\32\2\u012a\u012c\5\64")
        buf.write("\33\2\u012b\u0128\3\2\2\2\u012b\u012a\3\2\2\2\u012c\63")
        buf.write("\3\2\2\2\u012d\u012e\b\33\1\2\u012e\u0131\5\66\34\2\u012f")
        buf.write("\u0131\5:\36\2\u0130\u012d\3\2\2\2\u0130\u012f\3\2\2\2")
        buf.write("\u0131\u0145\3\2\2\2\u0132\u0133\f\6\2\2\u0133\u0134\7")
        buf.write("\65\2\2\u0134\u0135\5(\25\2\u0135\u0136\7\66\2\2\u0136")
        buf.write("\u0144\3\2\2\2\u0137\u0138\f\5\2\2\u0138\u0139\7/\2\2")
        buf.write("\u0139\u013b\79\2\2\u013a\u013c\7\61\2\2\u013b\u013a\3")
        buf.write("\2\2\2\u013b\u013c\3\2\2\2\u013c\u013e\3\2\2\2\u013d\u013f")
        buf.write("\5&\24\2\u013e\u013d\3\2\2\2\u013e\u013f\3\2\2\2\u013f")
        buf.write("\u0141\3\2\2\2\u0140\u0142\7\62\2\2\u0141\u0140\3\2\2")
        buf.write("\2\u0141\u0142\3\2\2\2\u0142\u0144\3\2\2\2\u0143\u0132")
        buf.write("\3\2\2\2\u0143\u0137\3\2\2\2\u0144\u0147\3\2\2\2\u0145")
        buf.write("\u0143\3\2\2\2\u0145\u0146\3\2\2\2\u0146\65\3\2\2\2\u0147")
        buf.write("\u0145\3\2\2\2\u0148\u014f\5J&\2\u0149\u014f\79\2\2\u014a")
        buf.write("\u014b\7\61\2\2\u014b\u014c\5(\25\2\u014c\u014d\7\62\2")
        buf.write("\2\u014d\u014f\3\2\2\2\u014e\u0148\3\2\2\2\u014e\u0149")
        buf.write("\3\2\2\2\u014e\u014a\3\2\2\2\u014f\67\3\2\2\2\u0150\u0151")
        buf.write("\7\65\2\2\u0151\u0152\7;\2\2\u0152\u0153\7\66\2\2\u0153")
        buf.write("\u0158\58\35\2\u0154\u0155\7\65\2\2\u0155\u0156\7;\2\2")
        buf.write("\u0156\u0158\7\66\2\2\u0157\u0150\3\2\2\2\u0157\u0154")
        buf.write("\3\2\2\2\u01589\3\2\2\2\u0159\u015a\79\2\2\u015a\u015c")
        buf.write("\7\61\2\2\u015b\u015d\5&\24\2\u015c\u015b\3\2\2\2\u015c")
        buf.write("\u015d\3\2\2\2\u015d\u015e\3\2\2\2\u015e\u0160\7\62\2")
        buf.write("\2\u015f\u0161\5^\60\2\u0160\u015f\3\2\2\2\u0160\u0161")
        buf.write("\3\2\2\2\u0161;\3\2\2\2\u0162\u0165\5> \2\u0163\u0165")
        buf.write("\5@!\2\u0164\u0162\3\2\2\2\u0164\u0163\3\2\2\2\u0165=")
        buf.write("\3\2\2\2\u0166\u0167\t\6\2\2\u0167?\3\2\2\2\u0168\u016b")
        buf.write("\5B\"\2\u0169\u016b\5D#\2\u016a\u0168\3\2\2\2\u016a\u0169")
        buf.write("\3\2\2\2\u016bA\3\2\2\2\u016c\u016d\79\2\2\u016dC\3\2")
        buf.write("\2\2\u016e\u016f\79\2\2\u016fE\3\2\2\2\u0170\u0171\58")
        buf.write("\35\2\u0171\u0172\5<\37\2\u0172G\3\2\2\2\u0173\u0174\5")
        buf.write("J&\2\u0174\u0175\78\2\2\u0175\u0176\5H%\2\u0176\u0179")
        buf.write("\3\2\2\2\u0177\u0179\5J&\2\u0178\u0173\3\2\2\2\u0178\u0177")
        buf.write("\3\2\2\2\u0179I\3\2\2\2\u017a\u0181\5V,\2\u017b\u0181")
        buf.write("\5X-\2\u017c\u0181\5\\/\2\u017d\u0181\5Z.\2\u017e\u0181")
        buf.write("\5R*\2\u017f\u0181\5L\'\2\u0180\u017a\3\2\2\2\u0180\u017b")
        buf.write("\3\2\2\2\u0180\u017c\3\2\2\2\u0180\u017d\3\2\2\2\u0180")
        buf.write("\u017e\3\2\2\2\u0180\u017f\3\2\2\2\u0181K\3\2\2\2\u0182")
        buf.write("\u0183\79\2\2\u0183\u0185\7\63\2\2\u0184\u0186\5N(\2\u0185")
        buf.write("\u0184\3\2\2\2\u0185\u0186\3\2\2\2\u0186\u0187\3\2\2\2")
        buf.write("\u0187\u0188\7\64\2\2\u0188M\3\2\2\2\u0189\u018b\5P)\2")
        buf.write("\u018a\u018c\5^\60\2\u018b\u018a\3\2\2\2\u018b\u018c\3")
        buf.write("\2\2\2\u018c\u0194\3\2\2\2\u018d\u018e\5P)\2\u018e\u018f")
        buf.write("\78\2\2\u018f\u0191\5N(\2\u0190\u0192\5^\60\2\u0191\u0190")
        buf.write("\3\2\2\2\u0191\u0192\3\2\2\2\u0192\u0194\3\2\2\2\u0193")
        buf.write("\u0189\3\2\2\2\u0193\u018d\3\2\2\2\u0194O\3\2\2\2\u0195")
        buf.write("\u0196\79\2\2\u0196\u0197\7\60\2\2\u0197\u0198\5(\25\2")
        buf.write("\u0198Q\3\2\2\2\u0199\u019a\5F$\2\u019a\u019b\7\63\2\2")
        buf.write("\u019b\u019c\5&\24\2\u019c\u019d\7\64\2\2\u019dS\3\2\2")
        buf.write("\2\u019e\u01a0\7\63\2\2\u019f\u01a1\5T+\2\u01a0\u019f")
        buf.write("\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2")
        buf.write("\u01ac\7\64\2\2\u01a3\u01a4\7\63\2\2\u01a4\u01a5\5(\25")
        buf.write("\2\u01a5\u01a7\78\2\2\u01a6\u01a8\5T+\2\u01a7\u01a6\3")
        buf.write("\2\2\2\u01a7\u01a8\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9\u01aa")
        buf.write("\7\64\2\2\u01aa\u01ac\3\2\2\2\u01ab\u019e\3\2\2\2\u01ab")
        buf.write("\u01a3\3\2\2\2\u01acU\3\2\2\2\u01ad\u01ae\t\7\2\2\u01ae")
        buf.write("W\3\2\2\2\u01af\u01b0\7:\2\2\u01b0Y\3\2\2\2\u01b1\u01b2")
        buf.write("\t\b\2\2\u01b2[\3\2\2\2\u01b3\u01b4\7?\2\2\u01b4]\3\2")
        buf.write("\2\2\u01b5\u01b7\7\4\2\2\u01b6\u01b5\3\2\2\2\u01b6\u01b7")
        buf.write("\3\2\2\2\u01b7\u01b8\3\2\2\2\u01b8\u01b9\7\5\2\2\u01b9")
        buf.write("_\3\2\2\2\62clnw}\u0080\u0083\u008a\u008d\u0096\u009f")
        buf.write("\u00a7\u00ad\u00bb\u00c4\u00cd\u00d2\u00dd\u00e7\u00ef")
        buf.write("\u00f9\u0104\u010f\u011a\u0125\u012b\u0130\u013b\u013e")
        buf.write("\u0141\u0143\u0145\u014e\u0157\u015c\u0160\u0164\u016a")
        buf.write("\u0178\u0180\u0185\u018b\u0191\u0193\u01a0\u01a7\u01ab")
        buf.write("\u01b6")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':='", "'\r'", "'\n'", "<INVALID>", "'if'", 
                     "'else'", "'for'", "'return'", "'func'", "'type'", 
                     "'struct'", "'interface'", "'string'", "'int'", "'float'", 
                     "'boolean'", "'const'", "'var'", "'continue'", "'break'", 
                     "'range'", "'nil'", "'true'", "'false'", "'!'", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'=='", "'!='", "'<'", 
                     "'>'", "'<='", "'>='", "'||'", "'&&'", "'='", "'+='", 
                     "'-='", "'*='", "'/='", "'%='", "'.'", "':'", "'('", 
                     "')'", "'{'", "'}'", "'['", "']'", "';'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "REL", "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", 
                      "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", 
                      "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", "NIL", 
                      "TRUE", "FALSE", "NOT", "ADD", "MINUS", "MUL", "DIV", 
                      "MOD", "EQUAL", "DIFF", "LT", "GT", "LE", "GE", "OR", 
                      "AND", "ASSIGN", "ADD_ASSIGN", "MINUS_ASSIGN", "MULT_ASSIGN", 
                      "DIV_ASSIGN", "REM_ASSIGN", "DOT", "COLON", "LPAREN", 
                      "RPAREN", "LBRACE", "RBRACE", "LBRACK", "RBRACK", 
                      "SEMI", "COMMA", "ID", "FLOAT_LIT", "DEC_LIT", "BIN_LIT", 
                      "OCT_LIT", "HEX_LIT", "STR_LIT", "BOOL_LIT", "WS", 
                      "LINE_COMMENT", "BLOCK_COMMENT", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_decllist = 1
    RULE_decl = 2
    RULE_variable_decl = 3
    RULE_const_decl = 4
    RULE_struct_decl = 5
    RULE_struct_fields = 6
    RULE_struct_field = 7
    RULE_method_decl = 8
    RULE_interface_decl = 9
    RULE_func_decl = 10
    RULE_list_statement = 11
    RULE_statement = 12
    RULE_declared_statement = 13
    RULE_assign_statement = 14
    RULE_lhs = 15
    RULE_ass_operator = 16
    RULE_return_statement = 17
    RULE_list_expr = 18
    RULE_expr = 19
    RULE_and_expr = 20
    RULE_rela_expr = 21
    RULE_add_expr = 22
    RULE_mul_expr = 23
    RULE_unary_expr = 24
    RULE_primary_expr = 25
    RULE_exprd = 26
    RULE_index_operator = 27
    RULE_func_call = 28
    RULE_types = 29
    RULE_primitive_types = 30
    RULE_composite_types = 31
    RULE_struct_type = 32
    RULE_interface_type = 33
    RULE_arr_type = 34
    RULE_literal_list = 35
    RULE_literals = 36
    RULE_struct_lit = 37
    RULE_list_field = 38
    RULE_field = 39
    RULE_arr_lit = 40
    RULE_arr_list = 41
    RULE_int_lit = 42
    RULE_float_lit = 43
    RULE_bool_lit = 44
    RULE_str_lit = 45
    RULE_newline = 46

    ruleNames =  [ "program", "decllist", "decl", "variable_decl", "const_decl", 
                   "struct_decl", "struct_fields", "struct_field", "method_decl", 
                   "interface_decl", "func_decl", "list_statement", "statement", 
                   "declared_statement", "assign_statement", "lhs", "ass_operator", 
                   "return_statement", "list_expr", "expr", "and_expr", 
                   "rela_expr", "add_expr", "mul_expr", "unary_expr", "primary_expr", 
                   "exprd", "index_operator", "func_call", "types", "primitive_types", 
                   "composite_types", "struct_type", "interface_type", "arr_type", 
                   "literal_list", "literals", "struct_lit", "list_field", 
                   "field", "arr_lit", "arr_list", "int_lit", "float_lit", 
                   "bool_lit", "str_lit", "newline" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    REL=4
    IF=5
    ELSE=6
    FOR=7
    RETURN=8
    FUNC=9
    TYPE=10
    STRUCT=11
    INTERFACE=12
    STRING=13
    INT=14
    FLOAT=15
    BOOLEAN=16
    CONST=17
    VAR=18
    CONTINUE=19
    BREAK=20
    RANGE=21
    NIL=22
    TRUE=23
    FALSE=24
    NOT=25
    ADD=26
    MINUS=27
    MUL=28
    DIV=29
    MOD=30
    EQUAL=31
    DIFF=32
    LT=33
    GT=34
    LE=35
    GE=36
    OR=37
    AND=38
    ASSIGN=39
    ADD_ASSIGN=40
    MINUS_ASSIGN=41
    MULT_ASSIGN=42
    DIV_ASSIGN=43
    REM_ASSIGN=44
    DOT=45
    COLON=46
    LPAREN=47
    RPAREN=48
    LBRACE=49
    RBRACE=50
    LBRACK=51
    RBRACK=52
    SEMI=53
    COMMA=54
    ID=55
    FLOAT_LIT=56
    DEC_LIT=57
    BIN_LIT=58
    OCT_LIT=59
    HEX_LIT=60
    STR_LIT=61
    BOOL_LIT=62
    WS=63
    LINE_COMMENT=64
    BLOCK_COMMENT=65
    ERROR_CHAR=66
    UNCLOSE_STRING=67
    ILLEGAL_ESCAPE=68

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

        def decllist(self):
            return self.getTypedRuleContext(MiniGoParser.DecllistContext,0)


        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.NewlineContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.NewlineContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.T__1 or _la==MiniGoParser.T__2:
                self.state = 94
                self.newline()
                self.state = 99
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 100
            self.decllist()
            self.state = 101
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecllistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.DeclContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.DeclContext,i)


        def newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.NewlineContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.NewlineContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decllist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecllist" ):
                return visitor.visitDecllist(self)
            else:
                return visitor.visitChildren(self)




    def decllist(self):

        localctx = MiniGoParser.DecllistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decllist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.decl()
            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__1) | (1 << MiniGoParser.T__2) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR))) != 0):
                self.state = 106
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.FUNC, MiniGoParser.TYPE, MiniGoParser.CONST, MiniGoParser.VAR]:
                    self.state = 104
                    self.decl()
                    pass
                elif token in [MiniGoParser.T__1, MiniGoParser.T__2]:
                    self.state = 105
                    self.newline()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 110
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def variable_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Variable_declContext,0)


        def const_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declContext,0)


        def func_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Func_declContext,0)


        def struct_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_declContext,0)


        def interface_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_declContext,0)


        def method_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Method_declContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = MiniGoParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 117
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 111
                self.variable_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 112
                self.const_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 113
                self.func_decl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 114
                self.struct_decl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 115
                self.interface_decl()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 116
                self.method_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def types(self):
            return self.getTypedRuleContext(MiniGoParser.TypesContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_variable_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_decl" ):
                return visitor.visitVariable_decl(self)
            else:
                return visitor.visitChildren(self)




    def variable_decl(self):

        localctx = MiniGoParser.Variable_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variable_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(MiniGoParser.VAR)
            self.state = 120
            self.match(MiniGoParser.ID)
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ASSIGN:
                self.state = 121
                self.match(MiniGoParser.ASSIGN)
                self.state = 122
                self.expr(0)


            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.ID))) != 0):
                self.state = 125
                self.types()


            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.SEMI:
                self.state = 128
                self.match(MiniGoParser.SEMI)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(MiniGoParser.CONST, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def types(self):
            return self.getTypedRuleContext(MiniGoParser.TypesContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_const_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst_decl" ):
                return visitor.visitConst_decl(self)
            else:
                return visitor.visitChildren(self)




    def const_decl(self):

        localctx = MiniGoParser.Const_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_const_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(MiniGoParser.CONST)
            self.state = 132
            self.match(MiniGoParser.ID)
            self.state = 133
            self.match(MiniGoParser.ASSIGN)
            self.state = 134
            self.expr(0)
            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.ID))) != 0):
                self.state = 135
                self.types()


            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.SEMI:
                self.state = 138
                self.match(MiniGoParser.SEMI)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def struct_fields(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_fieldsContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.NewlineContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.NewlineContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_decl" ):
                return visitor.visitStruct_decl(self)
            else:
                return visitor.visitChildren(self)




    def struct_decl(self):

        localctx = MiniGoParser.Struct_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_struct_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(MiniGoParser.TYPE)
            self.state = 142
            self.match(MiniGoParser.ID)
            self.state = 143
            self.match(MiniGoParser.STRUCT)
            self.state = 144
            self.match(MiniGoParser.LBRACE)
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.T__1 or _la==MiniGoParser.T__2:
                self.state = 145
                self.newline()
                self.state = 150
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 151
            self.struct_fields()
            self.state = 152
            self.match(MiniGoParser.RBRACE)
            self.state = 153
            self.match(MiniGoParser.SEMI)
            self.state = 157
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 154
                    self.newline() 
                self.state = 159
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_fieldsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Struct_fieldContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Struct_fieldContext,i)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.NewlineContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.NewlineContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_fields

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_fields" ):
                return visitor.visitStruct_fields(self)
            else:
                return visitor.visitChildren(self)




    def struct_fields(self):

        localctx = MiniGoParser.Struct_fieldsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_struct_fields)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.struct_field()
            self.state = 161
            self.match(MiniGoParser.SEMI)
            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__1) | (1 << MiniGoParser.T__2) | (1 << MiniGoParser.ID))) != 0):
                self.state = 165
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.T__1 or _la==MiniGoParser.T__2:
                    self.state = 162
                    self.newline()
                    self.state = 167
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 168
                self.struct_field()
                self.state = 173
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_fieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def types(self):
            return self.getTypedRuleContext(MiniGoParser.TypesContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_field

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_field" ):
                return visitor.visitStruct_field(self)
            else:
                return visitor.visitChildren(self)




    def struct_field(self):

        localctx = MiniGoParser.Struct_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_struct_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(MiniGoParser.ID)
            self.state = 175
            self.types()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_method_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_decl" ):
                return visitor.visitMethod_decl(self)
            else:
                return visitor.visitChildren(self)




    def method_decl(self):

        localctx = MiniGoParser.Method_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_method_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.match(MiniGoParser.FUNC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def INTERFACE(self):
            return self.getToken(MiniGoParser.INTERFACE, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.NewlineContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.NewlineContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_decl" ):
                return visitor.visitInterface_decl(self)
            else:
                return visitor.visitChildren(self)




    def interface_decl(self):

        localctx = MiniGoParser.Interface_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_interface_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.match(MiniGoParser.TYPE)
            self.state = 180
            self.match(MiniGoParser.ID)
            self.state = 181
            self.match(MiniGoParser.INTERFACE)
            self.state = 185
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.T__1 or _la==MiniGoParser.T__2:
                self.state = 182
                self.newline()
                self.state = 187
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 188
            self.match(MiniGoParser.LBRACE)
            self.state = 189
            self.match(MiniGoParser.RBRACE)
            self.state = 190
            self.match(MiniGoParser.SEMI)
            self.state = 194
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 191
                    self.newline() 
                self.state = 196
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_func_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decl" ):
                return visitor.visitFunc_decl(self)
            else:
                return visitor.visitChildren(self)




    def func_decl(self):

        localctx = MiniGoParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_func_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.match(MiniGoParser.FUNC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(MiniGoParser.StatementContext,0)


        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_statement" ):
                return visitor.visitList_statement(self)
            else:
                return visitor.visitChildren(self)




    def list_statement(self):

        localctx = MiniGoParser.List_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_list_statement)
        try:
            self.state = 203
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 199
                self.statement()
                self.state = 200
                self.list_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 202
                self.statement()
                pass


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

        def declared_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Declared_statementContext,0)


        def assign_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Return_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniGoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.VAR]:
                self.state = 205
                self.declared_statement()
                pass
            elif token in [MiniGoParser.LBRACK, MiniGoParser.ID]:
                self.state = 206
                self.assign_statement()
                pass
            elif token in [MiniGoParser.RETURN]:
                self.state = 207
                self.return_statement()
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


    class Declared_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Variable_declContext,0)


        def newline(self):
            return self.getTypedRuleContext(MiniGoParser.NewlineContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_declared_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclared_statement" ):
                return visitor.visitDeclared_statement(self)
            else:
                return visitor.visitChildren(self)




    def declared_statement(self):

        localctx = MiniGoParser.Declared_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_declared_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.variable_decl()
            self.state = 211
            self.newline()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def ass_operator(self):
            return self.getTypedRuleContext(MiniGoParser.Ass_operatorContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assign_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_statement" ):
                return visitor.visitAssign_statement(self)
            else:
                return visitor.visitChildren(self)




    def assign_statement(self):

        localctx = MiniGoParser.Assign_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_assign_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.lhs()
            self.state = 214
            self.ass_operator()
            self.state = 215
            self.expr(0)
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

        def arr_type(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_typeContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = MiniGoParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_lhs)
        try:
            self.state = 219
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LBRACK]:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                self.arr_type()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 218
                self.match(MiniGoParser.ID)
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


    class Ass_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS_ASSIGN(self):
            return self.getToken(MiniGoParser.MINUS_ASSIGN, 0)

        def ADD_ASSIGN(self):
            return self.getToken(MiniGoParser.ADD_ASSIGN, 0)

        def MULT_ASSIGN(self):
            return self.getToken(MiniGoParser.MULT_ASSIGN, 0)

        def DIV_ASSIGN(self):
            return self.getToken(MiniGoParser.DIV_ASSIGN, 0)

        def REM_ASSIGN(self):
            return self.getToken(MiniGoParser.REM_ASSIGN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_ass_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAss_operator" ):
                return visitor.visitAss_operator(self)
            else:
                return visitor.visitChildren(self)




    def ass_operator(self):

        localctx = MiniGoParser.Ass_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_ass_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__0) | (1 << MiniGoParser.ADD_ASSIGN) | (1 << MiniGoParser.MINUS_ASSIGN) | (1 << MiniGoParser.MULT_ASSIGN) | (1 << MiniGoParser.DIV_ASSIGN) | (1 << MiniGoParser.REM_ASSIGN))) != 0)):
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


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MiniGoParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.NewlineContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.NewlineContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = MiniGoParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.match(MiniGoParser.RETURN)
            self.state = 224
            self.expr(0)
            self.state = 225
            self.match(MiniGoParser.SEMI)
            self.state = 229
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.T__1 or _la==MiniGoParser.T__2:
                self.state = 226
                self.newline()
                self.state = 231
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_expr(self):
            return self.getTypedRuleContext(MiniGoParser.List_exprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_expr" ):
                return visitor.visitList_expr(self)
            else:
                return visitor.visitChildren(self)




    def list_expr(self):

        localctx = MiniGoParser.List_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_list_expr)
        try:
            self.state = 237
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.expr(0)
                self.state = 233
                self.match(MiniGoParser.COMMA)
                self.state = 234
                self.list_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 236
                self.expr(0)
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

        def and_expr(self):
            return self.getTypedRuleContext(MiniGoParser.And_exprContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.and_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 247
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 242
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 243
                    self.match(MiniGoParser.OR)
                    self.state = 244
                    self.and_expr(0) 
                self.state = 249
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class And_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rela_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Rela_exprContext,0)


        def and_expr(self):
            return self.getTypedRuleContext(MiniGoParser.And_exprContext,0)


        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_and_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnd_expr" ):
                return visitor.visitAnd_expr(self)
            else:
                return visitor.visitChildren(self)



    def and_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.And_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_and_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.rela_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 258
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.And_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_and_expr)
                    self.state = 253
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 254
                    self.match(MiniGoParser.AND)
                    self.state = 255
                    self.rela_expr(0) 
                self.state = 260
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Rela_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def add_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Add_exprContext,0)


        def rela_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Rela_exprContext,0)


        def REL(self):
            return self.getToken(MiniGoParser.REL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_rela_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRela_expr" ):
                return visitor.visitRela_expr(self)
            else:
                return visitor.visitChildren(self)



    def rela_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Rela_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_rela_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.add_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 269
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Rela_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_rela_expr)
                    self.state = 264
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 265
                    self.match(MiniGoParser.REL)
                    self.state = 266
                    self.add_expr(0) 
                self.state = 271
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Add_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mul_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Mul_exprContext,0)


        def add_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Add_exprContext,0)


        def ADD(self):
            return self.getToken(MiniGoParser.ADD, 0)

        def MINUS(self):
            return self.getToken(MiniGoParser.MINUS, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_add_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd_expr" ):
                return visitor.visitAdd_expr(self)
            else:
                return visitor.visitChildren(self)



    def add_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Add_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_add_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.mul_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 280
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Add_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_add_expr)
                    self.state = 275
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 276
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.ADD or _la==MiniGoParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 277
                    self.mul_expr(0) 
                self.state = 282
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Mul_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Unary_exprContext,0)


        def mul_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Mul_exprContext,0)


        def MUL(self):
            return self.getToken(MiniGoParser.MUL, 0)

        def DIV(self):
            return self.getToken(MiniGoParser.DIV, 0)

        def MOD(self):
            return self.getToken(MiniGoParser.MOD, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_mul_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMul_expr" ):
                return visitor.visitMul_expr(self)
            else:
                return visitor.visitChildren(self)



    def mul_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Mul_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_mul_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.unary_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 291
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Mul_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_mul_expr)
                    self.state = 286
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 287
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 288
                    self.unary_expr() 
                self.state = 293
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Unary_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Unary_exprContext,0)


        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def MINUS(self):
            return self.getToken(MiniGoParser.MINUS, 0)

        def primary_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Primary_exprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_unary_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary_expr" ):
                return visitor.visitUnary_expr(self)
            else:
                return visitor.visitChildren(self)




    def unary_expr(self):

        localctx = MiniGoParser.Unary_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_unary_expr)
        self._la = 0 # Token type
        try:
            self.state = 297
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NOT, MiniGoParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 294
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.NOT or _la==MiniGoParser.MINUS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 295
                self.unary_expr()
                pass
            elif token in [MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.LPAREN, MiniGoParser.LBRACK, MiniGoParser.ID, MiniGoParser.FLOAT_LIT, MiniGoParser.DEC_LIT, MiniGoParser.BIN_LIT, MiniGoParser.OCT_LIT, MiniGoParser.HEX_LIT, MiniGoParser.STR_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 296
                self.primary_expr(0)
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


    class Primary_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprd(self):
            return self.getTypedRuleContext(MiniGoParser.ExprdContext,0)


        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def primary_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Primary_exprContext,0)


        def LBRACK(self):
            return self.getToken(MiniGoParser.LBRACK, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RBRACK(self):
            return self.getToken(MiniGoParser.RBRACK, 0)

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def list_expr(self):
            return self.getTypedRuleContext(MiniGoParser.List_exprContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_primary_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary_expr" ):
                return visitor.visitPrimary_expr(self)
            else:
                return visitor.visitChildren(self)



    def primary_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Primary_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_primary_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 300
                self.exprd()
                pass

            elif la_ == 2:
                self.state = 301
                self.func_call()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 323
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 321
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Primary_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_primary_expr)
                        self.state = 304
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 305
                        self.match(MiniGoParser.LBRACK)
                        self.state = 306
                        self.expr(0)
                        self.state = 307
                        self.match(MiniGoParser.RBRACK)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Primary_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_primary_expr)
                        self.state = 309
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 310
                        self.match(MiniGoParser.DOT)
                        self.state = 311
                        self.match(MiniGoParser.ID)
                        self.state = 313
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                        if la_ == 1:
                            self.state = 312
                            self.match(MiniGoParser.LPAREN)


                        self.state = 316
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
                        if la_ == 1:
                            self.state = 315
                            self.list_expr()


                        self.state = 319
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
                        if la_ == 1:
                            self.state = 318
                            self.match(MiniGoParser.RPAREN)


                        pass

             
                self.state = 325
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExprdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literals(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralsContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_exprd

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprd" ):
                return visitor.visitExprd(self)
            else:
                return visitor.visitChildren(self)




    def exprd(self):

        localctx = MiniGoParser.ExprdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_exprd)
        try:
            self.state = 332
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 326
                self.literals()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 327
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 328
                self.match(MiniGoParser.LPAREN)
                self.state = 329
                self.expr(0)
                self.state = 330
                self.match(MiniGoParser.RPAREN)
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

        def LBRACK(self):
            return self.getToken(MiniGoParser.LBRACK, 0)

        def DEC_LIT(self):
            return self.getToken(MiniGoParser.DEC_LIT, 0)

        def RBRACK(self):
            return self.getToken(MiniGoParser.RBRACK, 0)

        def index_operator(self):
            return self.getTypedRuleContext(MiniGoParser.Index_operatorContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_index_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operator" ):
                return visitor.visitIndex_operator(self)
            else:
                return visitor.visitChildren(self)




    def index_operator(self):

        localctx = MiniGoParser.Index_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_index_operator)
        try:
            self.state = 341
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 334
                self.match(MiniGoParser.LBRACK)
                self.state = 335
                self.match(MiniGoParser.DEC_LIT)
                self.state = 336
                self.match(MiniGoParser.RBRACK)
                self.state = 337
                self.index_operator()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 338
                self.match(MiniGoParser.LBRACK)
                self.state = 339
                self.match(MiniGoParser.DEC_LIT)
                self.state = 340
                self.match(MiniGoParser.RBRACK)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def list_expr(self):
            return self.getTypedRuleContext(MiniGoParser.List_exprContext,0)


        def newline(self):
            return self.getTypedRuleContext(MiniGoParser.NewlineContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = MiniGoParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self.match(MiniGoParser.ID)
            self.state = 344
            self.match(MiniGoParser.LPAREN)
            self.state = 346
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.MINUS) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LBRACK) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.DEC_LIT) | (1 << MiniGoParser.BIN_LIT) | (1 << MiniGoParser.OCT_LIT) | (1 << MiniGoParser.HEX_LIT) | (1 << MiniGoParser.STR_LIT))) != 0):
                self.state = 345
                self.list_expr()


            self.state = 348
            self.match(MiniGoParser.RPAREN)
            self.state = 350
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.state = 349
                self.newline()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_types(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_typesContext,0)


        def composite_types(self):
            return self.getTypedRuleContext(MiniGoParser.Composite_typesContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_types

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypes" ):
                return visitor.visitTypes(self)
            else:
                return visitor.visitChildren(self)




    def types(self):

        localctx = MiniGoParser.TypesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_types)
        try:
            self.state = 354
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.NIL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 352
                self.primitive_types()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 353
                self.composite_types()
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


    class Primitive_typesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_primitive_types

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_types" ):
                return visitor.visitPrimitive_types(self)
            else:
                return visitor.visitChildren(self)




    def primitive_types(self):

        localctx = MiniGoParser.Primitive_typesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_primitive_types)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.NIL))) != 0)):
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


    class Composite_typesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_type(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_typeContext,0)


        def interface_type(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_composite_types

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComposite_types" ):
                return visitor.visitComposite_types(self)
            else:
                return visitor.visitChildren(self)




    def composite_types(self):

        localctx = MiniGoParser.Composite_typesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_composite_types)
        try:
            self.state = 360
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 358
                self.struct_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 359
                self.interface_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_type" ):
                return visitor.visitStruct_type(self)
            else:
                return visitor.visitChildren(self)




    def struct_type(self):

        localctx = MiniGoParser.Struct_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_struct_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self.match(MiniGoParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_type" ):
                return visitor.visitInterface_type(self)
            else:
                return visitor.visitChildren(self)




    def interface_type(self):

        localctx = MiniGoParser.Interface_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_interface_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            self.match(MiniGoParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def index_operator(self):
            return self.getTypedRuleContext(MiniGoParser.Index_operatorContext,0)


        def types(self):
            return self.getTypedRuleContext(MiniGoParser.TypesContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arr_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_type" ):
                return visitor.visitArr_type(self)
            else:
                return visitor.visitChildren(self)




    def arr_type(self):

        localctx = MiniGoParser.Arr_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_arr_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            self.index_operator()
            self.state = 367
            self.types()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Literal_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literals(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralsContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def literal_list(self):
            return self.getTypedRuleContext(MiniGoParser.Literal_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_literal_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral_list" ):
                return visitor.visitLiteral_list(self)
            else:
                return visitor.visitChildren(self)




    def literal_list(self):

        localctx = MiniGoParser.Literal_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_literal_list)
        try:
            self.state = 374
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 369
                self.literals()
                self.state = 370
                self.match(MiniGoParser.COMMA)
                self.state = 371
                self.literal_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 373
                self.literals()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def int_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Int_litContext,0)


        def float_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Float_litContext,0)


        def str_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Str_litContext,0)


        def bool_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Bool_litContext,0)


        def arr_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_litContext,0)


        def struct_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_litContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_literals

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiterals" ):
                return visitor.visitLiterals(self)
            else:
                return visitor.visitChildren(self)




    def literals(self):

        localctx = MiniGoParser.LiteralsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_literals)
        try:
            self.state = 382
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.DEC_LIT, MiniGoParser.BIN_LIT, MiniGoParser.OCT_LIT, MiniGoParser.HEX_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 376
                self.int_lit()
                pass
            elif token in [MiniGoParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 377
                self.float_lit()
                pass
            elif token in [MiniGoParser.STR_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 378
                self.str_lit()
                pass
            elif token in [MiniGoParser.TRUE, MiniGoParser.FALSE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 379
                self.bool_lit()
                pass
            elif token in [MiniGoParser.LBRACK]:
                self.enterOuterAlt(localctx, 5)
                self.state = 380
                self.arr_lit()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 381
                self.struct_lit()
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


    class Struct_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def list_field(self):
            return self.getTypedRuleContext(MiniGoParser.List_fieldContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_lit" ):
                return visitor.visitStruct_lit(self)
            else:
                return visitor.visitChildren(self)




    def struct_lit(self):

        localctx = MiniGoParser.Struct_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_struct_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self.match(MiniGoParser.ID)
            self.state = 385
            self.match(MiniGoParser.LBRACE)
            self.state = 387
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 386
                self.list_field()


            self.state = 389
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_fieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field(self):
            return self.getTypedRuleContext(MiniGoParser.FieldContext,0)


        def newline(self):
            return self.getTypedRuleContext(MiniGoParser.NewlineContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_field(self):
            return self.getTypedRuleContext(MiniGoParser.List_fieldContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_field

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_field" ):
                return visitor.visitList_field(self)
            else:
                return visitor.visitChildren(self)




    def list_field(self):

        localctx = MiniGoParser.List_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_list_field)
        try:
            self.state = 401
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 391
                self.field()
                self.state = 393
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
                if la_ == 1:
                    self.state = 392
                    self.newline()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 395
                self.field()
                self.state = 396
                self.match(MiniGoParser.COMMA)
                self.state = 397
                self.list_field()
                self.state = 399
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
                if la_ == 1:
                    self.state = 398
                    self.newline()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COLON(self):
            return self.getToken(MiniGoParser.COLON, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_field

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField" ):
                return visitor.visitField(self)
            else:
                return visitor.visitChildren(self)




    def field(self):

        localctx = MiniGoParser.FieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
            self.match(MiniGoParser.ID)
            self.state = 404
            self.match(MiniGoParser.COLON)
            self.state = 405
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arr_type(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_typeContext,0)


        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def list_expr(self):
            return self.getTypedRuleContext(MiniGoParser.List_exprContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arr_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_lit" ):
                return visitor.visitArr_lit(self)
            else:
                return visitor.visitChildren(self)




    def arr_lit(self):

        localctx = MiniGoParser.Arr_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_arr_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
            self.arr_type()
            self.state = 408
            self.match(MiniGoParser.LBRACE)
            self.state = 409
            self.list_expr()
            self.state = 410
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def arr_list(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_listContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arr_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_list" ):
                return visitor.visitArr_list(self)
            else:
                return visitor.visitChildren(self)




    def arr_list(self):

        localctx = MiniGoParser.Arr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_arr_list)
        self._la = 0 # Token type
        try:
            self.state = 425
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 412
                self.match(MiniGoParser.LBRACE)
                self.state = 414
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.LBRACE:
                    self.state = 413
                    self.arr_list()


                self.state = 416
                self.match(MiniGoParser.RBRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 417
                self.match(MiniGoParser.LBRACE)
                self.state = 418
                self.expr(0)
                self.state = 419
                self.match(MiniGoParser.COMMA)
                self.state = 421
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.LBRACE:
                    self.state = 420
                    self.arr_list()


                self.state = 423
                self.match(MiniGoParser.RBRACE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Int_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEC_LIT(self):
            return self.getToken(MiniGoParser.DEC_LIT, 0)

        def BIN_LIT(self):
            return self.getToken(MiniGoParser.BIN_LIT, 0)

        def OCT_LIT(self):
            return self.getToken(MiniGoParser.OCT_LIT, 0)

        def HEX_LIT(self):
            return self.getToken(MiniGoParser.HEX_LIT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_int_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_lit" ):
                return visitor.visitInt_lit(self)
            else:
                return visitor.visitChildren(self)




    def int_lit(self):

        localctx = MiniGoParser.Int_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_int_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 427
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.DEC_LIT) | (1 << MiniGoParser.BIN_LIT) | (1 << MiniGoParser.OCT_LIT) | (1 << MiniGoParser.HEX_LIT))) != 0)):
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


    class Float_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_float_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat_lit" ):
                return visitor.visitFloat_lit(self)
            else:
                return visitor.visitChildren(self)




    def float_lit(self):

        localctx = MiniGoParser.Float_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_float_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 429
            self.match(MiniGoParser.FLOAT_LIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bool_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(MiniGoParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniGoParser.FALSE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_bool_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool_lit" ):
                return visitor.visitBool_lit(self)
            else:
                return visitor.visitChildren(self)




    def bool_lit(self):

        localctx = MiniGoParser.Bool_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_bool_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 431
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.TRUE or _la==MiniGoParser.FALSE):
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


    class Str_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STR_LIT(self):
            return self.getToken(MiniGoParser.STR_LIT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_str_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStr_lit" ):
                return visitor.visitStr_lit(self)
            else:
                return visitor.visitChildren(self)




    def str_lit(self):

        localctx = MiniGoParser.Str_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_str_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 433
            self.match(MiniGoParser.STR_LIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NewlineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniGoParser.RULE_newline

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewline" ):
                return visitor.visitNewline(self)
            else:
                return visitor.visitChildren(self)




    def newline(self):

        localctx = MiniGoParser.NewlineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_newline)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 436
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.T__1:
                self.state = 435
                self.match(MiniGoParser.T__1)


            self.state = 438
            self.match(MiniGoParser.T__2)
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
        self._predicates[19] = self.expr_sempred
        self._predicates[20] = self.and_expr_sempred
        self._predicates[21] = self.rela_expr_sempred
        self._predicates[22] = self.add_expr_sempred
        self._predicates[23] = self.mul_expr_sempred
        self._predicates[25] = self.primary_expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def and_expr_sempred(self, localctx:And_exprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def rela_expr_sempred(self, localctx:Rela_exprContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def add_expr_sempred(self, localctx:Add_exprContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def mul_expr_sempred(self, localctx:Mul_exprContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def primary_expr_sempred(self, localctx:Primary_exprContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         




