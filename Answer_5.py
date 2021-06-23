s1 = "Nice to have it"
s2 = " here"
a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]

a.insert(0,s1)
a.append(s2)
print(a)

# Output = [ s1 + a + s2 ]