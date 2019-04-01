import flavio
from flavio.classes import Observable, Prediction
import numpy as np
r"""Functions for neutrinoless $\mu - e$ conversion in different target nuclei"""
def CR_mue(wc_obj, par, nucl):
  r"""Conversion rate independent of the target nucleus"""
  mm = par['m_mu']
  #####overlap integrals and other parameters#####
  # GuV = par['GuV']
  # GdV = par['GdV']
  # GsV = par['GsV']
  GuS = par['GuS']
  GdS = par['GdS']
  GsS = par['GsS']
  D   = par['D ' +nucl]*mm**(5/2)
  Sp  = par['Sp '+nucl]*mm**(5/2)
  Vp  = par['Vp '+nucl]*mm**(5/2)
  Sn  = par['Sn '+nucl]*mm**(5/2)
  Vn  = par['Vn '+nucl]*mm**(5/2)
  GC  = par['GammaCapture '+nucl]
  #####Wilson Coefficients######
  #####Conversion Rate obtained from hep-ph/0203110#####
  scale = flavio.config['renormalization scale']['mudecays']
  wc = wc_obj.get_wc('mue', scale, par, nf_out=3)
  AL = np.sqrt(2)/(4*par['GF']*mm)*wc['Cgamma_emu'].conjugate()
  AR = np.sqrt(2)/(4*par['GF']*mm)*wc['Cgamma_mue']
  gRV = {'u': 4*(wc['CVRR_mueuu'] + wc['CVLR_mueuu']),
         'd': 4*(wc['CVRR_muedd'] + wc['CVLR_muedd']),
         's': 4*(wc['CVRR_muess'] + wc['CVLR_muess'])}
  gLV = {'u': 4*(wc['CVLR_uumue'] + wc['CVLL_mueuu']),
         'd': 4*(wc['CVLR_ddmue'] + wc['CVLL_muedd']),
         's': 4*(wc['CVLR_ssmue'] + wc['CVLL_muess'])}
  gRS = {'u': 4*(wc['CSRR_emuuu'].conjugate() + wc['CSRL_mueuu']),
         'd': 4*(wc['CSRR_emudd'].conjugate() + wc['CSRL_muedd']),
         's': 4*(wc['CSRR_emuss'].conjugate() + wc['CSRL_muess'])}
  gLS = {'u': 4*(wc['CSRL_emuuu'].conjugate() + wc['CSRR_mueuu']),
         'd': 4*(wc['CSRL_emudd'].conjugate() + wc['CSRR_muedd']),
         's': 4*(wc['CSRL_emuss'].conjugate() + wc['CSRR_muess'])}
  lhc = (AR.conjugate()*D + (2*gLV['u'] + gLV['d'])*Vp 
         +(gLV['u'] + 2*gLV['d'])*Vn 
         + (GuS* gLS['u'] + GdS*gLS['d'] + GsS*gLS['s'])*Sp 
         + (GuS*gLS['u'] + GdS*gLS['d'] + GsS*gLS['s'])*Sn)
  rhc = (AL.conjugate()*D + (2*gRV['u'] + gRV['d'])*Vp 
         +(gRV['u'] + 2*gRV['d'])*Vn 
         + (GuS* gRS['u'] + GdS*gRS['d'] + GsS*gRS['s'])*Sp 
         + (GuS*gRS['u'] + GdS*gRS['d'] + GsS*gRS['s'])*Sn)
  return 2*(par['GF']**2)*(abs(lhc)**2 + abs(rhc)**2)/GC


def CR_mueAu(wc_obj, par):
  r"""Conversion rate for $\phantom k^{197}_{79} \mathrm{Au}$"""
  return CR_mue(wc_obj, par, 'Au')
def CR_mueAl(wc_obj, par):
  r"""Conversion rate for $\phantom k^{27}_{13} \mathrm{Al}$"""
  return CR_mue(wc_obj, par, 'Al')
def CR_mueTi(wc_obj, par):
  r"""Conversion rate for $\phantom k^{48}_{22} \mathrm{Ti}$"""
  return CR_mue(wc_obj, par, 'Ti')

CRAu = Observable('CR(mu->e, Au)')
Prediction('CR(mu->e, Au)', CR_mueAu)
CRAu.tex = r"$CR(\mu - e)$ in $\phantom k^{197}_{79} \mathrm{Au}$"
CRAu.description = r"Coherent conversion rate of $\mu^-$ to $e^-$ in $\phantom k^{197}_{79} \mathrm{Au}$"
CRAu.add_taxonomy(r'Process :: $\mu$ lepton decays :: LFV decays :: $CR(\mu\to e)$ :: ' + CRAu.tex)

CRAl = Observable('CR(mu->e, Al)')
Prediction('CR(mu->e, Al)', CR_mueAl)
CRAl.tex = r"$CR(\mu - e)$ in $\phantom k^{27}_{13} \mathrm{Al}$"
CRAl.description = r"Coherent conversion rate of $\mu^-$ to $e^-$ in $\phantom k^{27}_{13} \mathrm{Al}$"
CRAl.add_taxonomy(r'Process :: $\mu$ lepton decays :: LFV decays :: $CR(\mu\to e)$ :: ' + CRAl.tex)

CRTi = Observable('CR(mu->e, Ti)')
Prediction('CR(mu->e, Ti)', CR_mueTi)
CRTi.tex = r"$CR(\mu - e)$ in $\phantom k^{48}_{22} \mathrm{Ti}$"
CRTi.description = r"Coherent conversion rate of $\mu^-$ to $e^-$ in $\phantom k^{48}_{22} \mathrm{Ti}$"
CRTi.add_taxonomy(r'Process :: $\mu$ lepton decays :: LFV decays :: $CR(\mu\to e)$ :: ' + CRTi.tex)
