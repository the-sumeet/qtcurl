# Generated from Curl.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CurlParser import CurlParser
else:
    from CurlParser import CurlParser

# This class defines a complete listener for a parse tree produced by CurlParser.
class CurlListener(ParseTreeListener):

    # Enter a parse tree produced by CurlParser#curl.
    def enterCurl(self, ctx:CurlParser.CurlContext):
        pass

    # Exit a parse tree produced by CurlParser#curl.
    def exitCurl(self, ctx:CurlParser.CurlContext):
        pass


    # Enter a parse tree produced by CurlParser#args.
    def enterArgs(self, ctx:CurlParser.ArgsContext):
        pass

    # Exit a parse tree produced by CurlParser#args.
    def exitArgs(self, ctx:CurlParser.ArgsContext):
        pass


    # Enter a parse tree produced by CurlParser#method.
    def enterMethod(self, ctx:CurlParser.MethodContext):
        pass

    # Exit a parse tree produced by CurlParser#method.
    def exitMethod(self, ctx:CurlParser.MethodContext):
        pass


    # Enter a parse tree produced by CurlParser#header.
    def enterHeader(self, ctx:CurlParser.HeaderContext):
        pass

    # Exit a parse tree produced by CurlParser#header.
    def exitHeader(self, ctx:CurlParser.HeaderContext):
        pass


    # Enter a parse tree produced by CurlParser#headerName.
    def enterHeaderName(self, ctx:CurlParser.HeaderNameContext):
        pass

    # Exit a parse tree produced by CurlParser#headerName.
    def exitHeaderName(self, ctx:CurlParser.HeaderNameContext):
        pass


    # Enter a parse tree produced by CurlParser#headerValue.
    def enterHeaderValue(self, ctx:CurlParser.HeaderValueContext):
        pass

    # Exit a parse tree produced by CurlParser#headerValue.
    def exitHeaderValue(self, ctx:CurlParser.HeaderValueContext):
        pass


    # Enter a parse tree produced by CurlParser#uri.
    def enterUri(self, ctx:CurlParser.UriContext):
        pass

    # Exit a parse tree produced by CurlParser#uri.
    def exitUri(self, ctx:CurlParser.UriContext):
        pass


    # Enter a parse tree produced by CurlParser#scheme.
    def enterScheme(self, ctx:CurlParser.SchemeContext):
        pass

    # Exit a parse tree produced by CurlParser#scheme.
    def exitScheme(self, ctx:CurlParser.SchemeContext):
        pass


    # Enter a parse tree produced by CurlParser#host.
    def enterHost(self, ctx:CurlParser.HostContext):
        pass

    # Exit a parse tree produced by CurlParser#host.
    def exitHost(self, ctx:CurlParser.HostContext):
        pass


    # Enter a parse tree produced by CurlParser#DomainNameOrIPv4Host.
    def enterDomainNameOrIPv4Host(self, ctx:CurlParser.DomainNameOrIPv4HostContext):
        pass

    # Exit a parse tree produced by CurlParser#DomainNameOrIPv4Host.
    def exitDomainNameOrIPv4Host(self, ctx:CurlParser.DomainNameOrIPv4HostContext):
        pass


    # Enter a parse tree produced by CurlParser#IPv6Host.
    def enterIPv6Host(self, ctx:CurlParser.IPv6HostContext):
        pass

    # Exit a parse tree produced by CurlParser#IPv6Host.
    def exitIPv6Host(self, ctx:CurlParser.IPv6HostContext):
        pass


    # Enter a parse tree produced by CurlParser#v6host.
    def enterV6host(self, ctx:CurlParser.V6hostContext):
        pass

    # Exit a parse tree produced by CurlParser#v6host.
    def exitV6host(self, ctx:CurlParser.V6hostContext):
        pass


    # Enter a parse tree produced by CurlParser#port.
    def enterPort(self, ctx:CurlParser.PortContext):
        pass

    # Exit a parse tree produced by CurlParser#port.
    def exitPort(self, ctx:CurlParser.PortContext):
        pass


    # Enter a parse tree produced by CurlParser#path.
    def enterPath(self, ctx:CurlParser.PathContext):
        pass

    # Exit a parse tree produced by CurlParser#path.
    def exitPath(self, ctx:CurlParser.PathContext):
        pass


    # Enter a parse tree produced by CurlParser#user.
    def enterUser(self, ctx:CurlParser.UserContext):
        pass

    # Exit a parse tree produced by CurlParser#user.
    def exitUser(self, ctx:CurlParser.UserContext):
        pass


    # Enter a parse tree produced by CurlParser#login.
    def enterLogin(self, ctx:CurlParser.LoginContext):
        pass

    # Exit a parse tree produced by CurlParser#login.
    def exitLogin(self, ctx:CurlParser.LoginContext):
        pass


    # Enter a parse tree produced by CurlParser#password.
    def enterPassword(self, ctx:CurlParser.PasswordContext):
        pass

    # Exit a parse tree produced by CurlParser#password.
    def exitPassword(self, ctx:CurlParser.PasswordContext):
        pass


    # Enter a parse tree produced by CurlParser#frag.
    def enterFrag(self, ctx:CurlParser.FragContext):
        pass

    # Exit a parse tree produced by CurlParser#frag.
    def exitFrag(self, ctx:CurlParser.FragContext):
        pass


    # Enter a parse tree produced by CurlParser#query.
    def enterQuery(self, ctx:CurlParser.QueryContext):
        pass

    # Exit a parse tree produced by CurlParser#query.
    def exitQuery(self, ctx:CurlParser.QueryContext):
        pass


    # Enter a parse tree produced by CurlParser#search.
    def enterSearch(self, ctx:CurlParser.SearchContext):
        pass

    # Exit a parse tree produced by CurlParser#search.
    def exitSearch(self, ctx:CurlParser.SearchContext):
        pass


    # Enter a parse tree produced by CurlParser#searchparameter.
    def enterSearchparameter(self, ctx:CurlParser.SearchparameterContext):
        pass

    # Exit a parse tree produced by CurlParser#searchparameter.
    def exitSearchparameter(self, ctx:CurlParser.SearchparameterContext):
        pass


    # Enter a parse tree produced by CurlParser#string.
    def enterString(self, ctx:CurlParser.StringContext):
        pass

    # Exit a parse tree produced by CurlParser#string.
    def exitString(self, ctx:CurlParser.StringContext):
        pass



del CurlParser