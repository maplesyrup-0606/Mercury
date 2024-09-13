println("Hello, World!")

x = 3.123142
x = "Hello, World!"
println(typeof(x))

s1 = "Hello, " # single line
s2 = """World! "hello" """ # multi-line
println(s1, s2)

#'apple' #error

x = 1
y = 2

println("Hello I am $x + $y years old")

s3 = string(s1, s2)
println(s3)
println(string(x, "Hello"))

println(s1*s2)

# Dictionaries

my_dict = Dict("Mercury" => 1, "David" => 2)
my_dict["Taeyang"] = 3
println(my_dict["Mercury"] + my_dict["David"])
println(my_dict["Taeyang"] * my_dict["David"])

x = pop!(my_dict, "David")
println(my_dict)
println(x)

my_tuple = (1, 2, 3)
println(my_tuple[1]) # Julia is 1 indexed not 0 indexed
# my_tuple[1] = 0 # error

# Arrays
my_arr = [1, 2, 3]
println(my_arr[1])
my_arr[1] = 0 # cannot change to different type though
println(my_arr)
println(typeof(my_arr))

arr = ["abd", 1, 123.1251]
print(typeof(arr))

print(pop!(arr))
print(arr)

push!(my_arr, 3)
println(my_arr)


print(rand(4,3)) # 1d length 4, 2nd length 3

function loop()
    i = 0 
    while i < 3
        println(i)
        i += 1
    end
end

loop()

function four() 
    for i in 1:3 #inclusive range
        println(i)
    end
end

four()

print(arr)

for i in arr
    println(i)
end

apple = zeros(4, 4)

# for i in 1:4
#     for j in 1:4
#         println(apple[i, j])
#     end
# end

for i in 1:4, j in 1:4
    println(apple[i, j])
end

C = [i + j for i in 1:4, j in 1:4]
print(C)

for n in 1:10
    A = [i + j for i in 1:n, j in 1:n]
    println(A)
end