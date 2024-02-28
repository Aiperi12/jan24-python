part = str (input("What is your partition ?: "))
serv = str (input("What is your service ?: "))
reg = str (input("What is your region ?: "))
acc = int (input("What is your account-id?: "))
res = int (input("What is your resource-id?: "))
print ("           ")

print(f' ARN format -->  arn:{part}:{serv}:{serv}:{acc}:{res}')