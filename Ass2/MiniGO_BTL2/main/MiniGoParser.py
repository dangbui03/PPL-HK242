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
        buf.write("\u0340\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\3\2")
        buf.write("\7\2\u0088\n\2\f\2\16\2\u008b\13\2\3\2\3\2\3\2\3\3\3\3")
        buf.write("\3\3\7\3\u0093\n\3\f\3\16\3\u0096\13\3\3\3\3\3\7\3\u009a")
        buf.write("\n\3\f\3\16\3\u009d\13\3\5\3\u009f\n\3\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\5\4\u00a7\n\4\3\5\3\5\3\5\5\5\u00ac\n\5\3\5\3")
        buf.write("\5\5\5\u00b0\n\5\3\5\3\5\7\5\u00b4\n\5\f\5\16\5\u00b7")
        buf.write("\13\5\3\6\3\6\3\6\5\6\u00bc\n\6\3\6\3\6\3\6\5\6\u00c1")
        buf.write("\n\6\3\6\7\6\u00c4\n\6\f\6\16\6\u00c7\13\6\3\7\3\7\3\7")
        buf.write("\3\7\3\7\7\7\u00ce\n\7\f\7\16\7\u00d1\13\7\3\7\5\7\u00d4")
        buf.write("\n\7\3\7\3\7\3\7\5\7\u00d9\n\7\3\7\7\7\u00dc\n\7\f\7\16")
        buf.write("\7\u00df\13\7\3\b\3\b\3\b\3\b\5\b\u00e5\n\b\3\t\3\t\3")
        buf.write("\t\5\t\u00ea\n\t\3\t\3\t\7\t\u00ee\n\t\f\t\16\t\u00f1")
        buf.write("\13\t\3\t\3\t\3\t\3\t\5\t\u00f7\n\t\3\t\7\t\u00fa\n\t")
        buf.write("\f\t\16\t\u00fd\13\t\5\t\u00ff\n\t\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\5\n\u010a\n\n\3\n\3\n\7\n\u010e\n\n\f")
        buf.write("\n\16\n\u0111\13\n\3\13\3\13\3\13\3\13\3\13\3\13\5\13")
        buf.write("\u0119\n\13\3\f\3\f\3\f\3\f\7\f\u011f\n\f\f\f\16\f\u0122")
        buf.write("\13\f\3\f\3\f\7\f\u0126\n\f\f\f\16\f\u0129\13\f\3\f\5")
        buf.write("\f\u012c\n\f\3\f\3\f\5\f\u0130\n\f\3\f\7\f\u0133\n\f\f")
        buf.write("\f\16\f\u0136\13\f\3\r\3\r\3\r\3\r\5\r\u013c\n\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\5\16\u0143\n\16\3\16\5\16\u0146\n")
        buf.write("\16\3\16\7\16\u0149\n\16\f\16\16\16\u014c\13\16\3\17\3")
        buf.write("\17\3\17\3\17\3\17\5\17\u0153\n\17\3\20\3\20\5\20\u0157")
        buf.write("\n\20\3\20\5\20\u015a\n\20\3\21\3\21\3\21\3\21\3\21\3")
        buf.write("\21\5\21\u0162\n\21\3\21\3\21\7\21\u0166\n\21\f\21\16")
        buf.write("\21\u0169\13\21\3\22\3\22\3\22\3\22\3\22\5\22\u0170\n")
        buf.write("\22\3\23\3\23\3\23\5\23\u0175\n\23\3\24\3\24\7\24\u0179")
        buf.write("\n\24\f\24\16\24\u017c\13\24\3\24\5\24\u017f\n\24\3\24")
        buf.write("\3\24\7\24\u0183\n\24\f\24\16\24\u0186\13\24\3\25\3\25")
        buf.write("\3\25\3\25\5\25\u018c\n\25\3\26\3\26\3\26\3\26\3\26\3")
        buf.write("\26\3\26\3\26\5\26\u0196\n\26\3\27\3\27\7\27\u019a\n\27")
        buf.write("\f\27\16\27\u019d\13\27\3\27\3\27\7\27\u01a1\n\27\f\27")
        buf.write("\16\27\u01a4\13\27\5\27\u01a6\n\27\3\30\3\30\3\30\3\30")
        buf.write("\5\30\u01ac\n\30\3\30\7\30\u01af\n\30\f\30\16\30\u01b2")
        buf.write("\13\30\3\31\3\31\3\31\3\31\5\31\u01b8\n\31\3\32\3\32\3")
        buf.write("\32\5\32\u01bd\n\32\3\33\3\33\3\34\3\34\3\34\3\34\3\34")
        buf.write("\7\34\u01c6\n\34\f\34\16\34\u01c9\13\34\3\34\3\34\5\34")
        buf.write("\u01cd\n\34\3\34\5\34\u01d0\n\34\3\34\7\34\u01d3\n\34")
        buf.write("\f\34\16\34\u01d6\13\34\3\35\3\35\3\35\3\35\5\35\u01dc")
        buf.write("\n\35\3\36\3\36\3\36\3\36\3\36\3\36\7\36\u01e4\n\36\f")
        buf.write("\36\16\36\u01e7\13\36\3\36\3\36\3\37\3\37\7\37\u01ed\n")
        buf.write("\37\f\37\16\37\u01f0\13\37\3\37\3\37\3 \3 \3 \7 \u01f7")
        buf.write("\n \f \16 \u01fa\13 \3 \3 \7 \u01fe\n \f \16 \u0201\13")
        buf.write(" \3 \3 \3 \3 \3 \3 \7 \u0209\n \f \16 \u020c\13 \3 \3")
        buf.write(" \7 \u0210\n \f \16 \u0213\13 \3 \3 \3 \3 \3 \3 \7 \u021b")
        buf.write("\n \f \16 \u021e\13 \3 \3 \7 \u0222\n \f \16 \u0225\13")
        buf.write(" \5 \u0227\n \3!\3!\5!\u022b\n!\3\"\3\"\3\"\3\"\3#\3#")
        buf.write("\3#\5#\u0234\n#\3#\7#\u0237\n#\f#\16#\u023a\13#\3$\5$")
        buf.write("\u023d\n$\3$\3$\3$\5$\u0242\n$\3$\3$\3$\5$\u0247\n$\3")
        buf.write("$\7$\u024a\n$\f$\16$\u024d\13$\3%\3%\3%\5%\u0252\n%\3")
        buf.write("%\7%\u0255\n%\f%\16%\u0258\13%\3&\3&\5&\u025c\n&\3&\3")
        buf.write("&\5&\u0260\n&\3&\7&\u0263\n&\f&\16&\u0266\13&\3\'\3\'")
        buf.write("\3\'\3\'\3\'\5\'\u026d\n\'\3(\3(\3(\3(\3(\3(\7(\u0275")
        buf.write("\n(\f(\16(\u0278\13(\3)\3)\3)\3)\3)\3)\7)\u0280\n)\f)")
        buf.write("\16)\u0283\13)\3*\3*\3*\3*\3*\3*\7*\u028b\n*\f*\16*\u028e")
        buf.write("\13*\3+\3+\3+\3+\3+\3+\7+\u0296\n+\f+\16+\u0299\13+\3")
        buf.write(",\3,\3,\3,\3,\3,\7,\u02a1\n,\f,\16,\u02a4\13,\3-\3-\3")
        buf.write("-\5-\u02a9\n-\3.\3.\3.\5.\u02ae\n.\3.\3.\3.\3.\3.\3.\3")
        buf.write(".\3.\5.\u02b8\n.\3.\3.\5.\u02bc\n.\3.\5.\u02bf\n.\7.\u02c1")
        buf.write("\n.\f.\16.\u02c4\13.\3/\3/\3/\3/\3/\3/\5/\u02cc\n/\3\60")
        buf.write("\3\60\3\60\5\60\u02d1\n\60\3\60\3\60\5\60\u02d5\n\60\3")
        buf.write("\61\3\61\3\61\3\61\5\61\u02db\n\61\3\61\5\61\u02de\n\61")
        buf.write("\3\61\5\61\u02e1\n\61\3\62\3\62\3\62\5\62\u02e6\n\62\3")
        buf.write("\63\3\63\3\64\3\64\5\64\u02ec\n\64\3\65\3\65\3\66\3\66")
        buf.write("\3\67\3\67\5\67\u02f4\n\67\38\38\38\38\38\38\38\38\38")
        buf.write("\58\u02ff\n8\39\39\39\39\39\39\59\u0307\n9\3:\3:\3:\5")
        buf.write(":\u030c\n:\3:\3:\3;\3;\5;\u0312\n;\3;\3;\3;\3;\5;\u0318")
        buf.write("\n;\5;\u031a\n;\3<\3<\3<\3<\3=\3=\3=\5=\u0323\n=\3=\3")
        buf.write("=\3>\3>\3>\3>\5>\u032b\n>\3>\3>\5>\u032f\n>\5>\u0331\n")
        buf.write(">\3?\3?\3@\3@\3A\3A\3B\3B\3C\5C\u033c\nC\3C\3C\3C\2\b")
        buf.write("NPRTVZD\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*")
        buf.write(",.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080")
        buf.write("\u0082\u0084\2\t\4\2\3\3*.\3\2\34\35\3\2\36 \4\2\33\33")
        buf.write("\35\35\4\2\17\22\30\30\3\2:=\3\2\31\32\2\u037e\2\u0089")
        buf.write("\3\2\2\2\4\u009e\3\2\2\2\6\u00a6\3\2\2\2\b\u00a8\3\2\2")
        buf.write("\2\n\u00b8\3\2\2\2\f\u00c8\3\2\2\2\16\u00e4\3\2\2\2\20")
        buf.write("\u00fe\3\2\2\2\22\u0100\3\2\2\2\24\u0118\3\2\2\2\26\u011a")
        buf.write("\3\2\2\2\30\u013b\3\2\2\2\32\u013d\3\2\2\2\34\u0152\3")
        buf.write("\2\2\2\36\u0159\3\2\2\2 \u015b\3\2\2\2\"\u016f\3\2\2\2")
        buf.write("$\u0174\3\2\2\2&\u0176\3\2\2\2(\u018b\3\2\2\2*\u0195\3")
        buf.write("\2\2\2,\u01a5\3\2\2\2.\u01a7\3\2\2\2\60\u01b7\3\2\2\2")
        buf.write("\62\u01bc\3\2\2\2\64\u01be\3\2\2\2\66\u01c0\3\2\2\28\u01db")
        buf.write("\3\2\2\2:\u01dd\3\2\2\2<\u01ea\3\2\2\2>\u0226\3\2\2\2")
        buf.write("@\u022a\3\2\2\2B\u022c\3\2\2\2D\u0230\3\2\2\2F\u023c\3")
        buf.write("\2\2\2H\u024e\3\2\2\2J\u0259\3\2\2\2L\u026c\3\2\2\2N\u026e")
        buf.write("\3\2\2\2P\u0279\3\2\2\2R\u0284\3\2\2\2T\u028f\3\2\2\2")
        buf.write("V\u029a\3\2\2\2X\u02a8\3\2\2\2Z\u02ad\3\2\2\2\\\u02cb")
        buf.write("\3\2\2\2^\u02cd\3\2\2\2`\u02d6\3\2\2\2b\u02e5\3\2\2\2")
        buf.write("d\u02e7\3\2\2\2f\u02eb\3\2\2\2h\u02ed\3\2\2\2j\u02ef\3")
        buf.write("\2\2\2l\u02f1\3\2\2\2n\u02fe\3\2\2\2p\u0306\3\2\2\2r\u0308")
        buf.write("\3\2\2\2t\u0319\3\2\2\2v\u031b\3\2\2\2x\u031f\3\2\2\2")
        buf.write("z\u0330\3\2\2\2|\u0332\3\2\2\2~\u0334\3\2\2\2\u0080\u0336")
        buf.write("\3\2\2\2\u0082\u0338\3\2\2\2\u0084\u033b\3\2\2\2\u0086")
        buf.write("\u0088\5\u0084C\2\u0087\u0086\3\2\2\2\u0088\u008b\3\2")
        buf.write("\2\2\u0089\u0087\3\2\2\2\u0089\u008a\3\2\2\2\u008a\u008c")
        buf.write("\3\2\2\2\u008b\u0089\3\2\2\2\u008c\u008d\5\4\3\2\u008d")
        buf.write("\u008e\7\2\2\3\u008e\3\3\2\2\2\u008f\u0090\5\6\4\2\u0090")
        buf.write("\u0094\5\4\3\2\u0091\u0093\5\u0084C\2\u0092\u0091\3\2")
        buf.write("\2\2\u0093\u0096\3\2\2\2\u0094\u0092\3\2\2\2\u0094\u0095")
        buf.write("\3\2\2\2\u0095\u009f\3\2\2\2\u0096\u0094\3\2\2\2\u0097")
        buf.write("\u009b\5\6\4\2\u0098\u009a\5\u0084C\2\u0099\u0098\3\2")
        buf.write("\2\2\u009a\u009d\3\2\2\2\u009b\u0099\3\2\2\2\u009b\u009c")
        buf.write("\3\2\2\2\u009c\u009f\3\2\2\2\u009d\u009b\3\2\2\2\u009e")
        buf.write("\u008f\3\2\2\2\u009e\u0097\3\2\2\2\u009f\5\3\2\2\2\u00a0")
        buf.write("\u00a7\5\b\5\2\u00a1\u00a7\5\n\6\2\u00a2\u00a7\5 \21\2")
        buf.write("\u00a3\u00a7\5\22\n\2\u00a4\u00a7\5\f\7\2\u00a5\u00a7")
        buf.write("\5\26\f\2\u00a6\u00a0\3\2\2\2\u00a6\u00a1\3\2\2\2\u00a6")
        buf.write("\u00a2\3\2\2\2\u00a6\u00a3\3\2\2\2\u00a6\u00a4\3\2\2\2")
        buf.write("\u00a6\u00a5\3\2\2\2\u00a7\7\3\2\2\2\u00a8\u00a9\7\24")
        buf.write("\2\2\u00a9\u00ab\79\2\2\u00aa\u00ac\5b\62\2\u00ab\u00aa")
        buf.write("\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac\u00af\3\2\2\2\u00ad")
        buf.write("\u00ae\7)\2\2\u00ae\u00b0\5L\'\2\u00af\u00ad\3\2\2\2\u00af")
        buf.write("\u00b0\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00b5\7\67\2")
        buf.write("\2\u00b2\u00b4\5\u0084C\2\u00b3\u00b2\3\2\2\2\u00b4\u00b7")
        buf.write("\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6")
        buf.write("\t\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b8\u00b9\7\23\2\2\u00b9")
        buf.write("\u00bb\79\2\2\u00ba\u00bc\5b\62\2\u00bb\u00ba\3\2\2\2")
        buf.write("\u00bb\u00bc\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd\u00be\7")
        buf.write(")\2\2\u00be\u00c0\5L\'\2\u00bf\u00c1\7\67\2\2\u00c0\u00bf")
        buf.write("\3\2\2\2\u00c0\u00c1\3\2\2\2\u00c1\u00c5\3\2\2\2\u00c2")
        buf.write("\u00c4\5\u0084C\2\u00c3\u00c2\3\2\2\2\u00c4\u00c7\3\2")
        buf.write("\2\2\u00c5\u00c3\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6\13")
        buf.write("\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c8\u00c9\7\f\2\2\u00c9")
        buf.write("\u00ca\79\2\2\u00ca\u00cb\7\r\2\2\u00cb\u00cf\7\63\2\2")
        buf.write("\u00cc\u00ce\5\u0084C\2\u00cd\u00cc\3\2\2\2\u00ce\u00d1")
        buf.write("\3\2\2\2\u00cf\u00cd\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0")
        buf.write("\u00d3\3\2\2\2\u00d1\u00cf\3\2\2\2\u00d2\u00d4\5\16\b")
        buf.write("\2\u00d3\u00d2\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4\u00d5")
        buf.write("\3\2\2\2\u00d5\u00d8\7\64\2\2\u00d6\u00d9\7\67\2\2\u00d7")
        buf.write("\u00d9\5\u0084C\2\u00d8\u00d6\3\2\2\2\u00d8\u00d7\3\2")
        buf.write("\2\2\u00d9\u00dd\3\2\2\2\u00da\u00dc\5\u0084C\2\u00db")
        buf.write("\u00da\3\2\2\2\u00dc\u00df\3\2\2\2\u00dd\u00db\3\2\2\2")
        buf.write("\u00dd\u00de\3\2\2\2\u00de\r\3\2\2\2\u00df\u00dd\3\2\2")
        buf.write("\2\u00e0\u00e1\5\20\t\2\u00e1\u00e2\5\16\b\2\u00e2\u00e5")
        buf.write("\3\2\2\2\u00e3\u00e5\5\20\t\2\u00e4\u00e0\3\2\2\2\u00e4")
        buf.write("\u00e3\3\2\2\2\u00e5\17\3\2\2\2\u00e6\u00e9\79\2\2\u00e7")
        buf.write("\u00ea\5d\63\2\u00e8\u00ea\5l\67\2\u00e9\u00e7\3\2\2\2")
        buf.write("\u00e9\u00e8\3\2\2\2\u00ea\u00eb\3\2\2\2\u00eb\u00ef\7")
        buf.write("\67\2\2\u00ec\u00ee\5\u0084C\2\u00ed\u00ec\3\2\2\2\u00ee")
        buf.write("\u00f1\3\2\2\2\u00ef\u00ed\3\2\2\2\u00ef\u00f0\3\2\2\2")
        buf.write("\u00f0\u00ff\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f2\u00f3\7")
        buf.write("9\2\2\u00f3\u00f6\5f\64\2\u00f4\u00f7\7\67\2\2\u00f5\u00f7")
        buf.write("\5\u0084C\2\u00f6\u00f4\3\2\2\2\u00f6\u00f5\3\2\2\2\u00f7")
        buf.write("\u00fb\3\2\2\2\u00f8\u00fa\5\u0084C\2\u00f9\u00f8\3\2")
        buf.write("\2\2\u00fa\u00fd\3\2\2\2\u00fb\u00f9\3\2\2\2\u00fb\u00fc")
        buf.write("\3\2\2\2\u00fc\u00ff\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fe")
        buf.write("\u00e6\3\2\2\2\u00fe\u00f2\3\2\2\2\u00ff\21\3\2\2\2\u0100")
        buf.write("\u0101\7\13\2\2\u0101\u0102\7\61\2\2\u0102\u0103\5\24")
        buf.write("\13\2\u0103\u0104\7\62\2\2\u0104\u0105\79\2\2\u0105\u0106")
        buf.write("\7\61\2\2\u0106\u0107\5\"\22\2\u0107\u0109\7\62\2\2\u0108")
        buf.write("\u010a\5b\62\2\u0109\u0108\3\2\2\2\u0109\u010a\3\2\2\2")
        buf.write("\u010a\u010b\3\2\2\2\u010b\u010f\5&\24\2\u010c\u010e\5")
        buf.write("\u0084C\2\u010d\u010c\3\2\2\2\u010e\u0111\3\2\2\2\u010f")
        buf.write("\u010d\3\2\2\2\u010f\u0110\3\2\2\2\u0110\23\3\2\2\2\u0111")
        buf.write("\u010f\3\2\2\2\u0112\u0113\79\2\2\u0113\u0114\5f\64\2")
        buf.write("\u0114\u0115\5\24\13\2\u0115\u0119\3\2\2\2\u0116\u0117")
        buf.write("\79\2\2\u0117\u0119\5f\64\2\u0118\u0112\3\2\2\2\u0118")
        buf.write("\u0116\3\2\2\2\u0119\25\3\2\2\2\u011a\u011b\7\f\2\2\u011b")
        buf.write("\u011c\79\2\2\u011c\u0120\7\16\2\2\u011d\u011f\5\u0084")
        buf.write("C\2\u011e\u011d\3\2\2\2\u011f\u0122\3\2\2\2\u0120\u011e")
        buf.write("\3\2\2\2\u0120\u0121\3\2\2\2\u0121\u0123\3\2\2\2\u0122")
        buf.write("\u0120\3\2\2\2\u0123\u0127\7\63\2\2\u0124\u0126\5\u0084")
        buf.write("C\2\u0125\u0124\3\2\2\2\u0126\u0129\3\2\2\2\u0127\u0125")
        buf.write("\3\2\2\2\u0127\u0128\3\2\2\2\u0128\u012b\3\2\2\2\u0129")
        buf.write("\u0127\3\2\2\2\u012a\u012c\5\30\r\2\u012b\u012a\3\2\2")
        buf.write("\2\u012b\u012c\3\2\2\2\u012c\u012d\3\2\2\2\u012d\u012f")
        buf.write("\7\64\2\2\u012e\u0130\7\67\2\2\u012f\u012e\3\2\2\2\u012f")
        buf.write("\u0130\3\2\2\2\u0130\u0134\3\2\2\2\u0131\u0133\5\u0084")
        buf.write("C\2\u0132\u0131\3\2\2\2\u0133\u0136\3\2\2\2\u0134\u0132")
        buf.write("\3\2\2\2\u0134\u0135\3\2\2\2\u0135\27\3\2\2\2\u0136\u0134")
        buf.write("\3\2\2\2\u0137\u0138\5\32\16\2\u0138\u0139\5\30\r\2\u0139")
        buf.write("\u013c\3\2\2\2\u013a\u013c\5\32\16\2\u013b\u0137\3\2\2")
        buf.write("\2\u013b\u013a\3\2\2\2\u013c\31\3\2\2\2\u013d\u013e\7")
        buf.write("9\2\2\u013e\u013f\7\61\2\2\u013f\u0140\5\34\17\2\u0140")
        buf.write("\u0142\7\62\2\2\u0141\u0143\5b\62\2\u0142\u0141\3\2\2")
        buf.write("\2\u0142\u0143\3\2\2\2\u0143\u0145\3\2\2\2\u0144\u0146")
        buf.write("\7\67\2\2\u0145\u0144\3\2\2\2\u0145\u0146\3\2\2\2\u0146")
        buf.write("\u014a\3\2\2\2\u0147\u0149\5\u0084C\2\u0148\u0147\3\2")
        buf.write("\2\2\u0149\u014c\3\2\2\2\u014a\u0148\3\2\2\2\u014a\u014b")
        buf.write("\3\2\2\2\u014b\33\3\2\2\2\u014c\u014a\3\2\2\2\u014d\u014e")
        buf.write("\5\36\20\2\u014e\u014f\78\2\2\u014f\u0150\5\34\17\2\u0150")
        buf.write("\u0153\3\2\2\2\u0151\u0153\5\36\20\2\u0152\u014d\3\2\2")
        buf.write("\2\u0152\u0151\3\2\2\2\u0153\35\3\2\2\2\u0154\u0156\7")
        buf.write("9\2\2\u0155\u0157\5b\62\2\u0156\u0155\3\2\2\2\u0156\u0157")
        buf.write("\3\2\2\2\u0157\u015a\3\2\2\2\u0158\u015a\3\2\2\2\u0159")
        buf.write("\u0154\3\2\2\2\u0159\u0158\3\2\2\2\u015a\37\3\2\2\2\u015b")
        buf.write("\u015c\7\13\2\2\u015c\u015d\79\2\2\u015d\u015e\7\61\2")
        buf.write("\2\u015e\u015f\5\"\22\2\u015f\u0161\7\62\2\2\u0160\u0162")
        buf.write("\5b\62\2\u0161\u0160\3\2\2\2\u0161\u0162\3\2\2\2\u0162")
        buf.write("\u0163\3\2\2\2\u0163\u0167\5&\24\2\u0164\u0166\5\u0084")
        buf.write("C\2\u0165\u0164\3\2\2\2\u0166\u0169\3\2\2\2\u0167\u0165")
        buf.write("\3\2\2\2\u0167\u0168\3\2\2\2\u0168!\3\2\2\2\u0169\u0167")
        buf.write("\3\2\2\2\u016a\u016b\5$\23\2\u016b\u016c\78\2\2\u016c")
        buf.write("\u016d\5\"\22\2\u016d\u0170\3\2\2\2\u016e\u0170\5$\23")
        buf.write("\2\u016f\u016a\3\2\2\2\u016f\u016e\3\2\2\2\u0170#\3\2")
        buf.write("\2\2\u0171\u0172\79\2\2\u0172\u0175\5b\62\2\u0173\u0175")
        buf.write("\3\2\2\2\u0174\u0171\3\2\2\2\u0174\u0173\3\2\2\2\u0175")
        buf.write("%\3\2\2\2\u0176\u017a\7\63\2\2\u0177\u0179\5\u0084C\2")
        buf.write("\u0178\u0177\3\2\2\2\u0179\u017c\3\2\2\2\u017a\u0178\3")
        buf.write("\2\2\2\u017a\u017b\3\2\2\2\u017b\u017e\3\2\2\2\u017c\u017a")
        buf.write("\3\2\2\2\u017d\u017f\5(\25\2\u017e\u017d\3\2\2\2\u017e")
        buf.write("\u017f\3\2\2\2\u017f\u0180\3\2\2\2\u0180\u0184\7\64\2")
        buf.write("\2\u0181\u0183\5\u0084C\2\u0182\u0181\3\2\2\2\u0183\u0186")
        buf.write("\3\2\2\2\u0184\u0182\3\2\2\2\u0184\u0185\3\2\2\2\u0185")
        buf.write("\'\3\2\2\2\u0186\u0184\3\2\2\2\u0187\u0188\5*\26\2\u0188")
        buf.write("\u0189\5(\25\2\u0189\u018c\3\2\2\2\u018a\u018c\5*\26\2")
        buf.write("\u018b\u0187\3\2\2\2\u018b\u018a\3\2\2\2\u018c)\3\2\2")
        buf.write("\2\u018d\u0196\5,\27\2\u018e\u0196\5.\30\2\u018f\u0196")
        buf.write("\5\66\34\2\u0190\u0196\5> \2\u0191\u0196\5D#\2\u0192\u0196")
        buf.write("\5H%\2\u0193\u0196\5F$\2\u0194\u0196\5J&\2\u0195\u018d")
        buf.write("\3\2\2\2\u0195\u018e\3\2\2\2\u0195\u018f\3\2\2\2\u0195")
        buf.write("\u0190\3\2\2\2\u0195\u0191\3\2\2\2\u0195\u0192\3\2\2\2")
        buf.write("\u0195\u0193\3\2\2\2\u0195\u0194\3\2\2\2\u0196+\3\2\2")
        buf.write("\2\u0197\u019b\5\b\5\2\u0198\u019a\5\u0084C\2\u0199\u0198")
        buf.write("\3\2\2\2\u019a\u019d\3\2\2\2\u019b\u0199\3\2\2\2\u019b")
        buf.write("\u019c\3\2\2\2\u019c\u01a6\3\2\2\2\u019d\u019b\3\2\2\2")
        buf.write("\u019e\u01a2\5\n\6\2\u019f\u01a1\5\u0084C\2\u01a0\u019f")
        buf.write("\3\2\2\2\u01a1\u01a4\3\2\2\2\u01a2\u01a0\3\2\2\2\u01a2")
        buf.write("\u01a3\3\2\2\2\u01a3\u01a6\3\2\2\2\u01a4\u01a2\3\2\2\2")
        buf.write("\u01a5\u0197\3\2\2\2\u01a5\u019e\3\2\2\2\u01a6-\3\2\2")
        buf.write("\2\u01a7\u01a8\5\60\31\2\u01a8\u01a9\5\64\33\2\u01a9\u01ab")
        buf.write("\5N(\2\u01aa\u01ac\7\67\2\2\u01ab\u01aa\3\2\2\2\u01ab")
        buf.write("\u01ac\3\2\2\2\u01ac\u01b0\3\2\2\2\u01ad\u01af\5\u0084")
        buf.write("C\2\u01ae\u01ad\3\2\2\2\u01af\u01b2\3\2\2\2\u01b0\u01ae")
        buf.write("\3\2\2\2\u01b0\u01b1\3\2\2\2\u01b1/\3\2\2\2\u01b2\u01b0")
        buf.write("\3\2\2\2\u01b3\u01b4\5\62\32\2\u01b4\u01b5\5\60\31\2\u01b5")
        buf.write("\u01b8\3\2\2\2\u01b6\u01b8\5\62\32\2\u01b7\u01b3\3\2\2")
        buf.write("\2\u01b7\u01b6\3\2\2\2\u01b8\61\3\2\2\2\u01b9\u01bd\5")
        buf.write("l\67\2\u01ba\u01bd\79\2\2\u01bb\u01bd\7/\2\2\u01bc\u01b9")
        buf.write("\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bc\u01bb\3\2\2\2\u01bd")
        buf.write("\63\3\2\2\2\u01be\u01bf\t\2\2\2\u01bf\65\3\2\2\2\u01c0")
        buf.write("\u01c1\7\7\2\2\u01c1\u01c2\7\61\2\2\u01c2\u01c3\5N(\2")
        buf.write("\u01c3\u01c7\7\62\2\2\u01c4\u01c6\5\u0084C\2\u01c5\u01c4")
        buf.write("\3\2\2\2\u01c6\u01c9\3\2\2\2\u01c7\u01c5\3\2\2\2\u01c7")
        buf.write("\u01c8\3\2\2\2\u01c8\u01ca\3\2\2\2\u01c9\u01c7\3\2\2\2")
        buf.write("\u01ca\u01cc\5&\24\2\u01cb\u01cd\58\35\2\u01cc\u01cb\3")
        buf.write("\2\2\2\u01cc\u01cd\3\2\2\2\u01cd\u01cf\3\2\2\2\u01ce\u01d0")
        buf.write("\5<\37\2\u01cf\u01ce\3\2\2\2\u01cf\u01d0\3\2\2\2\u01d0")
        buf.write("\u01d4\3\2\2\2\u01d1\u01d3\5\u0084C\2\u01d2\u01d1\3\2")
        buf.write("\2\2\u01d3\u01d6\3\2\2\2\u01d4\u01d2\3\2\2\2\u01d4\u01d5")
        buf.write("\3\2\2\2\u01d5\67\3\2\2\2\u01d6\u01d4\3\2\2\2\u01d7\u01d8")
        buf.write("\5:\36\2\u01d8\u01d9\58\35\2\u01d9\u01dc\3\2\2\2\u01da")
        buf.write("\u01dc\5:\36\2\u01db\u01d7\3\2\2\2\u01db\u01da\3\2\2\2")
        buf.write("\u01dc9\3\2\2\2\u01dd\u01de\7\b\2\2\u01de\u01df\7\7\2")
        buf.write("\2\u01df\u01e0\7\61\2\2\u01e0\u01e1\5N(\2\u01e1\u01e5")
        buf.write("\7\62\2\2\u01e2\u01e4\5\u0084C\2\u01e3\u01e2\3\2\2\2\u01e4")
        buf.write("\u01e7\3\2\2\2\u01e5\u01e3\3\2\2\2\u01e5\u01e6\3\2\2\2")
        buf.write("\u01e6\u01e8\3\2\2\2\u01e7\u01e5\3\2\2\2\u01e8\u01e9\5")
        buf.write("&\24\2\u01e9;\3\2\2\2\u01ea\u01ee\7\b\2\2\u01eb\u01ed")
        buf.write("\5\u0084C\2\u01ec\u01eb\3\2\2\2\u01ed\u01f0\3\2\2\2\u01ee")
        buf.write("\u01ec\3\2\2\2\u01ee\u01ef\3\2\2\2\u01ef\u01f1\3\2\2\2")
        buf.write("\u01f0\u01ee\3\2\2\2\u01f1\u01f2\5&\24\2\u01f2=\3\2\2")
        buf.write("\2\u01f3\u01f4\7\t\2\2\u01f4\u01f8\5N(\2\u01f5\u01f7\5")
        buf.write("\u0084C\2\u01f6\u01f5\3\2\2\2\u01f7\u01fa\3\2\2\2\u01f8")
        buf.write("\u01f6\3\2\2\2\u01f8\u01f9\3\2\2\2\u01f9\u01fb\3\2\2\2")
        buf.write("\u01fa\u01f8\3\2\2\2\u01fb\u01ff\5&\24\2\u01fc\u01fe\5")
        buf.write("\u0084C\2\u01fd\u01fc\3\2\2\2\u01fe\u0201\3\2\2\2\u01ff")
        buf.write("\u01fd\3\2\2\2\u01ff\u0200\3\2\2\2\u0200\u0227\3\2\2\2")
        buf.write("\u0201\u01ff\3\2\2\2\u0202\u0203\7\t\2\2\u0203\u0204\5")
        buf.write("@!\2\u0204\u0205\5N(\2\u0205\u0206\7\67\2\2\u0206\u020a")
        buf.write("\5.\30\2\u0207\u0209\5\u0084C\2\u0208\u0207\3\2\2\2\u0209")
        buf.write("\u020c\3\2\2\2\u020a\u0208\3\2\2\2\u020a\u020b\3\2\2\2")
        buf.write("\u020b\u020d\3\2\2\2\u020c\u020a\3\2\2\2\u020d\u0211\5")
        buf.write("&\24\2\u020e\u0210\5\u0084C\2\u020f\u020e\3\2\2\2\u0210")
        buf.write("\u0213\3\2\2\2\u0211\u020f\3\2\2\2\u0211\u0212\3\2\2\2")
        buf.write("\u0212\u0227\3\2\2\2\u0213\u0211\3\2\2\2\u0214\u0215\7")
        buf.write("\t\2\2\u0215\u0216\79\2\2\u0216\u0217\78\2\2\u0217\u0218")
        buf.write("\5B\"\2\u0218\u021c\5N(\2\u0219\u021b\5\u0084C\2\u021a")
        buf.write("\u0219\3\2\2\2\u021b\u021e\3\2\2\2\u021c\u021a\3\2\2\2")
        buf.write("\u021c\u021d\3\2\2\2\u021d\u021f\3\2\2\2\u021e\u021c\3")
        buf.write("\2\2\2\u021f\u0223\5&\24\2\u0220\u0222\5\u0084C\2\u0221")
        buf.write("\u0220\3\2\2\2\u0222\u0225\3\2\2\2\u0223\u0221\3\2\2\2")
        buf.write("\u0223\u0224\3\2\2\2\u0224\u0227\3\2\2\2\u0225\u0223\3")
        buf.write("\2\2\2\u0226\u01f3\3\2\2\2\u0226\u0202\3\2\2\2\u0226\u0214")
        buf.write("\3\2\2\2\u0227?\3\2\2\2\u0228\u022b\5.\30\2\u0229\u022b")
        buf.write("\5\b\5\2\u022a\u0228\3\2\2\2\u022a\u0229\3\2\2\2\u022b")
        buf.write("A\3\2\2\2\u022c\u022d\79\2\2\u022d\u022e\7\3\2\2\u022e")
        buf.write("\u022f\7\27\2\2\u022fC\3\2\2\2\u0230\u0233\7\26\2\2\u0231")
        buf.write("\u0234\7\67\2\2\u0232\u0234\5\u0084C\2\u0233\u0231\3\2")
        buf.write("\2\2\u0233\u0232\3\2\2\2\u0234\u0238\3\2\2\2\u0235\u0237")
        buf.write("\5\u0084C\2\u0236\u0235\3\2\2\2\u0237\u023a\3\2\2\2\u0238")
        buf.write("\u0236\3\2\2\2\u0238\u0239\3\2\2\2\u0239E\3\2\2\2\u023a")
        buf.write("\u0238\3\2\2\2\u023b\u023d\5\60\31\2\u023c\u023b\3\2\2")
        buf.write("\2\u023c\u023d\3\2\2\2\u023d\u023e\3\2\2\2\u023e\u023f")
        buf.write("\79\2\2\u023f\u0241\7\61\2\2\u0240\u0242\5L\'\2\u0241")
        buf.write("\u0240\3\2\2\2\u0241\u0242\3\2\2\2\u0242\u0243\3\2\2\2")
        buf.write("\u0243\u0246\7\62\2\2\u0244\u0247\7\67\2\2\u0245\u0247")
        buf.write("\5\u0084C\2\u0246\u0244\3\2\2\2\u0246\u0245\3\2\2\2\u0247")
        buf.write("\u024b\3\2\2\2\u0248\u024a\5\u0084C\2\u0249\u0248\3\2")
        buf.write("\2\2\u024a\u024d\3\2\2\2\u024b\u0249\3\2\2\2\u024b\u024c")
        buf.write("\3\2\2\2\u024cG\3\2\2\2\u024d\u024b\3\2\2\2\u024e\u0251")
        buf.write("\7\25\2\2\u024f\u0252\7\67\2\2\u0250\u0252\5\u0084C\2")
        buf.write("\u0251\u024f\3\2\2\2\u0251\u0250\3\2\2\2\u0252\u0256\3")
        buf.write("\2\2\2\u0253\u0255\5\u0084C\2\u0254\u0253\3\2\2\2\u0255")
        buf.write("\u0258\3\2\2\2\u0256\u0254\3\2\2\2\u0256\u0257\3\2\2\2")
        buf.write("\u0257I\3\2\2\2\u0258\u0256\3\2\2\2\u0259\u025b\7\n\2")
        buf.write("\2\u025a\u025c\5N(\2\u025b\u025a\3\2\2\2\u025b\u025c\3")
        buf.write("\2\2\2\u025c\u025f\3\2\2\2\u025d\u0260\7\67\2\2\u025e")
        buf.write("\u0260\5\u0084C\2\u025f\u025d\3\2\2\2\u025f\u025e\3\2")
        buf.write("\2\2\u0260\u0264\3\2\2\2\u0261\u0263\5\u0084C\2\u0262")
        buf.write("\u0261\3\2\2\2\u0263\u0266\3\2\2\2\u0264\u0262\3\2\2\2")
        buf.write("\u0264\u0265\3\2\2\2\u0265K\3\2\2\2\u0266\u0264\3\2\2")
        buf.write("\2\u0267\u0268\5N(\2\u0268\u0269\78\2\2\u0269\u026a\5")
        buf.write("L\'\2\u026a\u026d\3\2\2\2\u026b\u026d\5N(\2\u026c\u0267")
        buf.write("\3\2\2\2\u026c\u026b\3\2\2\2\u026dM\3\2\2\2\u026e\u026f")
        buf.write("\b(\1\2\u026f\u0270\5P)\2\u0270\u0276\3\2\2\2\u0271\u0272")
        buf.write("\f\4\2\2\u0272\u0273\7\'\2\2\u0273\u0275\5P)\2\u0274\u0271")
        buf.write("\3\2\2\2\u0275\u0278\3\2\2\2\u0276\u0274\3\2\2\2\u0276")
        buf.write("\u0277\3\2\2\2\u0277O\3\2\2\2\u0278\u0276\3\2\2\2\u0279")
        buf.write("\u027a\b)\1\2\u027a\u027b\5R*\2\u027b\u0281\3\2\2\2\u027c")
        buf.write("\u027d\f\4\2\2\u027d\u027e\7(\2\2\u027e\u0280\5R*\2\u027f")
        buf.write("\u027c\3\2\2\2\u0280\u0283\3\2\2\2\u0281\u027f\3\2\2\2")
        buf.write("\u0281\u0282\3\2\2\2\u0282Q\3\2\2\2\u0283\u0281\3\2\2")
        buf.write("\2\u0284\u0285\b*\1\2\u0285\u0286\5T+\2\u0286\u028c\3")
        buf.write("\2\2\2\u0287\u0288\f\4\2\2\u0288\u0289\7\6\2\2\u0289\u028b")
        buf.write("\5T+\2\u028a\u0287\3\2\2\2\u028b\u028e\3\2\2\2\u028c\u028a")
        buf.write("\3\2\2\2\u028c\u028d\3\2\2\2\u028dS\3\2\2\2\u028e\u028c")
        buf.write("\3\2\2\2\u028f\u0290\b+\1\2\u0290\u0291\5V,\2\u0291\u0297")
        buf.write("\3\2\2\2\u0292\u0293\f\4\2\2\u0293\u0294\t\3\2\2\u0294")
        buf.write("\u0296\5V,\2\u0295\u0292\3\2\2\2\u0296\u0299\3\2\2\2\u0297")
        buf.write("\u0295\3\2\2\2\u0297\u0298\3\2\2\2\u0298U\3\2\2\2\u0299")
        buf.write("\u0297\3\2\2\2\u029a\u029b\b,\1\2\u029b\u029c\5X-\2\u029c")
        buf.write("\u02a2\3\2\2\2\u029d\u029e\f\4\2\2\u029e\u029f\t\4\2\2")
        buf.write("\u029f\u02a1\5X-\2\u02a0\u029d\3\2\2\2\u02a1\u02a4\3\2")
        buf.write("\2\2\u02a2\u02a0\3\2\2\2\u02a2\u02a3\3\2\2\2\u02a3W\3")
        buf.write("\2\2\2\u02a4\u02a2\3\2\2\2\u02a5\u02a6\t\5\2\2\u02a6\u02a9")
        buf.write("\5X-\2\u02a7\u02a9\5Z.\2\u02a8\u02a5\3\2\2\2\u02a8\u02a7")
        buf.write("\3\2\2\2\u02a9Y\3\2\2\2\u02aa\u02ab\b.\1\2\u02ab\u02ae")
        buf.write("\5^\60\2\u02ac\u02ae\5\\/\2\u02ad\u02aa\3\2\2\2\u02ad")
        buf.write("\u02ac\3\2\2\2\u02ae\u02c2\3\2\2\2\u02af\u02b0\f\6\2\2")
        buf.write("\u02b0\u02b1\7\65\2\2\u02b1\u02b2\5N(\2\u02b2\u02b3\7")
        buf.write("\66\2\2\u02b3\u02c1\3\2\2\2\u02b4\u02b5\f\5\2\2\u02b5")
        buf.write("\u02b7\7/\2\2\u02b6\u02b8\5N(\2\u02b7\u02b6\3\2\2\2\u02b7")
        buf.write("\u02b8\3\2\2\2\u02b8\u02be\3\2\2\2\u02b9\u02bb\7\61\2")
        buf.write("\2\u02ba\u02bc\5L\'\2\u02bb\u02ba\3\2\2\2\u02bb\u02bc")
        buf.write("\3\2\2\2\u02bc\u02bd\3\2\2\2\u02bd\u02bf\7\62\2\2\u02be")
        buf.write("\u02b9\3\2\2\2\u02be\u02bf\3\2\2\2\u02bf\u02c1\3\2\2\2")
        buf.write("\u02c0\u02af\3\2\2\2\u02c0\u02b4\3\2\2\2\u02c1\u02c4\3")
        buf.write("\2\2\2\u02c2\u02c0\3\2\2\2\u02c2\u02c3\3\2\2\2\u02c3[")
        buf.write("\3\2\2\2\u02c4\u02c2\3\2\2\2\u02c5\u02cc\5p9\2\u02c6\u02cc")
        buf.write("\79\2\2\u02c7\u02c8\7\61\2\2\u02c8\u02c9\5N(\2\u02c9\u02ca")
        buf.write("\7\62\2\2\u02ca\u02cc\3\2\2\2\u02cb\u02c5\3\2\2\2\u02cb")
        buf.write("\u02c6\3\2\2\2\u02cb\u02c7\3\2\2\2\u02cc]\3\2\2\2\u02cd")
        buf.write("\u02ce\79\2\2\u02ce\u02d0\7\61\2\2\u02cf\u02d1\5L\'\2")
        buf.write("\u02d0\u02cf\3\2\2\2\u02d0\u02d1\3\2\2\2\u02d1\u02d2\3")
        buf.write("\2\2\2\u02d2\u02d4\7\62\2\2\u02d3\u02d5\5\u0084C\2\u02d4")
        buf.write("\u02d3\3\2\2\2\u02d4\u02d5\3\2\2\2\u02d5_\3\2\2\2\u02d6")
        buf.write("\u02d7\5N(\2\u02d7\u02d8\7/\2\2\u02d8\u02da\79\2\2\u02d9")
        buf.write("\u02db\7\61\2\2\u02da\u02d9\3\2\2\2\u02da\u02db\3\2\2")
        buf.write("\2\u02db\u02dd\3\2\2\2\u02dc\u02de\5L\'\2\u02dd\u02dc")
        buf.write("\3\2\2\2\u02dd\u02de\3\2\2\2\u02de\u02e0\3\2\2\2\u02df")
        buf.write("\u02e1\7\62\2\2\u02e0\u02df\3\2\2\2\u02e0\u02e1\3\2\2")
        buf.write("\2\u02e1a\3\2\2\2\u02e2\u02e6\5d\63\2\u02e3\u02e6\5f\64")
        buf.write("\2\u02e4\u02e6\5l\67\2\u02e5\u02e2\3\2\2\2\u02e5\u02e3")
        buf.write("\3\2\2\2\u02e5\u02e4\3\2\2\2\u02e6c\3\2\2\2\u02e7\u02e8")
        buf.write("\t\6\2\2\u02e8e\3\2\2\2\u02e9\u02ec\5h\65\2\u02ea\u02ec")
        buf.write("\5j\66\2\u02eb\u02e9\3\2\2\2\u02eb\u02ea\3\2\2\2\u02ec")
        buf.write("g\3\2\2\2\u02ed\u02ee\79\2\2\u02eei\3\2\2\2\u02ef\u02f0")
        buf.write("\79\2\2\u02f0k\3\2\2\2\u02f1\u02f3\5n8\2\u02f2\u02f4\5")
        buf.write("b\62\2\u02f3\u02f2\3\2\2\2\u02f3\u02f4\3\2\2\2\u02f4m")
        buf.write("\3\2\2\2\u02f5\u02f6\7\65\2\2\u02f6\u02f7\5|?\2\u02f7")
        buf.write("\u02f8\7\66\2\2\u02f8\u02f9\5n8\2\u02f9\u02ff\3\2\2\2")
        buf.write("\u02fa\u02fb\7\65\2\2\u02fb\u02fc\5|?\2\u02fc\u02fd\7")
        buf.write("\66\2\2\u02fd\u02ff\3\2\2\2\u02fe\u02f5\3\2\2\2\u02fe")
        buf.write("\u02fa\3\2\2\2\u02ffo\3\2\2\2\u0300\u0307\5|?\2\u0301")
        buf.write("\u0307\7>\2\2\u0302\u0307\7?\2\2\u0303\u0307\5\u0080A")
        buf.write("\2\u0304\u0307\5x=\2\u0305\u0307\5r:\2\u0306\u0300\3\2")
        buf.write("\2\2\u0306\u0301\3\2\2\2\u0306\u0302\3\2\2\2\u0306\u0303")
        buf.write("\3\2\2\2\u0306\u0304\3\2\2\2\u0306\u0305\3\2\2\2\u0307")
        buf.write("q\3\2\2\2\u0308\u0309\79\2\2\u0309\u030b\7\63\2\2\u030a")
        buf.write("\u030c\5t;\2\u030b\u030a\3\2\2\2\u030b\u030c\3\2\2\2\u030c")
        buf.write("\u030d\3\2\2\2\u030d\u030e\7\64\2\2\u030es\3\2\2\2\u030f")
        buf.write("\u0311\5v<\2\u0310\u0312\5\u0084C\2\u0311\u0310\3\2\2")
        buf.write("\2\u0311\u0312\3\2\2\2\u0312\u031a\3\2\2\2\u0313\u0314")
        buf.write("\5v<\2\u0314\u0315\78\2\2\u0315\u0317\5t;\2\u0316\u0318")
        buf.write("\5\u0084C\2\u0317\u0316\3\2\2\2\u0317\u0318\3\2\2\2\u0318")
        buf.write("\u031a\3\2\2\2\u0319\u030f\3\2\2\2\u0319\u0313\3\2\2\2")
        buf.write("\u031au\3\2\2\2\u031b\u031c\79\2\2\u031c\u031d\7\60\2")
        buf.write("\2\u031d\u031e\5N(\2\u031ew\3\2\2\2\u031f\u0320\5l\67")
        buf.write("\2\u0320\u0322\7\63\2\2\u0321\u0323\5z>\2\u0322\u0321")
        buf.write("\3\2\2\2\u0322\u0323\3\2\2\2\u0323\u0324\3\2\2\2\u0324")
        buf.write("\u0325\7\64\2\2\u0325y\3\2\2\2\u0326\u0327\7\63\2\2\u0327")
        buf.write("\u0331\5z>\2\u0328\u032a\5L\'\2\u0329\u032b\7\64\2\2\u032a")
        buf.write("\u0329\3\2\2\2\u032a\u032b\3\2\2\2\u032b\u032e\3\2\2\2")
        buf.write("\u032c\u032d\78\2\2\u032d\u032f\5z>\2\u032e\u032c\3\2")
        buf.write("\2\2\u032e\u032f\3\2\2\2\u032f\u0331\3\2\2\2\u0330\u0326")
        buf.write("\3\2\2\2\u0330\u0328\3\2\2\2\u0331{\3\2\2\2\u0332\u0333")
        buf.write("\t\7\2\2\u0333}\3\2\2\2\u0334\u0335\7>\2\2\u0335\177\3")
        buf.write("\2\2\2\u0336\u0337\t\b\2\2\u0337\u0081\3\2\2\2\u0338\u0339")
        buf.write("\7?\2\2\u0339\u0083\3\2\2\2\u033a\u033c\7\4\2\2\u033b")
        buf.write("\u033a\3\2\2\2\u033b\u033c\3\2\2\2\u033c\u033d\3\2\2\2")
        buf.write("\u033d\u033e\7\5\2\2\u033e\u0085\3\2\2\2q\u0089\u0094")
        buf.write("\u009b\u009e\u00a6\u00ab\u00af\u00b5\u00bb\u00c0\u00c5")
        buf.write("\u00cf\u00d3\u00d8\u00dd\u00e4\u00e9\u00ef\u00f6\u00fb")
        buf.write("\u00fe\u0109\u010f\u0118\u0120\u0127\u012b\u012f\u0134")
        buf.write("\u013b\u0142\u0145\u014a\u0152\u0156\u0159\u0161\u0167")
        buf.write("\u016f\u0174\u017a\u017e\u0184\u018b\u0195\u019b\u01a2")
        buf.write("\u01a5\u01ab\u01b0\u01b7\u01bc\u01c7\u01cc\u01cf\u01d4")
        buf.write("\u01db\u01e5\u01ee\u01f8\u01ff\u020a\u0211\u021c\u0223")
        buf.write("\u0226\u022a\u0233\u0238\u023c\u0241\u0246\u024b\u0251")
        buf.write("\u0256\u025b\u025f\u0264\u026c\u0276\u0281\u028c\u0297")
        buf.write("\u02a2\u02a8\u02ad\u02b7\u02bb\u02be\u02c0\u02c2\u02cb")
        buf.write("\u02d0\u02d4\u02da\u02dd\u02e0\u02e5\u02eb\u02f3\u02fe")
        buf.write("\u0306\u030b\u0311\u0317\u0319\u0322\u032a\u032e\u0330")
        buf.write("\u033b")
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
                      "SEMI", "COMMA", "ID", "DEC_LIT", "BIN_LIT", "OCT_LIT", 
                      "HEX_LIT", "FLOAT_LIT", "STR_LIT", "BOOL_LIT", "WS", 
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
    RULE_method_para = 9
    RULE_interface_decl = 10
    RULE_interface_method_list = 11
    RULE_interface_method = 12
    RULE_interface_para_list = 13
    RULE_interface_para = 14
    RULE_func_decl = 15
    RULE_list_para = 16
    RULE_para = 17
    RULE_block_statement = 18
    RULE_list_statement = 19
    RULE_statement = 20
    RULE_declared_statement = 21
    RULE_assign_statement = 22
    RULE_lhs_list = 23
    RULE_lhs = 24
    RULE_ass_operator = 25
    RULE_if_statement = 26
    RULE_list_else_if_statement = 27
    RULE_else_if_statement = 28
    RULE_else_statement = 29
    RULE_for_statement = 30
    RULE_init_for_statement = 31
    RULE_value_assign = 32
    RULE_break_statement = 33
    RULE_call_statement = 34
    RULE_continue_statement = 35
    RULE_return_statement = 36
    RULE_list_expr = 37
    RULE_expr = 38
    RULE_and_expr = 39
    RULE_rela_expr = 40
    RULE_add_expr = 41
    RULE_mul_expr = 42
    RULE_unary_expr = 43
    RULE_primary_expr = 44
    RULE_exprd = 45
    RULE_func_call = 46
    RULE_method_call = 47
    RULE_types = 48
    RULE_primitive_types = 49
    RULE_composite_types = 50
    RULE_struct_type = 51
    RULE_interface_type = 52
    RULE_arr_type = 53
    RULE_index_operator = 54
    RULE_literals = 55
    RULE_struct_lit = 56
    RULE_list_field = 57
    RULE_field = 58
    RULE_arr_lit = 59
    RULE_arr_list = 60
    RULE_int_lit = 61
    RULE_float_lit = 62
    RULE_bool_lit = 63
    RULE_str_lit = 64
    RULE_newline = 65

    ruleNames =  [ "program", "decllist", "decl", "variable_decl", "const_decl", 
                   "struct_decl", "struct_fields", "struct_field", "method_decl", 
                   "method_para", "interface_decl", "interface_method_list", 
                   "interface_method", "interface_para_list", "interface_para", 
                   "func_decl", "list_para", "para", "block_statement", 
                   "list_statement", "statement", "declared_statement", 
                   "assign_statement", "lhs_list", "lhs", "ass_operator", 
                   "if_statement", "list_else_if_statement", "else_if_statement", 
                   "else_statement", "for_statement", "init_for_statement", 
                   "value_assign", "break_statement", "call_statement", 
                   "continue_statement", "return_statement", "list_expr", 
                   "expr", "and_expr", "rela_expr", "add_expr", "mul_expr", 
                   "unary_expr", "primary_expr", "exprd", "func_call", "method_call", 
                   "types", "primitive_types", "composite_types", "struct_type", 
                   "interface_type", "arr_type", "index_operator", "literals", 
                   "struct_lit", "list_field", "field", "arr_lit", "arr_list", 
                   "int_lit", "float_lit", "bool_lit", "str_lit", "newline" ]

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
    DEC_LIT=56
    BIN_LIT=57
    OCT_LIT=58
    HEX_LIT=59
    FLOAT_LIT=60
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
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.T__1 or _la==MiniGoParser.T__2:
                self.state = 132
                self.newline()
                self.state = 137
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 138
            self.decllist()
            self.state = 139
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

        def decl(self):
            return self.getTypedRuleContext(MiniGoParser.DeclContext,0)


        def decllist(self):
            return self.getTypedRuleContext(MiniGoParser.DecllistContext,0)


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
        try:
            self.state = 156
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                self.decl()
                self.state = 142
                self.decllist()
                self.state = 146
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 143
                        self.newline() 
                    self.state = 148
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 149
                self.decl()
                self.state = 153
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 150
                        self.newline() 
                    self.state = 155
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

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

        def variable_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Variable_declContext,0)


        def const_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declContext,0)


        def func_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Func_declContext,0)


        def method_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Method_declContext,0)


        def struct_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_declContext,0)


        def interface_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_declContext,0)


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
            self.state = 164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self.variable_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 159
                self.const_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 160
                self.func_decl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 161
                self.method_decl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 162
                self.struct_decl()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 163
                self.interface_decl()
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

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def types(self):
            return self.getTypedRuleContext(MiniGoParser.TypesContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def list_expr(self):
            return self.getTypedRuleContext(MiniGoParser.List_exprContext,0)


        def newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.NewlineContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.NewlineContext,i)


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
            self.state = 166
            self.match(MiniGoParser.VAR)
            self.state = 167
            self.match(MiniGoParser.ID)
            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.LBRACK) | (1 << MiniGoParser.ID))) != 0):
                self.state = 168
                self.types()


            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ASSIGN:
                self.state = 171
                self.match(MiniGoParser.ASSIGN)
                self.state = 172
                self.list_expr()


            self.state = 175
            self.match(MiniGoParser.SEMI)
            self.state = 179
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 176
                    self.newline() 
                self.state = 181
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

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

        def list_expr(self):
            return self.getTypedRuleContext(MiniGoParser.List_exprContext,0)


        def types(self):
            return self.getTypedRuleContext(MiniGoParser.TypesContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.NewlineContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.NewlineContext,i)


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
            self.state = 182
            self.match(MiniGoParser.CONST)
            self.state = 183
            self.match(MiniGoParser.ID)
            self.state = 185
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.LBRACK) | (1 << MiniGoParser.ID))) != 0):
                self.state = 184
                self.types()


            self.state = 187
            self.match(MiniGoParser.ASSIGN)
            self.state = 188
            self.list_expr()
            self.state = 190
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.SEMI:
                self.state = 189
                self.match(MiniGoParser.SEMI)


            self.state = 195
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 192
                    self.newline() 
                self.state = 197
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

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

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.NewlineContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.NewlineContext,i)


        def struct_fields(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_fieldsContext,0)


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
            self.state = 198
            self.match(MiniGoParser.TYPE)
            self.state = 199
            self.match(MiniGoParser.ID)
            self.state = 200
            self.match(MiniGoParser.STRUCT)
            self.state = 201
            self.match(MiniGoParser.LBRACE)
            self.state = 205
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.T__1 or _la==MiniGoParser.T__2:
                self.state = 202
                self.newline()
                self.state = 207
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 208
                self.struct_fields()


            self.state = 211
            self.match(MiniGoParser.RBRACE)
            self.state = 214
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SEMI]:
                self.state = 212
                self.match(MiniGoParser.SEMI)
                pass
            elif token in [MiniGoParser.T__1, MiniGoParser.T__2]:
                self.state = 213
                self.newline()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 219
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 216
                    self.newline() 
                self.state = 221
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

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

        def struct_field(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_fieldContext,0)


        def struct_fields(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_fieldsContext,0)


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
        try:
            self.state = 226
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 222
                self.struct_field()
                self.state = 223
                self.struct_fields()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 225
                self.struct_field()
                pass


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

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def primitive_types(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_typesContext,0)


        def arr_type(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_typeContext,0)


        def newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.NewlineContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.NewlineContext,i)


        def composite_types(self):
            return self.getTypedRuleContext(MiniGoParser.Composite_typesContext,0)


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
        self._la = 0 # Token type
        try:
            self.state = 252
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 228
                self.match(MiniGoParser.ID)
                self.state = 231
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.NIL]:
                    self.state = 229
                    self.primitive_types()
                    pass
                elif token in [MiniGoParser.LBRACK]:
                    self.state = 230
                    self.arr_type()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 233
                self.match(MiniGoParser.SEMI)
                self.state = 237
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.T__1 or _la==MiniGoParser.T__2:
                    self.state = 234
                    self.newline()
                    self.state = 239
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 240
                self.match(MiniGoParser.ID)
                self.state = 241
                self.composite_types()
                self.state = 244
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.SEMI]:
                    self.state = 242
                    self.match(MiniGoParser.SEMI)
                    pass
                elif token in [MiniGoParser.T__1, MiniGoParser.T__2]:
                    self.state = 243
                    self.newline()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 249
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.T__1 or _la==MiniGoParser.T__2:
                    self.state = 246
                    self.newline()
                    self.state = 251
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


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

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LPAREN)
            else:
                return self.getToken(MiniGoParser.LPAREN, i)

        def method_para(self):
            return self.getTypedRuleContext(MiniGoParser.Method_paraContext,0)


        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RPAREN)
            else:
                return self.getToken(MiniGoParser.RPAREN, i)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def list_para(self):
            return self.getTypedRuleContext(MiniGoParser.List_paraContext,0)


        def block_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Block_statementContext,0)


        def types(self):
            return self.getTypedRuleContext(MiniGoParser.TypesContext,0)


        def newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.NewlineContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.NewlineContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.match(MiniGoParser.FUNC)
            self.state = 255
            self.match(MiniGoParser.LPAREN)
            self.state = 256
            self.method_para()
            self.state = 257
            self.match(MiniGoParser.RPAREN)
            self.state = 258
            self.match(MiniGoParser.ID)
            self.state = 259
            self.match(MiniGoParser.LPAREN)
            self.state = 260
            self.list_para()
            self.state = 261
            self.match(MiniGoParser.RPAREN)
            self.state = 263
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.LBRACK) | (1 << MiniGoParser.ID))) != 0):
                self.state = 262
                self.types()


            self.state = 265
            self.block_statement()
            self.state = 269
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 266
                    self.newline() 
                self.state = 271
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_paraContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def composite_types(self):
            return self.getTypedRuleContext(MiniGoParser.Composite_typesContext,0)


        def method_para(self):
            return self.getTypedRuleContext(MiniGoParser.Method_paraContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_para

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_para" ):
                return visitor.visitMethod_para(self)
            else:
                return visitor.visitChildren(self)




    def method_para(self):

        localctx = MiniGoParser.Method_paraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_method_para)
        try:
            self.state = 278
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 272
                self.match(MiniGoParser.ID)
                self.state = 273
                self.composite_types()
                self.state = 274
                self.method_para()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 276
                self.match(MiniGoParser.ID)
                self.state = 277
                self.composite_types()
                pass


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

        def newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.NewlineContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.NewlineContext,i)


        def interface_method_list(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_method_listContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_decl" ):
                return visitor.visitInterface_decl(self)
            else:
                return visitor.visitChildren(self)




    def interface_decl(self):

        localctx = MiniGoParser.Interface_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_interface_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.match(MiniGoParser.TYPE)
            self.state = 281
            self.match(MiniGoParser.ID)
            self.state = 282
            self.match(MiniGoParser.INTERFACE)
            self.state = 286
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.T__1 or _la==MiniGoParser.T__2:
                self.state = 283
                self.newline()
                self.state = 288
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 289
            self.match(MiniGoParser.LBRACE)
            self.state = 293
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.T__1 or _la==MiniGoParser.T__2:
                self.state = 290
                self.newline()
                self.state = 295
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 297
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 296
                self.interface_method_list()


            self.state = 299
            self.match(MiniGoParser.RBRACE)
            self.state = 301
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.SEMI:
                self.state = 300
                self.match(MiniGoParser.SEMI)


            self.state = 306
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 303
                    self.newline() 
                self.state = 308
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_method_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def interface_method(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_methodContext,0)


        def interface_method_list(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_method_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_method_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_method_list" ):
                return visitor.visitInterface_method_list(self)
            else:
                return visitor.visitChildren(self)




    def interface_method_list(self):

        localctx = MiniGoParser.Interface_method_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_interface_method_list)
        try:
            self.state = 313
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 309
                self.interface_method()
                self.state = 310
                self.interface_method_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 312
                self.interface_method()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def interface_para_list(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_para_listContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def types(self):
            return self.getTypedRuleContext(MiniGoParser.TypesContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.NewlineContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.NewlineContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_method" ):
                return visitor.visitInterface_method(self)
            else:
                return visitor.visitChildren(self)




    def interface_method(self):

        localctx = MiniGoParser.Interface_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_interface_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.match(MiniGoParser.ID)
            self.state = 316
            self.match(MiniGoParser.LPAREN)
            self.state = 317
            self.interface_para_list()
            self.state = 318
            self.match(MiniGoParser.RPAREN)
            self.state = 320
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 319
                self.types()


            self.state = 323
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.SEMI:
                self.state = 322
                self.match(MiniGoParser.SEMI)


            self.state = 328
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.T__1 or _la==MiniGoParser.T__2:
                self.state = 325
                self.newline()
                self.state = 330
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_para_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def interface_para(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_paraContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def interface_para_list(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_para_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_para_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_para_list" ):
                return visitor.visitInterface_para_list(self)
            else:
                return visitor.visitChildren(self)




    def interface_para_list(self):

        localctx = MiniGoParser.Interface_para_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_interface_para_list)
        try:
            self.state = 336
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 331
                self.interface_para()
                self.state = 332
                self.match(MiniGoParser.COMMA)
                self.state = 333
                self.interface_para_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 335
                self.interface_para()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_paraContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def types(self):
            return self.getTypedRuleContext(MiniGoParser.TypesContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_para

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_para" ):
                return visitor.visitInterface_para(self)
            else:
                return visitor.visitChildren(self)




    def interface_para(self):

        localctx = MiniGoParser.Interface_paraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_interface_para)
        self._la = 0 # Token type
        try:
            self.state = 343
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 338
                self.match(MiniGoParser.ID)
                self.state = 340
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.LBRACK) | (1 << MiniGoParser.ID))) != 0):
                    self.state = 339
                    self.types()


                pass
            elif token in [MiniGoParser.RPAREN, MiniGoParser.COMMA]:
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


    class Func_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def list_para(self):
            return self.getTypedRuleContext(MiniGoParser.List_paraContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def block_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Block_statementContext,0)


        def types(self):
            return self.getTypedRuleContext(MiniGoParser.TypesContext,0)


        def newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.NewlineContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.NewlineContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decl" ):
                return visitor.visitFunc_decl(self)
            else:
                return visitor.visitChildren(self)




    def func_decl(self):

        localctx = MiniGoParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_func_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            self.match(MiniGoParser.FUNC)
            self.state = 346
            self.match(MiniGoParser.ID)
            self.state = 347
            self.match(MiniGoParser.LPAREN)
            self.state = 348
            self.list_para()
            self.state = 349
            self.match(MiniGoParser.RPAREN)
            self.state = 351
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.LBRACK) | (1 << MiniGoParser.ID))) != 0):
                self.state = 350
                self.types()


            self.state = 353
            self.block_statement()
            self.state = 357
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 354
                    self.newline() 
                self.state = 359
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_paraContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def para(self):
            return self.getTypedRuleContext(MiniGoParser.ParaContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_para(self):
            return self.getTypedRuleContext(MiniGoParser.List_paraContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_para

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_para" ):
                return visitor.visitList_para(self)
            else:
                return visitor.visitChildren(self)




    def list_para(self):

        localctx = MiniGoParser.List_paraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_list_para)
        try:
            self.state = 365
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 360
                self.para()
                self.state = 361
                self.match(MiniGoParser.COMMA)
                self.state = 362
                self.list_para()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 364
                self.para()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def types(self):
            return self.getTypedRuleContext(MiniGoParser.TypesContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_para

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara" ):
                return visitor.visitPara(self)
            else:
                return visitor.visitChildren(self)




    def para(self):

        localctx = MiniGoParser.ParaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_para)
        try:
            self.state = 370
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 367
                self.match(MiniGoParser.ID)
                self.state = 368
                self.types()
                pass
            elif token in [MiniGoParser.RPAREN, MiniGoParser.COMMA]:
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


    class Block_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.NewlineContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.NewlineContext,i)


        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_block_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_statement" ):
                return visitor.visitBlock_statement(self)
            else:
                return visitor.visitChildren(self)




    def block_statement(self):

        localctx = MiniGoParser.Block_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_block_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
            self.match(MiniGoParser.LBRACE)
            self.state = 376
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.T__1 or _la==MiniGoParser.T__2:
                self.state = 373
                self.newline()
                self.state = 378
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 380
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.DOT) | (1 << MiniGoParser.LBRACK) | (1 << MiniGoParser.ID))) != 0):
                self.state = 379
                self.list_statement()


            self.state = 382
            self.match(MiniGoParser.RBRACE)
            self.state = 386
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 383
                    self.newline() 
                self.state = 388
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

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
        self.enterRule(localctx, 38, self.RULE_list_statement)
        try:
            self.state = 393
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 389
                self.statement()
                self.state = 390
                self.list_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 392
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


        def if_statement(self):
            return self.getTypedRuleContext(MiniGoParser.If_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(MiniGoParser.For_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Continue_statementContext,0)


        def call_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Call_statementContext,0)


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
        self.enterRule(localctx, 40, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.state = 395
                self.declared_statement()
                pass

            elif la_ == 2:
                self.state = 396
                self.assign_statement()
                pass

            elif la_ == 3:
                self.state = 397
                self.if_statement()
                pass

            elif la_ == 4:
                self.state = 398
                self.for_statement()
                pass

            elif la_ == 5:
                self.state = 399
                self.break_statement()
                pass

            elif la_ == 6:
                self.state = 400
                self.continue_statement()
                pass

            elif la_ == 7:
                self.state = 401
                self.call_statement()
                pass

            elif la_ == 8:
                self.state = 402
                self.return_statement()
                pass


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


        def newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.NewlineContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.NewlineContext,i)


        def const_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_declared_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclared_statement" ):
                return visitor.visitDeclared_statement(self)
            else:
                return visitor.visitChildren(self)




    def declared_statement(self):

        localctx = MiniGoParser.Declared_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_declared_statement)
        self._la = 0 # Token type
        try:
            self.state = 419
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 405
                self.variable_decl()
                self.state = 409
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.T__1 or _la==MiniGoParser.T__2:
                    self.state = 406
                    self.newline()
                    self.state = 411
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [MiniGoParser.CONST]:
                self.enterOuterAlt(localctx, 2)
                self.state = 412
                self.const_decl()
                self.state = 416
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.T__1 or _la==MiniGoParser.T__2:
                    self.state = 413
                    self.newline()
                    self.state = 418
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

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


    class Assign_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs_list(self):
            return self.getTypedRuleContext(MiniGoParser.Lhs_listContext,0)


        def ass_operator(self):
            return self.getTypedRuleContext(MiniGoParser.Ass_operatorContext,0)


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
            return MiniGoParser.RULE_assign_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_statement" ):
                return visitor.visitAssign_statement(self)
            else:
                return visitor.visitChildren(self)




    def assign_statement(self):

        localctx = MiniGoParser.Assign_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_assign_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 421
            self.lhs_list()
            self.state = 422
            self.ass_operator()
            self.state = 423
            self.expr(0)
            self.state = 425
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.SEMI:
                self.state = 424
                self.match(MiniGoParser.SEMI)


            self.state = 430
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,49,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 427
                    self.newline() 
                self.state = 432
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,49,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lhs_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def lhs_list(self):
            return self.getTypedRuleContext(MiniGoParser.Lhs_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_lhs_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs_list" ):
                return visitor.visitLhs_list(self)
            else:
                return visitor.visitChildren(self)




    def lhs_list(self):

        localctx = MiniGoParser.Lhs_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_lhs_list)
        try:
            self.state = 437
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 433
                self.lhs()
                self.state = 434
                self.lhs_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 436
                self.lhs()
                pass


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

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = MiniGoParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_lhs)
        try:
            self.state = 442
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LBRACK]:
                self.enterOuterAlt(localctx, 1)
                self.state = 439
                self.arr_type()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 440
                self.match(MiniGoParser.ID)
                pass
            elif token in [MiniGoParser.DOT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 441
                self.match(MiniGoParser.DOT)
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
        self.enterRule(localctx, 50, self.RULE_ass_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 444
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


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def block_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Block_statementContext,0)


        def newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.NewlineContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.NewlineContext,i)


        def list_else_if_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_else_if_statementContext,0)


        def else_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Else_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = MiniGoParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 446
            self.match(MiniGoParser.IF)
            self.state = 447
            self.match(MiniGoParser.LPAREN)
            self.state = 448
            self.expr(0)
            self.state = 449
            self.match(MiniGoParser.RPAREN)
            self.state = 453
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.T__1 or _la==MiniGoParser.T__2:
                self.state = 450
                self.newline()
                self.state = 455
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 456
            self.block_statement()
            self.state = 458
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.state = 457
                self.list_else_if_statement()


            self.state = 461
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ELSE:
                self.state = 460
                self.else_statement()


            self.state = 466
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.T__1 or _la==MiniGoParser.T__2:
                self.state = 463
                self.newline()
                self.state = 468
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_else_if_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def else_if_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Else_if_statementContext,0)


        def list_else_if_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_else_if_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_else_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_else_if_statement" ):
                return visitor.visitList_else_if_statement(self)
            else:
                return visitor.visitChildren(self)




    def list_else_if_statement(self):

        localctx = MiniGoParser.List_else_if_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_list_else_if_statement)
        try:
            self.state = 473
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,56,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 469
                self.else_if_statement()
                self.state = 470
                self.list_else_if_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 472
                self.else_if_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_if_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def block_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Block_statementContext,0)


        def newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.NewlineContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.NewlineContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_else_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_if_statement" ):
                return visitor.visitElse_if_statement(self)
            else:
                return visitor.visitChildren(self)




    def else_if_statement(self):

        localctx = MiniGoParser.Else_if_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_else_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 475
            self.match(MiniGoParser.ELSE)
            self.state = 476
            self.match(MiniGoParser.IF)
            self.state = 477
            self.match(MiniGoParser.LPAREN)
            self.state = 478
            self.expr(0)
            self.state = 479
            self.match(MiniGoParser.RPAREN)
            self.state = 483
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.T__1 or _la==MiniGoParser.T__2:
                self.state = 480
                self.newline()
                self.state = 485
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 486
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def block_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Block_statementContext,0)


        def newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.NewlineContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.NewlineContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_else_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_statement" ):
                return visitor.visitElse_statement(self)
            else:
                return visitor.visitChildren(self)




    def else_statement(self):

        localctx = MiniGoParser.Else_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_else_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 488
            self.match(MiniGoParser.ELSE)
            self.state = 492
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.T__1 or _la==MiniGoParser.T__2:
                self.state = 489
                self.newline()
                self.state = 494
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 495
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def block_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Block_statementContext,0)


        def newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.NewlineContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.NewlineContext,i)


        def init_for_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Init_for_statementContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def assign_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_statementContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def value_assign(self):
            return self.getTypedRuleContext(MiniGoParser.Value_assignContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = MiniGoParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_for_statement)
        self._la = 0 # Token type
        try:
            self.state = 548
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,65,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 497
                self.match(MiniGoParser.FOR)
                self.state = 498
                self.expr(0)
                self.state = 502
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.T__1 or _la==MiniGoParser.T__2:
                    self.state = 499
                    self.newline()
                    self.state = 504
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 505
                self.block_statement()
                self.state = 509
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.T__1 or _la==MiniGoParser.T__2:
                    self.state = 506
                    self.newline()
                    self.state = 511
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 512
                self.match(MiniGoParser.FOR)
                self.state = 513
                self.init_for_statement()
                self.state = 514
                self.expr(0)
                self.state = 515
                self.match(MiniGoParser.SEMI)
                self.state = 516
                self.assign_statement()
                self.state = 520
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.T__1 or _la==MiniGoParser.T__2:
                    self.state = 517
                    self.newline()
                    self.state = 522
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 523
                self.block_statement()
                self.state = 527
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.T__1 or _la==MiniGoParser.T__2:
                    self.state = 524
                    self.newline()
                    self.state = 529
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 530
                self.match(MiniGoParser.FOR)
                self.state = 531
                self.match(MiniGoParser.ID)
                self.state = 532
                self.match(MiniGoParser.COMMA)
                self.state = 533
                self.value_assign()
                self.state = 534
                self.expr(0)
                self.state = 538
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.T__1 or _la==MiniGoParser.T__2:
                    self.state = 535
                    self.newline()
                    self.state = 540
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 541
                self.block_statement()
                self.state = 545
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.T__1 or _la==MiniGoParser.T__2:
                    self.state = 542
                    self.newline()
                    self.state = 547
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Init_for_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_statementContext,0)


        def variable_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Variable_declContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_init_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInit_for_statement" ):
                return visitor.visitInit_for_statement(self)
            else:
                return visitor.visitChildren(self)




    def init_for_statement(self):

        localctx = MiniGoParser.Init_for_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_init_for_statement)
        try:
            self.state = 552
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.DOT, MiniGoParser.LBRACK, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 550
                self.assign_statement()
                pass
            elif token in [MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 551
                self.variable_decl()
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


    class Value_assignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def RANGE(self):
            return self.getToken(MiniGoParser.RANGE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_value_assign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue_assign" ):
                return visitor.visitValue_assign(self)
            else:
                return visitor.visitChildren(self)




    def value_assign(self):

        localctx = MiniGoParser.Value_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_value_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 554
            self.match(MiniGoParser.ID)
            self.state = 555
            self.match(MiniGoParser.T__0)
            self.state = 556
            self.match(MiniGoParser.RANGE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MiniGoParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.NewlineContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.NewlineContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = MiniGoParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_break_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 558
            self.match(MiniGoParser.BREAK)
            self.state = 561
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SEMI]:
                self.state = 559
                self.match(MiniGoParser.SEMI)
                pass
            elif token in [MiniGoParser.T__1, MiniGoParser.T__2]:
                self.state = 560
                self.newline()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 566
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.T__1 or _la==MiniGoParser.T__2:
                self.state = 563
                self.newline()
                self.state = 568
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_statementContext(ParserRuleContext):
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

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.NewlineContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.NewlineContext,i)


        def lhs_list(self):
            return self.getTypedRuleContext(MiniGoParser.Lhs_listContext,0)


        def list_expr(self):
            return self.getTypedRuleContext(MiniGoParser.List_exprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_call_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_statement" ):
                return visitor.visitCall_statement(self)
            else:
                return visitor.visitChildren(self)




    def call_statement(self):

        localctx = MiniGoParser.Call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_call_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 570
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,69,self._ctx)
            if la_ == 1:
                self.state = 569
                self.lhs_list()


            self.state = 572
            self.match(MiniGoParser.ID)
            self.state = 573
            self.match(MiniGoParser.LPAREN)
            self.state = 575
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.MINUS) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LBRACK) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.DEC_LIT) | (1 << MiniGoParser.BIN_LIT) | (1 << MiniGoParser.OCT_LIT) | (1 << MiniGoParser.HEX_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STR_LIT))) != 0):
                self.state = 574
                self.list_expr()


            self.state = 577
            self.match(MiniGoParser.RPAREN)
            self.state = 580
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SEMI]:
                self.state = 578
                self.match(MiniGoParser.SEMI)
                pass
            elif token in [MiniGoParser.T__1, MiniGoParser.T__2]:
                self.state = 579
                self.newline()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 585
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.T__1 or _la==MiniGoParser.T__2:
                self.state = 582
                self.newline()
                self.state = 587
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MiniGoParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.NewlineContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.NewlineContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = MiniGoParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_continue_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 588
            self.match(MiniGoParser.CONTINUE)
            self.state = 591
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SEMI]:
                self.state = 589
                self.match(MiniGoParser.SEMI)
                pass
            elif token in [MiniGoParser.T__1, MiniGoParser.T__2]:
                self.state = 590
                self.newline()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 596
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.T__1 or _la==MiniGoParser.T__2:
                self.state = 593
                self.newline()
                self.state = 598
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.NewlineContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.NewlineContext,i)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = MiniGoParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 599
            self.match(MiniGoParser.RETURN)
            self.state = 601
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.MINUS) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LBRACK) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.DEC_LIT) | (1 << MiniGoParser.BIN_LIT) | (1 << MiniGoParser.OCT_LIT) | (1 << MiniGoParser.HEX_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STR_LIT))) != 0):
                self.state = 600
                self.expr(0)


            self.state = 605
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SEMI]:
                self.state = 603
                self.match(MiniGoParser.SEMI)
                pass
            elif token in [MiniGoParser.T__1, MiniGoParser.T__2]:
                self.state = 604
                self.newline()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 610
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.T__1 or _la==MiniGoParser.T__2:
                self.state = 607
                self.newline()
                self.state = 612
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
        self.enterRule(localctx, 74, self.RULE_list_expr)
        try:
            self.state = 618
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,78,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 613
                self.expr(0)
                self.state = 614
                self.match(MiniGoParser.COMMA)
                self.state = 615
                self.list_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 617
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
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 621
            self.and_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 628
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,79,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 623
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 624
                    self.match(MiniGoParser.OR)
                    self.state = 625
                    self.and_expr(0) 
                self.state = 630
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,79,self._ctx)

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
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_and_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 632
            self.rela_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 639
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,80,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.And_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_and_expr)
                    self.state = 634
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 635
                    self.match(MiniGoParser.AND)
                    self.state = 636
                    self.rela_expr(0) 
                self.state = 641
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,80,self._ctx)

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
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_rela_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 643
            self.add_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 650
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,81,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Rela_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_rela_expr)
                    self.state = 645
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 646
                    self.match(MiniGoParser.REL)
                    self.state = 647
                    self.add_expr(0) 
                self.state = 652
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,81,self._ctx)

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
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_add_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 654
            self.mul_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 661
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,82,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Add_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_add_expr)
                    self.state = 656
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 657
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.ADD or _la==MiniGoParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 658
                    self.mul_expr(0) 
                self.state = 663
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,82,self._ctx)

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
        _startState = 84
        self.enterRecursionRule(localctx, 84, self.RULE_mul_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 665
            self.unary_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 672
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,83,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Mul_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_mul_expr)
                    self.state = 667
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 668
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 669
                    self.unary_expr() 
                self.state = 674
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,83,self._ctx)

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
        self.enterRule(localctx, 86, self.RULE_unary_expr)
        self._la = 0 # Token type
        try:
            self.state = 678
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NOT, MiniGoParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 675
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.NOT or _la==MiniGoParser.MINUS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 676
                self.unary_expr()
                pass
            elif token in [MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.LPAREN, MiniGoParser.LBRACK, MiniGoParser.ID, MiniGoParser.DEC_LIT, MiniGoParser.BIN_LIT, MiniGoParser.OCT_LIT, MiniGoParser.HEX_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STR_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 677
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

        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def exprd(self):
            return self.getTypedRuleContext(MiniGoParser.ExprdContext,0)


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

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def list_expr(self):
            return self.getTypedRuleContext(MiniGoParser.List_exprContext,0)


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
        _startState = 88
        self.enterRecursionRule(localctx, 88, self.RULE_primary_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 683
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,85,self._ctx)
            if la_ == 1:
                self.state = 681
                self.func_call()
                pass

            elif la_ == 2:
                self.state = 682
                self.exprd()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 704
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,90,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 702
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,89,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Primary_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_primary_expr)
                        self.state = 685
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 686
                        self.match(MiniGoParser.LBRACK)
                        self.state = 687
                        self.expr(0)
                        self.state = 688
                        self.match(MiniGoParser.RBRACK)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Primary_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_primary_expr)
                        self.state = 690
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 691
                        self.match(MiniGoParser.DOT)
                        self.state = 693
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,86,self._ctx)
                        if la_ == 1:
                            self.state = 692
                            self.expr(0)


                        self.state = 700
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,88,self._ctx)
                        if la_ == 1:
                            self.state = 695
                            self.match(MiniGoParser.LPAREN)
                            self.state = 697
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.MINUS) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LBRACK) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.DEC_LIT) | (1 << MiniGoParser.BIN_LIT) | (1 << MiniGoParser.OCT_LIT) | (1 << MiniGoParser.HEX_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STR_LIT))) != 0):
                                self.state = 696
                                self.list_expr()


                            self.state = 699
                            self.match(MiniGoParser.RPAREN)


                        pass

             
                self.state = 706
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,90,self._ctx)

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
        self.enterRule(localctx, 90, self.RULE_exprd)
        try:
            self.state = 713
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,91,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 707
                self.literals()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 708
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 709
                self.match(MiniGoParser.LPAREN)
                self.state = 710
                self.expr(0)
                self.state = 711
                self.match(MiniGoParser.RPAREN)
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
        self.enterRule(localctx, 92, self.RULE_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 715
            self.match(MiniGoParser.ID)
            self.state = 716
            self.match(MiniGoParser.LPAREN)
            self.state = 718
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.MINUS) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LBRACK) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.DEC_LIT) | (1 << MiniGoParser.BIN_LIT) | (1 << MiniGoParser.OCT_LIT) | (1 << MiniGoParser.HEX_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STR_LIT))) != 0):
                self.state = 717
                self.list_expr()


            self.state = 720
            self.match(MiniGoParser.RPAREN)
            self.state = 722
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,93,self._ctx)
            if la_ == 1:
                self.state = 721
                self.newline()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


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
            return MiniGoParser.RULE_method_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_call" ):
                return visitor.visitMethod_call(self)
            else:
                return visitor.visitChildren(self)




    def method_call(self):

        localctx = MiniGoParser.Method_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_method_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 724
            self.expr(0)
            self.state = 725
            self.match(MiniGoParser.DOT)
            self.state = 726
            self.match(MiniGoParser.ID)
            self.state = 728
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,94,self._ctx)
            if la_ == 1:
                self.state = 727
                self.match(MiniGoParser.LPAREN)


            self.state = 731
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.MINUS) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LBRACK) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.DEC_LIT) | (1 << MiniGoParser.BIN_LIT) | (1 << MiniGoParser.OCT_LIT) | (1 << MiniGoParser.HEX_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STR_LIT))) != 0):
                self.state = 730
                self.list_expr()


            self.state = 734
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.RPAREN:
                self.state = 733
                self.match(MiniGoParser.RPAREN)


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


        def arr_type(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_types

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypes" ):
                return visitor.visitTypes(self)
            else:
                return visitor.visitChildren(self)




    def types(self):

        localctx = MiniGoParser.TypesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_types)
        try:
            self.state = 739
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.NIL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 736
                self.primitive_types()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 737
                self.composite_types()
                pass
            elif token in [MiniGoParser.LBRACK]:
                self.enterOuterAlt(localctx, 3)
                self.state = 738
                self.arr_type()
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
        self.enterRule(localctx, 98, self.RULE_primitive_types)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 741
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
        self.enterRule(localctx, 100, self.RULE_composite_types)
        try:
            self.state = 745
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,98,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 743
                self.struct_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 744
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
        self.enterRule(localctx, 102, self.RULE_struct_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 747
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
        self.enterRule(localctx, 104, self.RULE_interface_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 749
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
        self.enterRule(localctx, 106, self.RULE_arr_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 751
            self.index_operator()
            self.state = 753
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,99,self._ctx)
            if la_ == 1:
                self.state = 752
                self.types()


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

        def int_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Int_litContext,0)


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
        self.enterRule(localctx, 108, self.RULE_index_operator)
        try:
            self.state = 764
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,100,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 755
                self.match(MiniGoParser.LBRACK)
                self.state = 756
                self.int_lit()
                self.state = 757
                self.match(MiniGoParser.RBRACK)
                self.state = 758
                self.index_operator()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 760
                self.match(MiniGoParser.LBRACK)
                self.state = 761
                self.int_lit()
                self.state = 762
                self.match(MiniGoParser.RBRACK)
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


        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def STR_LIT(self):
            return self.getToken(MiniGoParser.STR_LIT, 0)

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
        self.enterRule(localctx, 110, self.RULE_literals)
        try:
            self.state = 772
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.DEC_LIT, MiniGoParser.BIN_LIT, MiniGoParser.OCT_LIT, MiniGoParser.HEX_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 766
                self.int_lit()
                pass
            elif token in [MiniGoParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 767
                self.match(MiniGoParser.FLOAT_LIT)
                pass
            elif token in [MiniGoParser.STR_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 768
                self.match(MiniGoParser.STR_LIT)
                pass
            elif token in [MiniGoParser.TRUE, MiniGoParser.FALSE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 769
                self.bool_lit()
                pass
            elif token in [MiniGoParser.LBRACK]:
                self.enterOuterAlt(localctx, 5)
                self.state = 770
                self.arr_lit()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 771
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
        self.enterRule(localctx, 112, self.RULE_struct_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 774
            self.match(MiniGoParser.ID)
            self.state = 775
            self.match(MiniGoParser.LBRACE)
            self.state = 777
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 776
                self.list_field()


            self.state = 779
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
        self.enterRule(localctx, 114, self.RULE_list_field)
        try:
            self.state = 791
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,105,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 781
                self.field()
                self.state = 783
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,103,self._ctx)
                if la_ == 1:
                    self.state = 782
                    self.newline()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 785
                self.field()
                self.state = 786
                self.match(MiniGoParser.COMMA)
                self.state = 787
                self.list_field()
                self.state = 789
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,104,self._ctx)
                if la_ == 1:
                    self.state = 788
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
        self.enterRule(localctx, 116, self.RULE_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 793
            self.match(MiniGoParser.ID)
            self.state = 794
            self.match(MiniGoParser.COLON)
            self.state = 795
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

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def arr_list(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arr_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_lit" ):
                return visitor.visitArr_lit(self)
            else:
                return visitor.visitChildren(self)




    def arr_lit(self):

        localctx = MiniGoParser.Arr_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_arr_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 797
            self.arr_type()
            self.state = 798
            self.match(MiniGoParser.LBRACE)
            self.state = 800
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.MINUS) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LBRACE) | (1 << MiniGoParser.LBRACK) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.DEC_LIT) | (1 << MiniGoParser.BIN_LIT) | (1 << MiniGoParser.OCT_LIT) | (1 << MiniGoParser.HEX_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STR_LIT))) != 0):
                self.state = 799
                self.arr_list()


            self.state = 802
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

        def arr_list(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_listContext,0)


        def list_expr(self):
            return self.getTypedRuleContext(MiniGoParser.List_exprContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

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
        self.enterRule(localctx, 120, self.RULE_arr_list)
        self._la = 0 # Token type
        try:
            self.state = 814
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LBRACE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 804
                self.match(MiniGoParser.LBRACE)
                self.state = 805
                self.arr_list()
                pass
            elif token in [MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.NOT, MiniGoParser.MINUS, MiniGoParser.LPAREN, MiniGoParser.LBRACK, MiniGoParser.ID, MiniGoParser.DEC_LIT, MiniGoParser.BIN_LIT, MiniGoParser.OCT_LIT, MiniGoParser.HEX_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STR_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 806
                self.list_expr()
                self.state = 808
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,107,self._ctx)
                if la_ == 1:
                    self.state = 807
                    self.match(MiniGoParser.RBRACE)


                self.state = 812
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.COMMA:
                    self.state = 810
                    self.match(MiniGoParser.COMMA)
                    self.state = 811
                    self.arr_list()


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
        self.enterRule(localctx, 122, self.RULE_int_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 816
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
        self.enterRule(localctx, 124, self.RULE_float_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 818
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
        self.enterRule(localctx, 126, self.RULE_bool_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 820
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
        self.enterRule(localctx, 128, self.RULE_str_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 822
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
        self.enterRule(localctx, 130, self.RULE_newline)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 825
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.T__1:
                self.state = 824
                self.match(MiniGoParser.T__1)


            self.state = 827
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
        self._predicates[38] = self.expr_sempred
        self._predicates[39] = self.and_expr_sempred
        self._predicates[40] = self.rela_expr_sempred
        self._predicates[41] = self.add_expr_sempred
        self._predicates[42] = self.mul_expr_sempred
        self._predicates[44] = self.primary_expr_sempred
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
         




