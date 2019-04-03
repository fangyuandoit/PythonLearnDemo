#集合（set）是一个无序的不重复元素序列。
#可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)


thisset = set(("Google", "Runoob", "Taobao"))

#添加元素
thisset.add("Facebook")
print(thisset)

#、移除元素
#thisset.remove("Taoba")  # 不存在会发生错误
#thisset.discard("Taobao") #移除集合中的元素，且如果元素不存在，不会发生错误
#print(thisset)

#我们也可以设置随机删除集合中的一个元素，语法格式如下： s.pop()
#x = thisset.pop()
#print(x)
#print(thisset)

#计算集合元素个数
i = len(thisset)
print(i)

#清空集合  s.clear()


#判断元素是否在集合中存在
print("Google" in thisset)


'''
集合内置方法完整列表
方法	描述
add()	为集合添加元素
clear()	移除集合中的所有元素
copy()	拷贝一个集合
difference()	返回多个集合的差集
difference_update()	移除集合中的元素，该元素在指定的集合也存在。
discard()	删除集合中指定的元素
intersection()	返回集合的交集
intersection_update()	删除集合中的元素，该元素在指定的集合中不存在。
isdisjoint()	判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。
issubset()	判断指定集合是否为该方法参数集合的子集。
issuperset()	判断该方法的参数集合是否为指定集合的子集
pop()	随机移除元素
remove()	移除指定元素
symmetric_difference()	返回两个集合中不重复的元素集合。
symmetric_difference_update()	移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。
union()	返回两个集合的并集
update()	给集合添加元素
'''











