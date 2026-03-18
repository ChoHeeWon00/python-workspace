st = {"key":"value", "이름":"홍길동"}
print( st )
print( st["이름"] )
st["키"] = "값"
print( st )

list_ = []
list_.append( st ) # [{},{},{}]
print( type(list_) )

print( st.keys() )
list_ = list( st.keys() )
print( list_ )

print( st.items() )
for k, v in st.items():
    print(k,":",v)