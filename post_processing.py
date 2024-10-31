
import matplotlib.pyplot as plt

def plots(t,days,ys):
    
    ys1 = ys[:,0]
    ys2 = ys[:,1]
    ys3 = ys[:,2]
    ys4 = ys[:,3]
    ys5 = ys[:,4]
    ys6 = ys[:,5]
    ys7 = ys[:,6]
    ys8 = ys[:,7]
    ys9 = ys[:,8]
    ys10 = ys[:,9]
    ys11 = ys[:,10]
    
    plt.figure()

    # Debris
    plt.subplot(221)
    plt.plot(t, ys1, 'r')
    plt.legend(["D"])
    plt.xlim(0,days)
    plt.title('Detritos')
    plt.grid(True)

    # Macrophagos
    plt.subplot(222)
    plt.plot(t, ys2, '--k', t,ys3, 'b', t,ys4, 'g')
    plt.legend(["M0", "M1", "M2"])
    plt.xlim(0,days)
    plt.title('Macrófagos')
    plt.grid(True)

    # TNF
    plt.subplot(223)
    plt.plot(t, ys5, 'g')
    plt.legend(["c1"])
    plt.xlim(0,days)
    plt.title('Citocinas pró-inflamatórias')
    plt.grid(True)

    # IL10
    plt.subplot(224)
    plt.plot(t, ys6, 'c')
    plt.legend(["c2"])
    plt.xlim(0,days)
    plt.title('Citocinas anti-inflamatórias')
    plt.grid(True)

    plt.tight_layout()

    # exibe a figura
    plt.savefig('inflamatorio.png')
    plt.show()

    print(ys1)

    plt.figure()

    # Mesenchymal stem cells

    plt.subplot(231)
    plt.plot(t, ys7, 'b')
    plt.xlim(0,days)
    plt.legend(["Cm"])
    plt.title('Células-tronco mesenquimais')
    plt.grid(True)

    # Osteoblasts
    plt.subplot(232)
    plt.plot(t, ys8, 'y')
    plt.legend(["Cb"])
    plt.xlim(0,days)
    plt.title('Osteoblastos')
    plt.grid(True)

    # cartilage
    plt.subplot(233)
    plt.plot(t, ys9, 'g')
    plt.xlim(0,days)
    plt.legend(["Mc"])
    plt.title('Cartilagem')
    plt.grid(True)

    # bone
    plt.subplot(234)
    plt.plot(t, ys10, 'r')
    plt.xlim(0,days)
    plt.legend(["Mb"])
    plt.title('Osso')
    plt.grid(True)
    
    #Estradiol sérico
    #plt.subplot(235)
    #plt.plot(t, ys11, 'k')
    #plt.xlim(0,days)
    #plt.legend(["E2"])
    #plt.title('Estradiol')
    #plt.grid(True)

    plt.tight_layout()

    # Display the figure.
    plt.savefig('osso.png')
    plt.show()