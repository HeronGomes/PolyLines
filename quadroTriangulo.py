# -*- coding: utf-8 -*-

import numpy as np
import cv2 as cv


imagem = np.full((800,600,3),255,dtype='uint8')

paleta = [
    
    [255,255,255], #preto
    [0,0,0], #branco
    
    [25,217,217], #amarelo: ouro brilhante
    [0,127,255],  #vermelho: coral
    [204,153,50] #azul: Azul Celeste
    
    
    ]

seedPic = np.random.randint(1,1e6)
cont = 0;

while True:
        
    
    pontoA = (np.random.randint(0,600),np.random.randint(0,800))
    
    pontoB = (pontoA[0]+np.random.randint(1,200) ,pontoA[1]+np.random.randint(1,200))
    
    pontoC = (pontoB[0]+np.random.randint(1,200) , pontoB[1]+np.random.randint(1,200))
    
    
    pontos = np.array([pontoA,pontoB,pontoC])

    corRGB = ( paleta[np.random.randint(0,len(paleta))]  )
    
    cv.drawContours(image=imagem,
                   contours= [pontos],
                    contourIdx=0,
                    color=corRGB,
                    thickness=cv.FILLED)
    
    
    cv.drawContours(image=imagem,
                   contours= [pontos],
                    contourIdx=0,
                    color=(0,0,0),
                    thickness=2,
                    lineType=cv.LINE_AA)
    
    
    if cont == seedPic:
        break
    cont +=1
    
    # cv.imshow('Quadro',imagem)
        
    # tecla = cv.waitKey(200)
    # if tecla == ord('q'):
    #     cv.destroyAllWindows()
    #     break
    
imgAssinatura = np.zeros((50,600,3),np.uint8)
cv.putText(imgAssinatura,'Mine Painting: Heron TF Gomes',(140,25),cv.FONT_HERSHEY_SCRIPT_SIMPLEX ,1,(190,190,190),1,cv.LINE_AA )
cv.putText(imgAssinatura,'07/06/2020',(495,45),cv.FONT_HERSHEY_SCRIPT_SIMPLEX ,0.5,(190,190,190),1,cv.LINE_AA )    
cv.putText(imgAssinatura,'Seed:'+str(seedPic),(0,45),cv.FONT_HERSHEY_SCRIPT_SIMPLEX ,0.5,(190,190,190),1,cv.LINE_AA )    


quadro = cv.vconcat([imagem,imgAssinatura])

cv.imwrite('Quadro_Seed_'+str(seedPic)+'.png',quadro);


    
cv.imshow('Quadro: '+str(seedPic),quadro)
cv.waitKey()
cv.destroyAllWindows()







