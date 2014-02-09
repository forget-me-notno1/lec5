a=[[1,2,3], [0,4,5], [6,3,1]]
n=len(a)
m=len(a[0])
sum=0
avg=0
max_row=[]
for i in range(n):
      max_elem=a[i][0]
      for j in range(m):
            sum+=a[i][j]
            if (j!=0) and (a[i][j]>max_elem):
                max_elem=a[i][j]
      max_row.append(max_elem)
avg=sum/(n*m)
print('сумма: ', sum)
print('среднее арифметическое: ', avg)
print('максимальные значения по строкам: ', max_row)
