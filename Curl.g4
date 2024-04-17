grammar Curl;

curl: 'curl' args* uri;

args
    : method
    | header;

method
    : '-X' METHOD ;

header
    : '-H' '"' headerName ':' headerValue '"';

headerName: string;
headerValue: string;

uri
    : scheme '://' login? host (':' port)? ('/' path?)? query? frag? WS?
    ;

scheme
    : string
    ;

host
    : '/'? hostname
    ;

hostname
    : string         # DomainNameOrIPv4Host
    | '[' v6host ']' # IPv6Host
    ;

v6host
    : '::'? (string | DIGITS) ((':' | '::') (string | DIGITS))*
    ;

port
    : DIGITS
    ;

path
    : string ('/' string)* '/'?
    ;

user
    : string
    ;

login
    : user (':' password)? '@'
    ;

password
    : string
    ;

frag
    : '#' (string | DIGITS)
    ;

query
    : '?' search
    ;

search
    : searchparameter ('&' searchparameter)*
    ;

searchparameter
    : string ('=' (string | DIGITS | HEX))?
    ;

string
    : STRING
    | DIGITS
    ;


DIGITS
    : [0-9]+
    ;

METHOD
    : 'GET'
    | 'PUT'
    | 'POST'
    | 'PATCH'
    | 'DELETE'
    | 'OPTIONS'
    ;

HEX
    : ('%' [a-fA-F0-9] [a-fA-F0-9])+
    ;

STRING
    : ([a-zA-Z~0-9] | HEX) ([a-zA-Z0-9.+-] | HEX)*
    ;


WS : [ \t\r\n]+ -> skip ;