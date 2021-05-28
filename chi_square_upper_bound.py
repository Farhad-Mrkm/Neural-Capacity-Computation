# -*- coding: utf-8 -*-
"""chi_square_upper_bound.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fUZMy1Q8hw2vujqXzJddBsw5MA6Z8_ip
"""

def chi_square_upper_bound(data0,data1, device, ref_n_samples=100000):
    def _uniform_sampling(x, batch_size):
      max1 = np.array(x.max())
      min1 = np.array(x.min())
      rng = np.random.default_rng()
      vals = rng.uniform(min1,max1,[batch_size,1])
      return vals

    
    x_samplei0=data0
    y_samplei0 = data1
    x_samplei=x_samplei0.cpu().detach().numpy()
    y_samplei=y_samplei0.cpu().detach().numpy()
    nsamples = x_samplei.shape[0]
    
    bins1=10000
    dens_ref = _uniform_sampling(x_samplei, ref_n_samples)
    dens_ref1 = _uniform_sampling(y_samplei, ref_n_samples)
    dens_x_sample = np.histogram(x_samplei, bins1)  # ,np.min(dens_ref),np.max(dens_ref))
    dens_y_sample = np.histogram(y_samplei, bins1)  # ,np.min(dens_ref1),np.max(dens_ref1))
    histrefx=np.histogram(dens_ref,bins1)
    histrefy=np.histogram(dens_ref1,bins1)
    numm = 0
    numm1 = 0
    numm2 = 0
    numm3 = 0
    for counter1 in range(bins1):
        if histrefx[0][counter1]!=0:
            numm=numm+((dens_x_sample[0][counter1]/nsamples-histrefx[0][counter1]/ref_n_samples)**2)/(histrefx[0][counter1]/ref_n_samples)

    for counter2 in range(bins1):
        if dens_x_sample[0][counter2]!=0:
            numm1=numm1+((dens_x_sample[0][counter2]/nsamples-histrefx[0][counter2]/ref_n_samples)**2)/(dens_x_sample[0][counter2]/nsamples) 
    for counter3 in range(bins1):
        if histrefy[0][counter3]!=0:
            numm2=numm2+((dens_y_sample[0][counter3]/nsamples-histrefy[0][counter3]/ref_n_samples)**2)/(histrefy[0][counter3]/ref_n_samples) 
    for counter4 in range(bins1):
        if dens_y_sample[0][counter4]!=0:
            numm3=numm3+((dens_y_sample[0][counter4]/nsamples-histrefy[0][counter4]/ref_n_samples)**2)/(dens_y_sample[0][counter4]/nsamples)    

    chi2x=np.log10(2)*numm 
    chi2xrev=np.log10(2)*numm1
    chi2y=np.log10(2)*numm2
    chi2yrev=np.log10(2)*numm3
    chi2xright=(1.5*(chi2x)**2)*np.log2(np.exp(1))
    chi2xleft=((1+chi2xrev)*(1+chi2x)**2)-1
    chi2yright=(1.5*(chi2y)**2)*np.log2(np.exp(1))
    chi2yleft=((1+chi2yrev)*(1+chi2y)**2)-1
    
    upkl_x =(np.log10(2)* np.log(1+chi2x)- (chi2xright/chi2xleft))
    upkl_y =(np.log10(2)* np.log(1+chi2y)- (chi2yright/chi2yleft))
    upkl_x = torch.tensor(upkl_x, dtype=torch.float).to(device)
    upkl_y = torch.tensor(upkl_y, dtype=torch.float).to(device)
    if upkl_x<=0:
        upkl_x = torch.tensor(0., dtype=torch.float).to(device)
        
    if upkl_y<=0:
        upkl_y = torch.tensor(0., dtype=torch.float).to(device)

    
    return upkl_x, upkl_y