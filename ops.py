cores = {"azul":(1, 6, 14, 21, 22)
        ,"vermelho":(2, 5, 13, 15, 20)
        ,"verde":(9, 12, 16, 23, 25)
        ,"roxo":(3, 4, 10, 17, 18)
        ,"preto":(7, 8, 11, 19, 24)}

    print '_'*37
print '_'*37
print '| Azul     | {azul[0]:2} | {azul[1]:2} | {azul[2]:2} | {azul[3]:2} | {azul[4]:2} |'.format(**cores)
print '_'*37
print '| Vermelho | {vermelho[0]:2} | {vermelho[1]:2} | {vermelho[2]:2} | {vermelho[3]:2} | {vermelho[4]:2} |'.format(**cores)
print '_'*37
print '| Verde    | {verde[0]:2} | {verde[1]:2} | {verde[2]:2} | {verde[3]:2} | {verde[4]:2} |'.format(**cores)
print '_'*37
print '| Roxo     | {roxo[0]:2} | {roxo[1]:2} | {roxo[2]:2} | {roxo[3]:2} | {roxo[4]:2} |'.format(**cores)
print '_'*37
print '| Preto    | {preto[0]:2} | {preto[1]:2} | {preto[2]:2} | {preto[3]:2} | {preto[4]:2} |'.format(**cores)
print '_'*37


print '_'*37
for cor in cores.keys():
    print '| {0:8} | {1[0]:2} | {1[1]:2} | {1[2]:2} | {1[3]:2} | {1[4]:2} |'.format(cor, cores[cor])


for cor in cores.keys():
    print '| {:8} | '.format(cor)

