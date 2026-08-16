

<!-- ===== SOURCE FILE: raw.md ===== -->



# **3rd Generation Partnership Project; Technical Specification Group Services and System Aspects; Technical Specifications and Technical Reports for a UTRAN-based 3GPP system (Release 9)** ---

![3GPP logo](935eed7aa61f7777f62cfc032e11bee9_img.jpg)

The 3GPP logo is a stylized representation of the letters '3GPP' in a bold, black, sans-serif font. The '3' is slightly larger and positioned to the left of the 'G', 'P', and 'P'. A small 'TM' trademark symbol is located to the upper right of the 'P'.

3GPP logo

The present document has been developed within the 3<sup>rd</sup> Generation Partnership Project (3GPP™) and may be further elaborated for the purposes of 3GPP.

The present document has not been subject to any approval process by the 3GPP Organisational Partners and shall not be implemented.  
This Specification is provided for future development work within 3GPP only. The Organisational Partners accept no liability for any use of this Specification.  
Specifications and reports for implementation of the 3GPP™ system should be obtained via the 3GPP Organisational Partners' Publications Offices.

---

Keywords  
UMTS, architecture

**3GPP**

Postal address

---

3GPP support office address

---

650 Route des Lucioles - Sophia Antipolis  
Valbonne - FRANCE  
Tel.: +33 4 92 94 42 00 Fax: +33 4 93 65 47 16

Internet

---

<http://www.3gpp.org>

# --- Contents

|                                            |    |
|--------------------------------------------|----|
| Foreword.....                              | 4  |
| 1 Scope.....                               | 5  |
| 2 References.....                          | 5  |
| 3 Abbreviations.....                       | 5  |
| 4 General.....                             | 5  |
| 5 Specifications and Reports.....          | 5  |
| Annex A (informative): Change history..... | 41 |

## **Copyright Notification**

No part may be reproduced except as authorized by written permission.  
The copyright and the foregoing restriction extend to reproduction in all media.

© 2012, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TTA, TTC).  
All rights reserved.

UMTSTM is a Trade Mark of ETSI registered for the benefit of its members  
3GPP™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners  
LTETM is a Trade Mark of ETSI currently being registered for the benefit of its Members and of the 3GPP Organizational Partners  
GSM® and the GSM logo are registered and owned by the GSM Association

# --- Foreword

This Technical Specification (TS) has been produced by the 3<sup>rd</sup> Generation Partnership Project (3GPP).

The contents of the present document are subject to continuing work within the TSG and may change following formal TSG approval. Should the TSG modify the contents of the present document, it will be re-released by the TSG with an identifying change of release date and an increase in version number as follows:

Version x.y.z

where:

- x the first digit:
  - 1 presented to TSG for information;
  - 2 presented to TSG for approval;
  - 3 or greater indicates TSG approved document under change control.
- y the second digit is incremented for all changes of substance, i.e. technical enhancements, corrections, updates, etc.
- z the third digit is incremented when editorial only changes have been incorporated in the document.

# 1 Scope

The present document identifies the 3GPP system specifications for Release 9. The specifications and reports of 3GPP Release 8 have a major version number 9 (i.e. 9.x.y). The listed Specifications are required to build a system based on UTRAN radio technology.

# 2 References

The following documents contain provisions which, through reference in this text, constitute provisions of the present document.

- References are either specific (identified by date of publication, edition number, version number, etc.) or non-specific.
- For a specific reference, subsequent revisions do not apply.
- For a non-specific reference, the latest version applies. In the case of a reference to a 3GPP document (including a GSM document), a non-specific reference implicitly refers to the latest version of that document *in the same Release as the present document*.

[1] 3GPP TR 21.905: "Vocabulary for 3GPP Specifications".

[2] 3GPP TR 21.900: "Technical Specification Group working methods".

# 3 Abbreviations

For the purposes of the present document, the terms and definitions given in 3GPP TS 21.905 [1] apply.

# 4 General

The numbering scheme for specifications is described in 3GPP TR 21.900 [2].

# 5 Specifications and Reports

NOTE 1: The "for publication?" column of the table below indicates whether or not the documents are intended for adoption by the partner Standards Development Organizations as their own publications. Those marked "no" are internal working documents of the 3GPP TSGs.

NOTE 2: Some of the algorithm specifications in the 35.-series are available only under licence.

NOTE 3: "Type" indicates Technical Specification (TS) or Technical Report (TR).

NOTE 4: For definition of "freezing" of specifications (last two columns), see 3GPP TS 21.900 [2].

| Type | Number | Title                                                                                               | WG prime | For publication? | freeze date | frozen |
|------|--------|-----------------------------------------------------------------------------------------------------|----------|------------------|-------------|--------|
| TS   | 21.101 | Technical Specifications and Technical Reports for a UTRAN-based 3GPP system                        | SP       | Yes              | 2010-03-25  | yes    |
| TS   | 21.111 | USIM and IC card requirements                                                                       | C6       | Yes              | 2009-12-10  | yes    |
| TS   | 21.202 | Technical Specifications and Technical Reports relating to the Common IP Multimedia Subsystem (IMS) | SP       | Yes              | 2010-03-25  | yes    |
| TR   | 21.801 | Specification drafting rules                                                                        | SP       | No               | 2009-12-10  | yes    |

| Type | Number | Title                                                                                             | WG prime | For publication? | freeze date | frozen |
|------|--------|---------------------------------------------------------------------------------------------------|----------|------------------|-------------|--------|
| TR   | 21.900 | Technical Specification Group working methods                                                     | SP       | Yes              | 2009-12-10  | yes    |
| TR   | 21.902 | Evolution of 3GPP system                                                                          | SP       | Yes              | 2009-12-10  | yes    |
| TR   | 21.905 | Vocabulary for 3GPP Specifications                                                                | SP       | Yes              | 2009-12-10  | yes    |
| TS   | 22.001 | Principles of circuit telecommunication services supported by a Public Land Mobile Network (PLMN) | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.002 | Circuit Bearer Services (BS) supported by a Public Land Mobile Network (PLMN)                     | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.003 | Circuit Teleservices supported by a Public Land Mobile Network (PLMN)                             | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.004 | General on supplementary services                                                                 | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.011 | Service accessibility                                                                             | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.016 | International Mobile station Equipment Identities (IMEI)                                          | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.022 | Personalisation of Mobile Equipment (ME); Mobile functionality specification                      | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.024 | Description of Charge Advice Information (CAI)                                                    | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.030 | Man-Machine Interface (MMI) of the User Equipment (UE)                                            | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.031 | 3G Security; Fraud Information Gathering System (FIGS); Service description; Stage 1              | S3       | Yes              | 2009-12-10  | yes    |
| TS   | 22.032 | Immediate Service Termination (IST); Service description; Stage 1                                 | S3       | Yes              | 2009-12-10  | yes    |
| TS   | 22.034 | High Speed Circuit Switched Data (HSCSD); Stage 1                                                 | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.038 | (U)SIM Application Toolkit (USAT); Service description; Stage 1                                   | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.041 | Operator Determined Barring (ODB)                                                                 | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.042 | Network Identity and TimeZone (NITZ); Service description; Stage 1                                | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.053 | Tandem Free Operation (TFO); Service description; Stage 1                                         | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 22.057 | Mobile Execution Environment (MExE); Service description; Stage 1                                 | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.060 | General Packet Radio Service (GPRS); Service description; Stage 1                                 | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.066 | Support of Mobile Number Portability (MNP); Service description; Stage 1                          | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.067 | enhanced Multi Level Precedence and Pre-emption service (eMLPP); Stage 1                          | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.071 | Location Services (LCS); Service description; Stage 1                                             | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.072 | Call Deflection (CD) service description; Stage 1                                                 | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.076 | Noise suppression for the AMR codec; Service description; Stage 1                                 | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 22.078 | Customized Applications for Mobile network Enhanced Logic                                         | S1       | Yes              | 2009-12-10  | yes    |

| Type | Number | Title                                                                                 | WG prime | For publication? | freeze date | frozen |
|------|--------|---------------------------------------------------------------------------------------|----------|------------------|-------------|--------|
|      |        | (CAMEL); Service description; Stage 1                                                 |          |                  | 12-10       |        |
| TS   | 22.079 | Support of Optimal Routeing (SOR); Service definition; Stage 1                        | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.081 | Line Identification supplementary services; Stage 1                                   | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.082 | Call Forwarding (CF) Supplementary Services; Stage 1                                  | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.083 | Call Waiting (CW) and Call Holding (HOLD); Supplementary Services; Stage 1            | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.084 | MultiParty (MPTY) supplementary service; Stage 1                                      | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.085 | Closed User Group (CUG) supplementary services; Stage 1                               | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.086 | Advice of Charge (AoC) supplementary services; Stage 1                                | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.087 | User-to-User Signalling (UUS); Service description; Stage 1                           | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.088 | Call Barring (CB) supplementary services; Stage 1                                     | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.090 | Unstructured Supplementary Service Data (USSD); Stage 1                               | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.091 | Explicit Call Transfer (ECT) supplementary service; Stage 1                           | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.093 | Completion of Calls to Busy Subscriber (CCBS); Service description, Stage 1           | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.094 | Follow Me service description; Stage 1                                                | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.096 | Name identification supplementary services; Stage 1                                   | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.097 | Multiple Subscriber Profile (MSP) Phase 2; Service description; Stage 1               | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.101 | Service aspects; Service principles                                                   | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.105 | Services and service capabilities                                                     | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.115 | Service aspects; Charging and billing                                                 | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.127 | Service requirement for the Open Services Access (OSA); Stage 1                       | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.129 | Service aspects; Handover requirements between UTRAN and GERAN or other radio systems | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.135 | Multicall; Service description; Stage 1                                               | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.140 | Multimedia Messaging Service (MMS); Stage 1                                           | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.141 | Presence service; Stage 1                                                             | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.142 | Value Added Services (VAS) for Short Message Service (SMS) requirements               | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.146 | Multimedia Broadcast/Multicast Service (MBMS); Stage 1                                | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.153 | Multimedia priority service                                                           | S1       | Yes              | 2009-12-10  | yes    |

| Type | Number | Title                                                                                                       | WG prime | For publication? | freeze date | frozen |
|------|--------|-------------------------------------------------------------------------------------------------------------|----------|------------------|-------------|--------|
| TS   | 22.173 | IP Multimedia Core Network Subsystem (IMS) Multimedia Telephony Service and supplementary services; Stage 1 | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.174 | Push Service; Service aspects; Stage 1                                                                      | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.182 | Customized Alerting Tones (CAT) requirements; Stage 1                                                       | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.183 | Customized Ringing Signal (CRS) requirements; Stage 1                                                       | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.220 | Service requirements for Home Node B (HNB) and Home eNode B (HeNB)                                          | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.226 | Global Text Telephony (GTT); Stage 1                                                                        | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.228 | Service requirements for the Internet Protocol (IP) multimedia core network subsystem (IMS); Stage 1        | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.233 | Transparent end-to-end packet-switched streaming service; Stage 1                                           | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.234 | Requirements on 3GPP system to Wireless Local Area Network (WLAN) interworking                              | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.240 | Service requirements for 3GPP Generic User Profile (GUP); Stage 1                                           | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.242 | Digital Rights Management (DRM); Stage 1                                                                    | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.243 | Speech recognition framework for automated voice services; Stage 1                                          | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.246 | Multimedia Broadcast/Multicast Service (MBMS) user services; Stage 1                                        | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.250 | IP Multimedia Subsystem (IMS) Group Management; Stage 1                                                     | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.259 | Service requirements for Personal Network Management (PNM); Stage 1                                         | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.268 | Public Warning System (PWS) requirements                                                                    | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.278 | Service requirements for the Evolved Packet System (EPS)                                                    | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.279 | Combined Circuit Switched (CS) and IP Multimedia Subsystem (IMS) sessions; Stage 1                          | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 22.340 | IP Multimedia Subsystem (IMS) messaging; Stage 1                                                            | S1       | Yes              | 2009-12-10  | yes    |
| TR   | 22.903 | Study on Videotelephony teleservice                                                                         | S1       | Yes              | 2009-12-10  | yes    |
| TR   | 22.908 | Study on Paging Permission with Access Control (PPAC)                                                       | S1       | Yes              | 2009-12-10  | yes    |
| TR   | 22.912 | Study into network selection requirements for non-3GPP access                                               | S1       | Yes              | 2009-12-10  | yes    |
| TR   | 22.934 | Feasibility study on 3GPP system to Wireless Local Area Network (WLAN) interworking                         | S1       | Yes              | 2009-12-10  | yes    |
| TR   | 22.935 | Feasibility study on Location Services (LCS) for Wireless Local Area Network (WLAN) interworking            | S1       | Yes              | 2009-12-10  | yes    |
| TR   | 22.936 | Multi-system terminals                                                                                      | S1       | Yes              | 2009-12-10  | yes    |
| TR   | 22.937 | Requirements for service continuity between mobile and Wireless Local Area Network (WLAN) networks          | S1       | Yes              | 2009-12-10  | yes    |
| TR   | 22.940 | IP Multimedia Subsystem (IMS) messaging                                                                     | S1       | Yes              | 2009-12-10  | yes    |

| Type | Number | Title                                                                                                | WG prime | For publication? | freeze date | frozen |
|------|--------|------------------------------------------------------------------------------------------------------|----------|------------------|-------------|--------|
|      |        |                                                                                                      |          |                  | 12-10       |        |
| TR   | 22.942 | Study on Value Added Services (VAS) for Short Message Service (SMS)                                  | S1       | Yes              | 2009-12-10  | yes    |
| TR   | 22.944 | Report on service requirements for UE functionality split                                            | S1       | Yes              | 2009-12-10  | yes    |
| TR   | 22.948 | Study of requirements of IP-Multimedia Subsystem (IMS) convergent multimedia conferencing            | S1       | Yes              | 2009-12-10  | yes    |
| TR   | 22.949 | Study on a generalized privacy capability                                                            | S1       | Yes              | 2009-12-10  | yes    |
| TR   | 22.950 | Priority service feasibility study                                                                   | S1       | Yes              | 2009-12-10  | yes    |
| TR   | 22.951 | Service aspects and requirements for network sharing                                                 | S1       | Yes              | 2009-12-10  | yes    |
| TR   | 22.952 | Priority service guide                                                                               | S1       | Yes              | 2009-12-10  | yes    |
| TR   | 22.953 | Multimedia priority service feasibility study                                                        | S1       | Yes              | 2009-12-10  | yes    |
| TR   | 22.967 | Transferring of emergency call data                                                                  | S1       | Yes              | 2009-12-10  | yes    |
| TR   | 22.968 | Study for requirements for a Public Warning System (PWS) service                                     | S1       | Yes              | 2009-12-10  | yes    |
| TR   | 22.973 | IMS Multimedia Telephony service; and supplementary services                                         | S1       | Yes              | 2009-12-10  | yes    |
| TR   | 22.977 | Feasibility study for speech-enabled services                                                        | S1       | Yes              | 2009-12-10  | yes    |
| TR   | 22.978 | All-IP network (AIPN) feasibility study                                                              | S1       | Yes              | 2009-12-10  | yes    |
| TR   | 22.979 | Feasibility study on combined Circuit Switched (CS) calls and IP Multimedia Subsystem (IMS) sessions | S1       | Yes              | 2009-12-10  | yes    |
| TR   | 22.980 | Network composition feasibility study                                                                | S1       | Yes              | 2009-12-10  | yes    |
| TR   | 22.982 | Study of Customised Alerting Tone (CAT) requirements                                                 | S1       | Yes              | 2009-12-10  | yes    |
| TR   | 22.983 | Services alignment and migration                                                                     | S1       | Yes              | 2009-12-10  | yes    |
| TR   | 22.985 | Service requirements for the User Data Convergence (UDC)                                             | S1       | Yes              | 2009-12-10  | yes    |
| TR   | 22.986 | Study on Service Specific Access Control                                                             | S1       | Yes              | 2009-12-10  | yes    |
| TS   | 23.002 | Network architecture                                                                                 | S2       | Yes              | 2009-12-10  | yes    |
| TS   | 23.003 | Numbering, addressing and identification                                                             | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 23.007 | Restoration procedures                                                                               | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 23.008 | Organization of subscriber data                                                                      | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 23.009 | Handover procedures                                                                                  | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 23.011 | Technical realization of Supplementary Services                                                      | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 23.012 | Location management procedures                                                                       | C4       | Yes              | 2009-12-10  | yes    |

| Type | Number | Title                                                                                  | WG prime | For publication? | freeze date | frozen |
|------|--------|----------------------------------------------------------------------------------------|----------|------------------|-------------|--------|
| TS   | 23.014 | Support of Dual Tone Multi-Frequency (DTMF) signalling                                 | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 23.015 | Technical realization of Operator Determined Barring (ODB)                             | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 23.016 | Subscriber data management; Stage 2                                                    | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 23.018 | Basic call handling; Technical realization                                             | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 23.031 | 3G Security; Fraud Information Gathering System (FIGS); Technical realization; Stage 2 | S3       | Yes              | 2009-12-10  | yes    |
| TS   | 23.032 | Universal Geographical Area Description (GAD)                                          | S2       | Yes              | 2009-12-10  | yes    |
| TS   | 23.034 | High Speed Circuit Switched Data (HSCSD); Stage 2                                      | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 23.035 | Immediate Service Termination (IST); Stage 2                                           | S3       | Yes              | 2009-12-10  | yes    |
| TS   | 23.038 | Alphabets and language-specific information                                            | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 23.040 | Technical realization of the Short Message Service (SMS)                               | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 23.041 | Technical realization of Cell Broadcast Service (CBS)                                  | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 23.042 | Compression algorithm for text messaging services                                      | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 23.053 | Tandem Free Operation (TFO); Service description; Stage 2                              | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 23.057 | Mobile Execution Environment (MExE); Functional description; Stage 2                   | S2       | Yes              | 2009-12-10  | yes    |
| TS   | 23.060 | General Packet Radio Service (GPRS); Service description; Stage 2                      | S2       | Yes              | 2009-12-10  | yes    |
| TS   | 23.066 | Support of Mobile Number Portability (MNP); Technical realization; Stage 2             | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 23.067 | enhanced Multi-Level Precedence and Pre-emption Service (eMLPP); Stage 2               | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 23.072 | Call Deflection (CD) supplementary service; Stage 2                                    | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 23.078 | Customised Applications for Mobile network Enhanced Logic (CAMEL) Phase 4; Stage 2     | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 23.079 | Support of Optimal Routeing (SOR); Technical realization                               | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 23.081 | Line Identification supplementary services; Stage 2                                    | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 23.082 | Call Forwarding (CF) supplementary services; Stage 2                                   | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 23.083 | Call Waiting (CW) and Call Hold (HOLD) supplementary services; Stage 2                 | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 23.084 | Multi Party (MPTY) supplementary service; Stage 2                                      | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 23.085 | Closed User Group (CUG) supplementary service; Stage 2                                 | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 23.086 | Advice of Charge (AoC) supplementary services; Stage 2                                 | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 23.087 | User-to-User Signalling (UUS) supplementary service; Stage 2                           | C4       | Yes              | 2009-12-10  | yes    |

| Type | Number | Title                                                                                                                | WG prime | For publication? | freeze date | frozen |
|------|--------|----------------------------------------------------------------------------------------------------------------------|----------|------------------|-------------|--------|
|      |        |                                                                                                                      |          |                  | 12-10       |        |
| TS   | 23.088 | Call Barring (CB) Supplementary Services; Stage 2                                                                    | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 23.090 | Unstructured Supplementary Service Data (USSD); Stage 2                                                              | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 23.091 | Explicit Call Transfer (ECT) supplementary service; Stage 2                                                          | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 23.093 | Technical realization of Completion of Calls to Busy Subscriber (CCBS); Stage 2                                      | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 23.094 | Follow-Me (FM); Stage 2                                                                                              | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 23.096 | Name identification supplementary services; Stage 2                                                                  | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 23.097 | Multiple Subscriber Profile (MSP) (Phase X); Stage 2                                                                 | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 23.101 | General Universal Mobile Telecommunications System (UMTS) architecture                                               | S2       | Yes              | 2009-12-10  | yes    |
| TS   | 23.107 | Quality of Service (QoS) concept and architecture                                                                    | S2       | Yes              | 2009-12-10  | yes    |
| TS   | 23.108 | Mobile radio interface layer 3 specification, core network protocols; Stage 2                                        | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 23.110 | Universal Mobile Telecommunications System (UMTS) access stratum; Services and functions                             | S2       | Yes              | 2009-12-10  | yes    |
| TS   | 23.116 | Super-Charger technical realization; Stage 2                                                                         | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 23.119 | Gateway Location Register (GLR); Stage2                                                                              | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 23.122 | Non-Access-Stratum (NAS) functions related to Mobile Station (MS) in idle mode                                       | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 23.135 | Multicall supplementary service; Stage 2                                                                             | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 23.141 | Presence service; Architecture and functional description                                                            | S2       | Yes              | 2009-12-10  | yes    |
| TS   | 23.142 | Value-added Services for SMS (VAS4SMS); Interface and signalling flow                                                | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 23.146 | Technical realization of facsimile Group 3 non-transparent                                                           | C3       | Yes              | 2009-12-10  | yes    |
| TS   | 23.153 | Out of band transcoder control; Stage 2                                                                              | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 23.167 | IP Multimedia Subsystem (IMS) emergency sessions                                                                     | S2       | Yes              | 2009-12-10  | yes    |
| TS   | 23.172 | Technical realization of Circuit Switched (CS) multimedia service UDI/RDI fallback and service modification; Stage 2 | C3       | Yes              | 2009-12-10  | yes    |
| TS   | 23.198 | Open Service Access (OSA); Stage 2                                                                                   | CP       | Yes              | 2009-12-10  | yes    |
| TS   | 23.202 | Circuit switched data bearer services                                                                                | C3       | Yes              | 2009-12-10  | yes    |
| TS   | 23.203 | Policy and charging control architecture                                                                             | S2       | Yes              | 2009-12-10  | yes    |
| TS   | 23.204 | Support of Short Message Service (SMS) over generic 3GPP Internet Protocol (IP) access; Stage 2                      | S2       | Yes              | 2009-12-10  | yes    |
| TS   | 23.205 | Bearer-independent circuit-switched core network; Stage 2                                                            | C4       | Yes              | 2009-12-10  | yes    |

| Type | Number | Title                                                                                                                                | WG prime | For publication? | freeze date | frozen |
|------|--------|--------------------------------------------------------------------------------------------------------------------------------------|----------|------------------|-------------|--------|
| TS   | 23.207 | End-to-end Quality of Service (QoS) concept and architecture                                                                         | S2       | Yes              | 2009-12-10  | yes    |
| TS   | 23.216 | Single Radio Voice Call Continuity (SRVCC); Stage 2                                                                                  | S2       | Yes              | 2009-12-10  | yes    |
| TS   | 23.218 | IP Multimedia (IM) session handling; IM call model; Stage 2                                                                          | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 23.221 | Architectural requirements                                                                                                           | S2       | Yes              | 2009-12-10  | yes    |
| TS   | 23.226 | Global text telephony (GTT); Stage 2                                                                                                 | S2       | Yes              | 2009-12-10  | yes    |
| TS   | 23.228 | IP Multimedia Subsystem (IMS); Stage 2                                                                                               | S2       | Yes              | 2009-12-10  | yes    |
| TS   | 23.231 | SIP-I based circuit-switched core network; Stage 2                                                                                   | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 23.234 | 3GPP system to Wireless Local Area Network (WLAN) interworking; System description                                                   | S2       | Yes              | 2009-12-10  | yes    |
| TS   | 23.236 | Intra-domain connection of Radio Access Network (RAN) nodes to multiple Core Network (CN) nodes                                      | S2       | Yes              | 2009-12-10  | yes    |
| TS   | 23.237 | IP Multimedia Subsystem (IMS) Service Continuity; Stage 2                                                                            | S2       | Yes              | 2009-12-10  | yes    |
| TS   | 23.240 | 3GPP Generic User Profile (GUP); Architecture (Stage 2)                                                                              | S2       | Yes              | 2009-12-10  | yes    |
| TS   | 23.246 | Multimedia Broadcast/Multicast Service (MBMS); Architecture and functional description                                               | S2       | Yes              | 2009-12-10  | yes    |
| TS   | 23.251 | Network sharing; Architecture and functional description                                                                             | S2       | Yes              | 2009-12-10  | yes    |
| TS   | 23.259 | Personal Network Management (PNM); Procedures and information flows; Stage 2                                                         | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 23.271 | Functional stage 2 description of Location Services (LCS)                                                                            | S2       | Yes              | 2009-12-10  | yes    |
| TS   | 23.272 | Circuit Switched (CS) fallback in Evolved Packet System (EPS); Stage 2                                                               | S2       | Yes              | 2009-12-10  | yes    |
| TS   | 23.278 | Customized Applications for Mobile network Enhanced Logic (CAMEL) Phase 4; Stage 2; IM CN Interworking                               | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 23.279 | Combining Circuit Switched (CS) and IP Multimedia Subsystem (IMS) services; Stage 2                                                  | S2       | Yes              | 2009-12-10  | yes    |
| TS   | 23.292 | IP Multimedia Subsystem (IMS) centralized services; Stage 2                                                                          | S2       | Yes              | 2009-12-10  | yes    |
| TS   | 23.327 | Mobility between 3GPP-Wireless Local Area Network (WLAN) interworking and 3GPP systems                                               | S2       | Yes              | 2009-12-10  | yes    |
| TS   | 23.333 | Multimedia Resource Function Controller (MRFC) - Multimedia Resource Function Processor (MRFP) Mp interface: Procedures descriptions | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 23.334 | IP Multimedia Subsystem (IMS) Application Level Gateway (IMS-ALG) – IMS Access Gateway (IMS-AGW) interface: Procedures descriptions  | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 23.335 | User Data Convergence (UDC); Technical realization and information flows; Stage 2                                                    | C4       | Yes              | 2010-03-19  | yes    |
| TS   | 23.380 | IMS Restoration Procedures                                                                                                           | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 23.402 | Architecture enhancements for non-3GPP accesses                                                                                      | S2       | Yes              | 2009-12-10  | yes    |
| TR   | 23.820 | Study of IMS restoration procedures                                                                                                  | C4       | No               | 2009-       | yes    |

| Type | Number | Title                                                                                                                                                            | WG prime | For publication? | freeze date | frozen |
|------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|------------------|-------------|--------|
|      |        |                                                                                                                                                                  |          |                  | 12-10       |        |
| TR   | 23.826 | Feasibility study on Voice Call Continuity (VCC) support for emergency calls                                                                                     | S2       | No               | 2009-12-10  | yes    |
| TR   | 23.830 | Architecture aspects of Home Node B (HNB) / Home enhanced Node B (HeNB)                                                                                          | S2       | No               | 2009-12-10  | yes    |
| TR   | 23.838 | IP Multimedia Subsystem (IMS) service continuity enhancements; Service, policy and interaction; Stage 2                                                          | S2       | No               | 2009-12-10  | yes    |
| TR   | 23.868 | Feasibility study on extension of support for IP Multimedia Subsystem (IMS) emergency calls                                                                      | S2       | No               | 2009-12-10  | yes    |
| TR   | 23.869 | Support for Internet Protocol (IP) based IP Multimedia Subsystem (IMS) Emergency calls over General Packet Radio Service (GPRS) and Evolved Packet Service (EPS) | S2       | No               | 2009-12-10  | yes    |
| TR   | 23.870 | Single Radio Voice Call Continuity (SR-VCC) support for IMS Emergency Calls                                                                                      | S2       | No               | 2009-12-10  | yes    |
| TR   | 23.879 | Study on Circuit Switched (CS) domain services over evolved Packet Switched (PS) access                                                                          | S2       | No               | 2009-12-10  | yes    |
| TR   | 23.883 | Study on enhancements to IMS Centralized Services (ICS)                                                                                                          | S2       | No               | 2009-12-10  | yes    |
| TR   | 23.903 | Redial solution for voice-video switching                                                                                                                        | S2       | Yes              | 2009-12-10  | yes    |
| TR   | 23.919 | Direct tunnel deployment guideline                                                                                                                               | S2       | Yes              | 2009-12-10  | yes    |
| TR   | 23.976 | Push architecture                                                                                                                                                | S2       | Yes              | 2009-12-10  | yes    |
| TR   | 23.977 | Bandwidth And Resource Savings (BARS) and speech enhancements for Circuit Switched (CS) networks                                                                 | S2       | Yes              | 2009-12-10  | yes    |
| TR   | 23.979 | 3GPP enablers for Open Mobile Alliance (OMA); Push-to-talk over Cellular (PoC) services; Stage 2                                                                 | S2       | Yes              | 2009-12-10  | yes    |
| TR   | 23.981 | Interworking aspects and migration scenarios for IPv4-based IP Multimedia Subsystem (IMS) implementations                                                        | S2       | Yes              | 2009-12-10  | yes    |
| TS   | 24.002 | GSM - UMTS Public Land Mobile Network (PLMN) Access Reference Configuration                                                                                      | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 24.007 | Mobile radio interface signalling layer 3; General Aspects                                                                                                       | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 24.008 | Mobile radio interface Layer 3 specification; Core network protocols; Stage 3                                                                                    | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 24.010 | Mobile radio interface layer 3; Supplementary services specification; General aspects                                                                            | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 24.011 | Point-to-Point (PP) Short Message Service (SMS) support on mobile radio interface                                                                                | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 24.022 | Radio Link Protocol (RLP) for circuit switched bearer and teleservices                                                                                           | C3       | Yes              | 2009-12-10  | yes    |
| TS   | 24.030 | Location Services (LCS); Supplementary service operations; Stage 3                                                                                               | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 24.067 | Enhanced Multi-Level Precedence and Pre-emption service (eMLPP); Stage 3                                                                                         | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 24.072 | Call Deflection (CD) supplementary service; Stage 3                                                                                                              | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 24.080 | Mobile radio interface layer 3 supplementary services specification; Formats and coding                                                                          | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 24.081 | Line Identification supplementary services; Stage 3                                                                                                              | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 24.082 | Call Forwarding (CF) supplementary services; Stage 3                                                                                                             | C4       | Yes              | 2009-12-10  | yes    |

| Type | Number | Title                                                                                                                          | WG prime | For publication? | freeze date | frozen |
|------|--------|--------------------------------------------------------------------------------------------------------------------------------|----------|------------------|-------------|--------|
|      |        |                                                                                                                                |          |                  | 12-10       |        |
| TS   | 24.083 | Call Waiting (CW) and Call Hold (HOLD) supplementary services; Stage 3                                                         | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 24.084 | Multi Party (MPTY) supplementary service; Stage 3                                                                              | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 24.085 | Closed User Group (CUG) supplementary service; Stage 3                                                                         | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 24.086 | Advice of Charge (AoC) supplementary services; Stage 3                                                                         | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 24.087 | User-to-User Signalling (UUS) Supplementary Service; Stage 3                                                                   | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 24.088 | Call Barring (CB) supplementary service; Stage 3                                                                               | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 24.090 | Unstructured Supplementary Service Data (USSD); Stage 3                                                                        | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 24.091 | Explicit Call Transfer (ECT) supplementary service; Stage 3                                                                    | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 24.093 | Completion of Calls to Busy Subscriber (CCBS); Stage 3                                                                         | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 24.096 | Name Identification supplementary services; Stage 3                                                                            | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 24.109 | Bootstrapping interface (Ub) and network application function interface (Ua); Protocol details                                 | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 24.135 | Multicall supplementary service; Stage 3                                                                                       | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 24.141 | Presence service using the IP Multimedia (IM) Core Network (CN) subsystem; Stage 3                                             | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 24.147 | Conferencing using the IP Multimedia (IM) Core Network (CN) subsystem; Stage 3                                                 | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 24.166 | 3GPP IP Multimedia Subsystem (IMS) conferencing Management Object (MO)                                                         | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 24.167 | 3GPP IMS Management Object (MO); Stage 3                                                                                       | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 24.173 | IMS Multimedia telephony communication service and supplementary services; Stage 3                                             | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 24.182 | IP Multimedia Subsystem (IMS) Customized Alerting Tones (CAT); Protocol specification                                          | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 24.183 | IP Multimedia Subsystem (IMS) Customized Ringing Signal (CRS); Protocol specification                                          | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 24.216 | Communication Continuity Management Object (MO)                                                                                | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 24.229 | IP multimedia call control protocol based on Session Initiation Protocol (SIP) and Session Description Protocol (SDP); Stage 3 | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 24.234 | 3GPP system to Wireless Local Area Network (WLAN) interworking; WLAN User Equipment (WLAN UE) to network protocols; Stage 3    | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 24.237 | IP Multimedia (IM) Core Network (CN) subsystem IP Multimedia Subsystem (IMS) service continuity; Stage 3                       | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 24.238 | Session Initiation Protocol (SIP) based user configuration; Stage 3                                                            | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 24.239 | Flexible Alerting (FA) using IP Multimedia (IM) Core Network (CN) subsystem; Protocol specification                            | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 24.247 | Messaging service using the IP Multimedia (IM) Core Network                                                                    | C1       | Yes              | 2009-12-10  | yes    |

| Type | Number | Title                                                                                                                                                                       | WG prime | For publication? | freeze date | frozen |
|------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|------------------|-------------|--------|
|      |        | (CN) subsystem; Stage 3                                                                                                                                                     |          |                  | 12-10       |        |
| TS   | 24.259 | Personal Network Management (PNM); Stage 3                                                                                                                                  | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 24.279 | Combining Circuit Switched (CS) and IP Multimedia Subsystem (IMS) services; Stage 3                                                                                         | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 24.285 | Allowed Closed Subscriber Group (CSG) list; Management Object (MO)                                                                                                          | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 24.286 | IP Multimedia (IM) Core Network (CN) subsystem Centralized Services (ICS); Management Object (MO)                                                                           | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 24.292 | IP Multimedia (IM) Core Network (CN) subsystem Centralized Services (ICS); Stage 3                                                                                          | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 24.294 | IP Multimedia Subsystem (IMS) Centralized Services (ICS) protocol via I1 interface                                                                                          | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 24.301 | Non-Access-Stratum (NAS) protocol for Evolved Packet System (EPS); Stage 3                                                                                                  | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 24.302 | Access to the 3GPP Evolved Packet Core (EPC) via non-3GPP access networks; Stage 3                                                                                          | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 24.303 | Mobility management based on Dual-Stack Mobile IPv6; Stage 3                                                                                                                | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 24.304 | Mobility management based on Mobile IPv4; User Equipment (UE) - foreign agent interface; Stage 3                                                                            | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 24.305 | Selective Disabling of 3GPP User Equipment Capabilities (SDOUE) Management Object (MO)                                                                                      | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 24.312 | Access Network Discovery and Selection Function (ANDSF) Management Object (MO)                                                                                              | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 24.323 | 3GPP IP Multimedia Subsystem (IMS) service level tracing Management Object (MO)                                                                                             | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 24.327 | Mobility between 3GPP Wireless Local Area Network (WLAN) interworking (I-WLAN) and 3GPP systems; General Packet Radio System (GPRS) and 3GPP I-WLAN aspects; Stage 3        | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 24.341 | Support of SMS over IP networks; Stage 3                                                                                                                                    | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 24.604 | Communication Diversion (CDIV) using IP Multimedia (IM) Core Network (CN) subsystem; Protocol specification                                                                 | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 24.605 | Conference (CONF) using IP Multimedia (IM) Core Network (CN) subsystem; Protocol specification                                                                              | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 24.606 | Message Waiting Indication (MWI) using IP Multimedia (IM) Core Network (CN) subsystem; Protocol specification                                                               | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 24.607 | Originating Identification Presentation (OIP) and Originating Identification Restriction (OIR) using IP Multimedia (IM) Core Network (CN) subsystem; Protocol specification | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 24.608 | Terminating Identification Presentation (TIP) and Terminating Identification Restriction (TIR) using IP Multimedia (IM) Core Network (CN) subsystem; Protocol specification | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 24.610 | Communication HOLD (HOLD) using IP Multimedia (IM) Core Network (CN) subsystem; Protocol specification                                                                      | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 24.611 | Anonymous Communication Rejection (ACR) and Communication Barring (CB) using IP Multimedia (IM) Core Network (CN) subsystem; Protocol specification                         | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 24.615 | Communication Waiting (CW) using IP Multimedia (IM) Core Network (CN) subsystem; Protocol Specification                                                                     | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 24.616 | Malicious Communication Identification (MCID) using IP Multimedia (IM) Core Network (CN) subsystem; Protocol                                                                | C1       | Yes              | 2009-12-10  | yes    |

| Type | Number | Title                                                                                                                                                                                   | WG prime | For publication? | freeze date | frozen |
|------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|------------------|-------------|--------|
|      |        | specification                                                                                                                                                                           |          |                  |             |        |
| TS   | 24.623 | Extensible Markup Language (XML) Configuration Access Protocol (XCAP) over the Ut interface for Manipulating Supplementary Services                                                     | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 24.628 | Common Basic Communication procedures using IP Multimedia (IM) Core Network (CN) subsystem; Protocol specification                                                                      | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 24.629 | Explicit Communication Transfer (ECT) using IP Multimedia (IM) Core Network (CN) subsystem; Protocol specification                                                                      | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 24.642 | Completion of Communications to Busy Subscriber (CCBS) and Completion of Communications by No Reply (CCNR) using IP Multimedia (IM) Core Network (CN) subsystem; Protocol specification | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 24.647 | Advice Of Charge (AOC) using IP Multimedia (IM) Core Network (CN) subsystem                                                                                                             | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 24.654 | Closed User Group (CUG) using IP Multimedia (IM) Core Network (CN) subsystem, Protocol Specification                                                                                    | C1       | Yes              | 2009-12-10  | yes    |
| TR   | 24.930 | Signalling flows for the session setup in the IP Multimedia core network Subsystem (IMS) based on Session Initiation Protocol (SIP) and Session Description Protocol (SDP); Stage 3     | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 25.101 | User Equipment (UE) radio transmission and reception (FDD)                                                                                                                              | R4       | Yes              | 2009-12-10  | yes    |
| TS   | 25.102 | User Equipment (UE) radio transmission and reception (TDD)                                                                                                                              | R4       | Yes              | 2009-12-10  | yes    |
| TS   | 25.104 | Base Station (BS) radio transmission and reception (FDD)                                                                                                                                | R4       | Yes              | 2009-12-10  | yes    |
| TS   | 25.105 | Base Station (BS) radio transmission and reception (TDD)                                                                                                                                | R4       | Yes              | 2009-12-10  | yes    |
| TS   | 25.106 | UTRA repeater radio transmission and reception                                                                                                                                          | R4       | Yes              | 2009-12-10  | yes    |
| TS   | 25.111 | Location Measurement Unit (LMU) performance specification; User Equipment (UE) positioning in UTRAN                                                                                     | R4       | Yes              | 2009-12-10  | yes    |
| TS   | 25.113 | Base station (BS) and repeater electromagnetic compatibility (EMC)                                                                                                                      | R4       | Yes              | 2009-12-10  | yes    |
| TS   | 25.123 | Requirements for support of radio resource management (TDD)                                                                                                                             | R4       | Yes              | 2009-12-10  | yes    |
| TS   | 25.133 | Requirements for support of radio resource management (FDD)                                                                                                                             | R4       | Yes              | 2009-12-10  | yes    |
| TS   | 25.141 | Base Station (BS) conformance testing (FDD)                                                                                                                                             | R4       | Yes              | 2009-12-10  | yes    |
| TS   | 25.142 | Base Station (BS) conformance testing (TDD)                                                                                                                                             | R4       | Yes              | 2009-12-10  | yes    |
| TS   | 25.143 | UTRA repeater conformance testing                                                                                                                                                       | R4       | Yes              | 2009-12-10  | yes    |
| TS   | 25.144 | User Equipment (UE) and Mobile Station (MS) over the air performance requirements                                                                                                       | R4       | Yes              | 2009-12-10  | yes    |
| TS   | 25.171 | Requirements for support of Assisted Global Positioning System (A-GPS); Frequency Division Duplex (FDD)                                                                                 | R4       | Yes              | 2009-12-10  | yes    |
| TS   | 25.201 | Physical layer - general description                                                                                                                                                    | R1       | Yes              | 2009-12-10  | yes    |
| TS   | 25.202 | 7.68 Mcps Time Division Duplex (TDD) option; Overall description: Stage 2                                                                                                               | R1       | Yes              | 2009-12-10  | yes    |
| TS   | 25.211 | Physical channels and mapping of transport channels onto physical channels (FDD)                                                                                                        | R1       | Yes              | 2009-12-10  | yes    |

| Type | Number | Title                                                                                                                              | WG prime | For publication? | freeze date | frozen |
|------|--------|------------------------------------------------------------------------------------------------------------------------------------|----------|------------------|-------------|--------|
| TS   | 25.212 | Multiplexing and channel coding (FDD)                                                                                              | R1       | Yes              | 2009-12-10  | yes    |
| TS   | 25.213 | Spreading and modulation (FDD)                                                                                                     | R1       | Yes              | 2009-12-10  | yes    |
| TS   | 25.214 | Physical layer procedures (FDD)                                                                                                    | R1       | Yes              | 2009-12-10  | yes    |
| TS   | 25.215 | Physical layer; Measurements (FDD)                                                                                                 | R1       | Yes              | 2009-12-10  | yes    |
| TS   | 25.221 | Physical channels and mapping of transport channels onto physical channels (TDD)                                                   | R1       | Yes              | 2009-12-10  | yes    |
| TS   | 25.222 | Multiplexing and channel coding (TDD)                                                                                              | R1       | Yes              | 2009-12-10  | yes    |
| TS   | 25.223 | Spreading and modulation (TDD)                                                                                                     | R1       | Yes              | 2009-12-10  | yes    |
| TS   | 25.224 | Physical layer procedures (TDD)                                                                                                    | R1       | Yes              | 2009-12-10  | yes    |
| TS   | 25.225 | Physical layer; Measurements (TDD)                                                                                                 | R1       | Yes              | 2009-12-10  | yes    |
| TS   | 25.301 | Radio interface protocol architecture                                                                                              | R2       | Yes              | 2009-12-10  | yes    |
| TS   | 25.302 | Services provided by the physical layer                                                                                            | R2       | Yes              | 2009-12-10  | yes    |
| TS   | 25.303 | Interlayer procedures in Connected Mode                                                                                            | R2       | Yes              | 2009-12-10  | yes    |
| TS   | 25.304 | User Equipment (UE) procedures in idle mode and procedures for cell reselection in connected mode                                  | R2       | Yes              | 2009-12-10  | yes    |
| TS   | 25.305 | Stage 2 functional specification of User Equipment (UE) positioning in UTRAN                                                       | R2       | Yes              | 2009-12-10  | yes    |
| TS   | 25.306 | UE Radio Access capabilities                                                                                                       | R2       | Yes              | 2009-12-10  | yes    |
| TS   | 25.307 | Requirements on User Equipments (UEs) supporting a release-independent frequency band                                              | R2       | Yes              | 2009-12-10  | yes    |
| TS   | 25.308 | High Speed Downlink Packet Access (HSDPA); Overall description; Stage 2                                                            | R2       | Yes              | 2009-12-10  | yes    |
| TS   | 25.317 | High Speed Packet Access (HSPA); Requirements on User Equipments (UEs) supporting a release-independent frequency band combination | R2       | Yes              | 2011-03-18  | yes    |
| TS   | 25.319 | Enhanced uplink; Overall description; Stage 2                                                                                      | R2       | Yes              | 2009-12-10  | yes    |
| TS   | 25.321 | Medium Access Control (MAC) protocol specification                                                                                 | R2       | Yes              | 2009-12-10  | yes    |
| TS   | 25.322 | Radio Link Control (RLC) protocol specification                                                                                    | R2       | Yes              | 2009-12-10  | yes    |
| TS   | 25.323 | Packet Data Convergence Protocol (PDCP) specification                                                                              | R2       | Yes              | 2009-12-10  | yes    |
| TS   | 25.324 | Broadcast/Multicast Control (BMC)                                                                                                  | R2       | Yes              | 2009-12-10  | yes    |
| TS   | 25.331 | Radio Resource Control (RRC); Protocol specification                                                                               | R2       | Yes              | 2009-12-10  | yes    |
| TS   | 25.346 | Introduction of the Multimedia Broadcast/Multicast Service (MBMS) in the Radio Access Network (RAN); Stage 2                       | R2       | Yes              | 2009-12-10  | yes    |
| TS   | 25.367 | Mobility procedures for Home Node B (HNB); Overall description; Stage 2                                                            | R2       | Yes              | 2009-12-10  | yes    |

| Type | Number | Title                                                                                                 | WG prime | For publication? | freeze date | frozen |
|------|--------|-------------------------------------------------------------------------------------------------------|----------|------------------|-------------|--------|
| TS   | 25.401 | UTRAN overall description                                                                             | R3       | Yes              | 2009-12-10  | yes    |
| TS   | 25.402 | Synchronisation in UTRAN Stage 2                                                                      | R3       | Yes              | 2009-12-10  | yes    |
| TS   | 25.410 | UTRAN Iu interface: General aspects and principles                                                    | R3       | Yes              | 2009-12-10  | yes    |
| TS   | 25.411 | UTRAN Iu interface layer 1                                                                            | R3       | Yes              | 2009-12-10  | yes    |
| TS   | 25.412 | UTRAN Iu interface signalling transport                                                               | R3       | Yes              | 2009-12-10  | yes    |
| TS   | 25.413 | UTRAN Iu interface Radio Access Network Application Part (RANAP) signalling                           | R3       | Yes              | 2009-12-10  | yes    |
| TS   | 25.414 | UTRAN Iu interface data transport and transport signalling                                            | R3       | Yes              | 2009-12-10  | yes    |
| TS   | 25.415 | UTRAN Iu interface user plane protocols                                                               | R3       | Yes              | 2009-12-10  | yes    |
| TS   | 25.419 | UTRAN Iu-BC interface: Service Area Broadcast Protocol (SABP)                                         | R3       | Yes              | 2009-12-10  | yes    |
| TS   | 25.420 | UTRAN Iur interface general aspects and principles                                                    | R3       | Yes              | 2009-12-10  | yes    |
| TS   | 25.421 | UTRAN Iur interface layer 1                                                                           | R3       | Yes              | 2009-12-10  | yes    |
| TS   | 25.422 | UTRAN Iur interface signalling transport                                                              | R3       | Yes              | 2009-12-10  | yes    |
| TS   | 25.423 | UTRAN Iur interface Radio Network Subsystem Application Part (RNSAP) signalling                       | R3       | Yes              | 2009-12-10  | yes    |
| TS   | 25.424 | UTRAN Iur interface data transport & transport signalling for Common Transport Channel data streams   | R3       | Yes              | 2009-12-10  | yes    |
| TS   | 25.425 | UTRAN Iur interface user plane protocols for Common Transport Channel data streams                    | R3       | Yes              | 2009-12-10  | yes    |
| TS   | 25.426 | UTRAN Iur and Iub interface data transport & transport signalling for DCH data streams                | R3       | Yes              | 2009-12-10  | yes    |
| TS   | 25.427 | UTRAN Iub/Iur interface user plane protocol for DCH data streams                                      | R3       | Yes              | 2009-12-10  | yes    |
| TS   | 25.430 | UTRAN Iub Interface: general aspects and principles                                                   | R3       | Yes              | 2009-12-10  | yes    |
| TS   | 25.431 | UTRAN Iub interface Layer 1                                                                           | R3       | Yes              | 2009-12-10  | yes    |
| TS   | 25.432 | UTRAN Iub interface: signalling transport                                                             | R3       | Yes              | 2009-12-10  | yes    |
| TS   | 25.433 | UTRAN Iub interface Node B Application Part (NBAP) signalling                                         | R3       | Yes              | 2009-12-10  | yes    |
| TS   | 25.434 | UTRAN Iub interface data transport and transport signalling for Common Transport Channel data streams | R3       | Yes              | 2009-12-10  | yes    |
| TS   | 25.435 | UTRAN Iub interface user plane protocols for Common Transport Channel data streams                    | R3       | Yes              | 2009-12-10  | yes    |
| TS   | 25.442 | UTRAN implementation-specific O&M transport                                                           | R3       | Yes              | 2009-12-10  | yes    |
| TS   | 25.444 | Iuh data transport                                                                                    | R3       | Yes              | 2009-12-10  | yes    |
| TS   | 25.446 | MBMS synchronisation protocol (SYNC)                                                                  | R3       | Yes              | 2009-12-10  | yes    |
| TS   | 25.450 | UTRAN Iupc interface general aspects and principles                                                   | R3       | Yes              | 2009-12-10  | yes    |

| Type | Number | Title                                                                                                                                                             | WG prime | For publication? | freeze date | frozen |
|------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|------------------|-------------|--------|
|      |        |                                                                                                                                                                   |          |                  | 12-10       |        |
| TS   | 25.451 | UTRAN Iupc interface layer 1                                                                                                                                      | R3       | Yes              | 2009-12-10  | yes    |
| TS   | 25.452 | UTRAN Iupc interface: signalling transport                                                                                                                        | R3       | Yes              | 2009-12-10  | yes    |
| TS   | 25.453 | UTRAN Iupc interface Positioning Calculation Application Part (PCAP) signalling                                                                                   | R3       | Yes              | 2009-12-10  | yes    |
| TS   | 25.460 | UTRAN Iuant interface: General aspects and principles                                                                                                             | R3       | Yes              | 2009-12-10  | yes    |
| TS   | 25.461 | UTRAN Iuant interface: Layer 1                                                                                                                                    | R3       | Yes              | 2009-12-10  | yes    |
| TS   | 25.462 | UTRAN Iuant interface: Signalling transport                                                                                                                       | R3       | Yes              | 2009-12-10  | yes    |
| TS   | 25.466 | UTRAN Iuant interface: Application part                                                                                                                           | R3       | Yes              | 2009-12-10  | yes    |
| TS   | 25.467 | UTRAN architecture for 3G Home Node B (HNB); Stage 2                                                                                                              | R3       | Yes              | 2009-12-10  | yes    |
| TS   | 25.468 | UTRAN Iuh Interface RANAP User Adaption (RUA) signalling                                                                                                          | R3       | Yes              | 2009-12-10  | yes    |
| TS   | 25.469 | UTRAN Iuh interface Home Node B (HNB) Application Part (HNBAP) signalling                                                                                         | R3       | Yes              | 2009-12-10  | yes    |
| TR   | 25.866 | 1.28 Mcps TDD Home Node B (HNB) study item technical report                                                                                                       | R4       | No               | 2009-12-10  | yes    |
| TR   | 25.903 | Continuous connectivity for packet data users                                                                                                                     | R1       | Yes              | 2009-12-10  | yes    |
| TR   | 25.906 | Dynamically reconfiguring a Frequency Division Duplex (FDD) User Equipment (UE) receiver to reduce power consumption when desired Quality of Service (QoS) is met | R4       | Yes              | 2009-12-10  | yes    |
| TR   | 25.907 | Evaluation of path-loss technologies for Location Services (LCS)                                                                                                  | R4       | Yes              | 2009-12-10  | yes    |
| TR   | 25.912 | Feasibility study for evolved Universal Terrestrial Radio Access (UTRA) and Universal Terrestrial Radio Access Network (UTRAN)                                    | RP       | Yes              | 2009-12-10  | yes    |
| TR   | 25.913 | Requirements for Evolved UTRA (E-UTRA) and Evolved UTRAN (E-UTRAN)                                                                                                | RP       | Yes              | 2009-12-10  | yes    |
| TR   | 25.914 | Measurements of radio performances for UMTS terminals in speech mode                                                                                              | R4       | Yes              | 2009-12-10  | yes    |
| TR   | 25.929 | Continuous connectivity for packet data users; 1.28 Mcps TDD                                                                                                      | R1       | Yes              | 2009-12-10  | yes    |
| TR   | 25.931 | UTRAN functions, examples on signalling procedures                                                                                                                | R3       | Yes              | 2009-12-10  | yes    |
| TR   | 25.942 | Radio Frequency (RF) system scenarios                                                                                                                             | R4       | Yes              | 2009-12-10  | yes    |
| TR   | 25.943 | Deployment aspects                                                                                                                                                | R4       | Yes              | 2009-12-10  | yes    |
| TR   | 25.951 | FDD Base Station (BS) classification                                                                                                                              | R4       | Yes              | 2009-12-10  | yes    |
| TR   | 25.956 | Universal Terrestrial Radio Access (UTRA) repeater planning guidelines and system analysis                                                                        | R4       | Yes              | 2009-12-10  | yes    |
| TR   | 25.963 | Feasibility study on interference cancellation for UTRA FDD User Equipment (UE)                                                                                   | R4       | Yes              | 2009-12-10  | yes    |
| TR   | 25.967 | Home Node B (HNB) Radio Frequency (RF) requirements (FDD)                                                                                                         | R4       | Yes              | 2009-12-10  | yes    |

| Type | Number | Title                                                                                                                          | WG prime | For publication? | freeze date | frozen |
|------|--------|--------------------------------------------------------------------------------------------------------------------------------|----------|------------------|-------------|--------|
| TR   | 25.992 | Multimedia Broadcast/Multicast Service (MBMS); UTRAN/GERAN requirements                                                        | RP       | Yes              | 2009-12-10  | yes    |
| TR   | 25.993 | Typical examples of Radio Access Bearers (RABs) and Radio Bearers (RBs) supported by Universal Terrestrial Radio Access (UTRA) | R2       | Yes              | 2009-12-10  | yes    |
| TR   | 25.996 | Spatial channel model for Multiple Input Multiple Output (MIMO) simulations                                                    | R1       | Yes              | 2009-12-10  | yes    |
| TS   | 26.071 | Mandatory speech CODEC speech processing functions; AMR speech Codec; General description                                      | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.073 | ANSI-C code for the Adaptive Multi Rate (AMR) speech codec                                                                     | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.074 | Mandatory speech codec speech processing functions; Adaptive Multi-Rate (AMR) speech codec test sequences                      | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.077 | Minimum performance requirements for noise suppresser; Application to the Adaptive Multi-Rate (AMR) speech encoder             | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.090 | Mandatory Speech Codec speech processing functions; Adaptive Multi-Rate (AMR) speech codec; Transcoding functions              | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.091 | Mandatory Speech Codec speech processing functions; Adaptive Multi-Rate (AMR) speech codec; Error concealment of lost frames   | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.092 | Mandatory speech codec speech processing functions; Adaptive Multi-Rate (AMR) speech codec; Comfort noise aspects              | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.093 | Mandatory speech codec speech processing functions Adaptive Multi-Rate (AMR) speech codec; Source controlled rate operation    | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.094 | Mandatory speech codec speech processing functions; Adaptive Multi-Rate (AMR) speech codec; Voice Activity Detector (VAD)      | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.101 | Mandatory speech codec speech processing functions; Adaptive Multi-Rate (AMR) speech codec frame structure                     | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.102 | Mandatory speech codec; Adaptive Multi-Rate (AMR) speech codec; Interface to Iu, Uu and Nb                                     | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.103 | Speech codec list for GSM and UMTS                                                                                             | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.104 | ANSI-C code for the floating-point Adaptive Multi-Rate (AMR) speech codec                                                      | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.110 | Codec for circuit switched multimedia telephony service; General description                                                   | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.111 | Codec for circuit switched multimedia telephony service; Modifications to H.324                                                | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.114 | IP Multimedia Subsystem (IMS); Multimedia telephony; Media handling and interaction                                            | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.115 | Echo control for speech and multimedia services                                                                                | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.131 | Terminal acoustic characteristics for telephony; Requirements                                                                  | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.132 | Speech and video telephony terminal acoustic test specification                                                                | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.140 | Multimedia Messaging Service (MMS); Media formats and codecs                                                                   | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.141 | IP Multimedia System (IMS) Messaging and Presence; Media formats and codecs                                                    | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.142 | Dynamic and Interactive Multimedia Scenes (DIMS)                                                                               | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.150 | Syndicated Feed Reception (SFR) within 3GPP environments; Protocols and codecs                                                 | S4       | Yes              | 2009-12-10  | yes    |

| Type | Number | Title                                                                                                                                         | WG prime | For publication? | freeze date | frozen |
|------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------|----------|------------------|-------------|--------|
| TS   | 26.171 | Speech codec speech processing functions; Adaptive Multi-Rate - Wideband (AMR-WB) speech codec; General description                           | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.173 | ANSI-C code for the Adaptive Multi-Rate - Wideband (AMR-WB) speech codec                                                                      | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.174 | Speech codec speech processing functions; Adaptive Multi-Rate - Wideband (AMR-WB) speech codec test sequences                                 | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.177 | Speech Enabled Services (SES); Distributed Speech Recognition (DSR) extended advanced front-end test sequences                                | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.190 | Speech codec speech processing functions; Adaptive Multi-Rate - Wideband (AMR-WB) speech codec; Transcoding functions                         | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.191 | Speech codec speech processing functions; Adaptive Multi-Rate - Wideband (AMR-WB) speech codec; Error concealment of erroneous or lost frames | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.192 | Speech codec speech processing functions; Adaptive Multi-Rate - Wideband (AMR-WB) speech codec; Comfort noise aspects                         | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.193 | Speech codec speech processing functions; Adaptive Multi-Rate - Wideband (AMR-WB) speech codec; Source controlled rate operation              | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.194 | Speech codec speech processing functions; Adaptive Multi-Rate - Wideband (AMR-WB) speech codec; Voice Activity Detector (VAD)                 | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.201 | Speech codec speech processing functions; Adaptive Multi-Rate - Wideband (AMR-WB) speech codec; Frame structure                               | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.202 | Speech codec speech processing functions; Adaptive Multi-Rate - Wideband (AMR-WB) speech codec; Interface to Iu, Uu and Nb                    | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.204 | Speech codec speech processing functions; Adaptive Multi-Rate - Wideband (AMR-WB) speech codec; ANSI-C code                                   | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.226 | Cellular text telephone modem; General description                                                                                            | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.230 | Cellular text telephone modem; Transmitter bit exact C-code                                                                                   | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.231 | Cellular text telephone modem; Minimum performance requirements                                                                               | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.233 | Transparent end-to-end Packet-switched Streaming service (PSS); General description                                                           | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.234 | Transparent end-to-end Packet-switched Streaming Service (PSS); Protocols and codecs                                                          | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.235 | Packet switched conversational multimedia applications; Default codecs                                                                        | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.236 | Packet switched conversational multimedia applications; Transport protocols                                                                   | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.237 | IP Multimedia Subsystem (IMS) based Packet Switch Streaming (PSS) and Multimedia Broadcast/Multicast Service (MBMS) User Service; Protocols   | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.243 | ANSI-C code for the fixed-point distributed speech recognition extended advanced front-end                                                    | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.244 | Transparent end-to-end packet switched streaming service (PSS); 3GPP file format (3GP)                                                        | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.245 | Transparent end-to-end Packet switched Streaming Service (PSS); Timed text format                                                             | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.246 | Transparent end-to-end Packet-switched Streaming Service (PSS); 3GPP SMIL language profile                                                    | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.267 | eCall data transfer; In-band modem solution; General description                                                                              | S4       | Yes              | 2009-12-10  | yes    |

| Type | Number | Title                                                                                                                                               | WG prime | For publication? | freeze date | frozen |
|------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------|----------|------------------|-------------|--------|
|      |        |                                                                                                                                                     |          |                  | 12-10       |        |
| TS   | 26.268 | eCall data transfer; In-band modem solution; ANSI-C reference code                                                                                  | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.269 | eCall data transfer; In-band modem solution; Conformance testing                                                                                    | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.273 | ANSI-C code for the fixed-point Extended Adaptive Multi-Rate - Wideband (AMR-WB+) speech codec                                                      | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.274 | Audio codec processing functions; Extended Adaptive Multi-Rate - Wideband (AMR-WB+) speech codec; Conformance testing                               | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.290 | Audio codec processing functions; Extended Adaptive Multi-Rate - Wideband (AMR-WB+) codec; Transcoding functions                                    | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.304 | Extended Adaptive Multi-Rate - Wideband (AMR-WB+) codec; Floating-point ANSI-C code                                                                 | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.346 | Multimedia Broadcast/Multicast Service (MBMS); Protocols and codecs                                                                                 | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.401 | General audio codec audio processing functions; Enhanced aacPlus general audio codec; General description                                           | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.402 | General audio codec audio processing functions; Enhanced aacPlus general audio codec; Additional decoder tools                                      | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.403 | General audio codec audio processing functions; Enhanced aacPlus general audio codec; Encoder specification; Advanced Audio Coding (AAC) part       | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.404 | General audio codec audio processing functions; Enhanced aacPlus general audio codec; Enhanced aacPlus encoder Spectral Band Replication (SBR) part | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.405 | General audio codec audio processing functions; Enhanced aacPlus general audio codec; Encoder specification parametric stereo part                  | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.406 | General audio codec audio processing functions; Enhanced aacPlus general audio codec; Conformance testing                                           | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.410 | General audio codec audio processing functions; Enhanced aacPlus general audio codec; Floating-point ANSI-C code                                    | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.411 | General audio codec audio processing functions; Enhanced aacPlus general audio codec; Fixed-point ANSI-C code                                       | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.412 | Source code for 3GP file format                                                                                                                     | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 26.430 | Timed graphics                                                                                                                                      | S4       | Yes              | 2010-03-25  | yes    |
| TR   | 26.902 | Video codec performance                                                                                                                             | S4       | Yes              | 2009-12-10  | yes    |
| TR   | 26.903 | Improved video support for Packet Switched Streaming (PSS) and Multimedia Broadcast/Multicast Service (MBMS) Services                               | S4       | Yes              | 2010-03-25  | yes    |
| TR   | 26.911 | Codec(s) for Circuit-Switched (CS) multimedia telephony service; Terminal implementor's guide                                                       | S4       | Yes              | 2009-12-10  | yes    |
| TR   | 26.914 | Multimedia telephony over IP Multimedia Subsystem (IMS); Optimization opportunities                                                                 | S4       | Yes              | 2009-12-10  | yes    |
| TR   | 26.935 | Packet Switched (PS) conversational multimedia applications; Performance characterisation of default codecs                                         | S4       | Yes              | 2009-12-10  | yes    |
| TR   | 26.936 | Performance characterization of 3GPP audio codecs                                                                                                   | S4       | Yes              | 2009-12-10  | yes    |
| TR   | 26.937 | Transparent end-to-end Packet-switched Streaming Service (PSS); Real-time Transport Protocol (RTP) usage model                                      | S4       | Yes              | 2009-12-10  | yes    |
| TR   | 26.943 | Recognition performance evaluations of codecs for Speech                                                                                            | S4       | Yes              | 2009-12-10  | yes    |

| Type | Number | Title                                                                                                                                                                                                                   | WG prime | For publication? | freeze date | frozen |
|------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|------------------|-------------|--------|
|      |        | Enabled Services (SES)                                                                                                                                                                                                  |          |                  | 12-10       |        |
| TR   | 26.944 | End-to-end multimedia services performance metrics                                                                                                                                                                      | S4       | Yes              | 2009-12-10  | yes    |
| TR   | 26.946 | Multimedia Broadcast/Multicast Service (MBMS) user service guidelines                                                                                                                                                   | S4       | Yes              | 2009-12-10  | yes    |
| TR   | 26.967 | eCall data transfer; In-band modem solution                                                                                                                                                                             | S4       | Yes              | 2009-12-10  | yes    |
| TR   | 26.969 | eCall data transfer; In-band modem solution; Characterization report                                                                                                                                                    | S4       | Yes              | 2009-12-10  | yes    |
| TR   | 26.975 | Performance characterization of the Adaptive Multi-Rate (AMR) speech codec                                                                                                                                              | S4       | Yes              | 2009-12-10  | yes    |
| TR   | 26.976 | Performance characterization of the Adaptive Multi-Rate Wideband (AMR-WB) speech codec                                                                                                                                  | S4       | Yes              | 2009-12-10  | yes    |
| TR   | 26.978 | Results of the Adaptive Multi-Rate (AMR) noise suppression selection phase                                                                                                                                              | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 27.001 | General on Terminal Adaptation Functions (TAF) for Mobile Stations (MS)                                                                                                                                                 | C3       | Yes              | 2009-12-10  | yes    |
| TS   | 27.002 | Terminal Adaptation Functions (TAF) for services using asynchronous bearer capabilities                                                                                                                                 | C3       | Yes              | 2009-12-10  | yes    |
| TS   | 27.003 | Terminal Adaptation Functions (TAF) for services using synchronous bearer capabilities                                                                                                                                  | C3       | Yes              | 2009-12-10  | yes    |
| TS   | 27.005 | Use of Data Terminal Equipment - Data Circuit terminating Equipment (DTE - DCE) interface for Short Message Service (SMS) and Cell Broadcast Service (CBS)                                                              | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 27.007 | AT command set for User Equipment (UE)                                                                                                                                                                                  | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 27.010 | Terminal Equipment to User Equipment (TE-UE) multiplexer protocol                                                                                                                                                       | C3       | Yes              | 2009-12-10  | yes    |
| TS   | 27.060 | Packet domain; Mobile Station (MS) supporting Packet Switched services                                                                                                                                                  | C3       | Yes              | 2009-12-10  | yes    |
| TS   | 28.062 | Inband Tandem Free Operation (TFO) of speech codecs; Service description; Stage 3                                                                                                                                       | S4       | Yes              | 2009-12-10  | yes    |
| TS   | 29.002 | Mobile Application Part (MAP) specification                                                                                                                                                                             | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 29.007 | General requirements on interworking between the Public Land Mobile Network (PLMN) and the Integrated Services Digital Network (ISDN) or Public Switched Telephone Network (PSTN)                                       | C3       | Yes              | 2009-12-10  | yes    |
| TS   | 29.010 | Information element mapping between Mobile Station - Base Station System (MS - BSS) and Base Station System - Mobile-services Switching Centre (BSS - MSC); Signalling Procedures and the Mobile Application Part (MAP) | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 29.011 | Signalling Interworking for supplementary services                                                                                                                                                                      | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 29.013 | Signalling interworking between ISDN supplementary services; Application Service Element (ASE) and Mobile Application Part (MAP) protocols                                                                              | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 29.016 | General Packet Radio Service (GPRS); Serving GPRS Support Node (SGSN) - Visitors Location Register (VLR); Gs interface network service specification                                                                    | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 29.018 | General Packet Radio Service (GPRS); Serving GPRS Support Node (SGSN) - Visitors Location Register (VLR); Gs interface layer 3 specification                                                                            | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 29.060 | General Packet Radio Service (GPRS); GPRS Tunnelling Protocol (GTP) across the Gn and Gp interface                                                                                                                      | C4       | Yes              | 2009-12-10  | yes    |

| Type | Number      | Title                                                                                                                                                                         | WG prime | For publication? | freeze date | frozen |
|------|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|------------------|-------------|--------|
| TS   | 29.061      | Interworking between the Public Land Mobile Network (PLMN) supporting packet based services and Packet Data Networks (PDN)                                                    | C3       | Yes              | 2009-12-10  | yes    |
| TS   | 29.078      | Customised Applications for Mobile network Enhanced Logic (CAMEL) Phase X; CAMEL Application Part (CAP) specification                                                         | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 29.108      | Application of the Radio Access Network Application Part (RANAP) on the E-interface                                                                                           | R3       | Yes              | 2009-12-10  | yes    |
| TS   | 29.109      | Generic Authentication Architecture (GAA); Zh and Zn Interfaces based on the Diameter protocol; Stage 3                                                                       | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 29.118      | Mobility Management Entity (MME) - Visitor Location Register (VLR) SGs interface specification                                                                                | C1       | Yes              | 2009-12-10  | yes    |
| TS   | 29.119      | GPRS Tunnelling Protocol (GTP) specification for Gateway Location Register (GLR)                                                                                              | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 29.120      | Mobile Application Part (MAP) specification for Gateway Location Register (GLR)                                                                                               | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 29.161      | Interworking between the Public Land Mobile Network (PLMN) supporting packet based services with Wireless Local Area Network (WLAN) access and Packet data Networks (PDN)     | C3       | Yes              | 2009-12-10  | yes    |
| TS   | 29.162      | Interworking between the IM CN subsystem and IP networks                                                                                                                      | C3       | Yes              | 2009-12-10  | yes    |
| TS   | 29.163      | Interworking between the IP Multimedia (IM) Core Network (CN) subsystem and Circuit Switched (CS) networks                                                                    | C3       | Yes              | 2009-12-10  | yes    |
| TS   | 29.164      | Interworking between the 3GPP CS domain with BICC or ISUP as signalling protocol and external SIP-I networks                                                                  | C3       | Yes              | 2009-12-10  | yes    |
| TS   | 29.165      | Inter-IMS Network to Network Interface (NNI)                                                                                                                                  | C3       | Yes              | 2009-12-10  | yes    |
| TS   | 29.168      | Cell Broadcast Centre interfaces with the Evolved Packet Core; Stage 3                                                                                                        | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 29.171      | Location Services (LCS); LCS Application Protocol (LCS-AP) between the Mobile Management Entity (MME) and Evolved Serving Mobile Location Centre (E-SMLC); SLs interface      | C4       | Yes              | 2010-03-19  | yes    |
| TS   | 29.172      | Location Services (LCS); Evolved Packet Core (EPC) LCS Protocol (ELP) between the Gateway Mobile Location Centre (GMLC) and the Mobile Management Entity (MME); SLg interface | C4       | Yes              | 2010-03-19  | yes    |
| TS   | 29.173      | Location Services (LCS); Diameter-based SLh interface for Control Plane LCS                                                                                                   | C4       | Yes              | 2010-03-19  | yes    |
| TS   | 29.198-01   | Open Service Access (OSA) Application Programming Interface (API); Part 1: Overview                                                                                           | CP       | Yes              | 2009-12-10  | yes    |
| TS   | 29.198-02   | Open Service Access (OSA) Application Programming Interface (API); Part 2: Common data definitions                                                                            | CP       | Yes              | 2009-12-10  | yes    |
| TS   | 29.198-03   | Open Service Access (OSA) Application Programming Interface (API); Part 3: Framework                                                                                          | CP       | Yes              | 2009-12-10  | yes    |
| TS   | 29.198-04-1 | Open Service Access (OSA) Application Programming Interface (API); Part 4: Call control; Subpart 1: Call control common definitions                                           | CP       | Yes              | 2009-12-10  | yes    |
| TS   | 29.198-04-2 | Open Service Access (OSA) Application Programming Interface (API); Part 4: Call control; Subpart 2: Generic call control Service Capability Feature (SCF)                     | CP       | Yes              | 2009-12-10  | yes    |
| TS   | 29.198-04-3 | Open Service Access (OSA) Application Programming Interface (API); Part 4: Call control; Subpart 3: Multi-party call control Service Capability Feature (SCF)                 | CP       | Yes              | 2009-12-10  | yes    |
| TS   | 29.198-04-4 | Open Service Access (OSA) Application Programming Interface (API); Part 4: Call control; Subpart 4: Multimedia call control Service Capability Feature (SCF)                  | CP       | Yes              | 2009-12-10  | yes    |

| Type | Number      | Title                                                                                                                                                        | WG prime | For publication? | freeze date | frozen |
|------|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|------------------|-------------|--------|
| TS   | 29.198-04-5 | Open Service Access (OSA) Application Programming Interface (API); Part 4: Call control; Subpart 5: Conference call control Service Capability Feature (SCF) | CP       | Yes              | 2009-12-10  | yes    |
| TS   | 29.198-05   | Open Service Access (OSA) Application Programming Interface (API); Part 5: User interaction Service Capability Feature (SCF)                                 | CP       | Yes              | 2009-12-10  | yes    |
| TS   | 29.198-06   | Open Service Access (OSA) Application Programming Interface (API); Part 6: Mobility Service Capability Feature (SCF)                                         | CP       | Yes              | 2009-12-10  | yes    |
| TS   | 29.198-07   | Open Service Access (OSA) Application Programming Interface (API); Part 7: Terminal capabilities Service Capability Feature (SCF)                            | CP       | Yes              | 2009-12-10  | yes    |
| TS   | 29.198-08   | Open Service Access (OSA) Application Programming Interface (API); Part 8: Data session control Service Capability Feature (SCF)                             | CP       | Yes              | 2009-12-10  | yes    |
| TS   | 29.198-10   | Open Service Access (OSA) Application Programming Interface (API); Part 10: Connectivity manager Service Capability Feature (SCF)                            | CP       | Yes              | 2009-12-10  | yes    |
| TS   | 29.198-11   | Open Service Access (OSA) Application Programming Interface (API); Part 11: Account management Service Capability Feature (SCF)                              | CP       | Yes              | 2009-12-10  | yes    |
| TS   | 29.198-12   | Open Service Access (OSA) Application Programming Interface (API); Part 12: Charging Service Capability Feature (SCF)                                        | CP       | Yes              | 2009-12-10  | yes    |
| TS   | 29.198-13   | Open Service Access (OSA) Application Programming Interface (API); Part 13: Policy management Service Capability Feature (SCF)                               | CP       | Yes              | 2009-12-10  | yes    |
| TS   | 29.198-14   | Open Service Access (OSA) Application Programming Interface (API); Part 14: Presence and Availability Management (PAM) Service Capability Feature (SCF)      | CP       | Yes              | 2009-12-10  | yes    |
| TS   | 29.198-15   | Open Service Access (OSA) Application Programming Interface (API); Part 15: Multi-media Messaging (MM) Service Capability Feature (SCF)                      | CP       | Yes              | 2009-12-10  | yes    |
| TS   | 29.198-16   | Open Service Access (OSA) Application Programming Interface (API); Part 16: Service broker Service Capability Feature (SCF)                                  | CP       | Yes              | 2009-12-10  | yes    |
| TS   | 29.199-01   | Open Service Access (OSA); Parlay X web services; Part 1: Common                                                                                             | CP       | Yes              | 2009-12-10  | yes    |
| TS   | 29.199-02   | Open Service Access (OSA); Parlay X web services; Part 2: Third party call                                                                                   | CP       | Yes              | 2009-12-10  | yes    |
| TS   | 29.199-03   | Open Service Access (OSA); Parlay X web services; Part 3: Call notification                                                                                  | CP       | Yes              | 2009-12-10  | yes    |
| TS   | 29.199-04   | Open Service Access (OSA); Parlay X web services; Part 4: Short messaging                                                                                    | CP       | Yes              | 2009-12-10  | yes    |
| TS   | 29.199-05   | Open Service Access (OSA); Parlay X web services; Part 5: Multimedia messaging                                                                               | CP       | Yes              | 2009-12-10  | yes    |
| TS   | 29.199-06   | Open Service Access (OSA); Parlay X web services; Part 6: Payment                                                                                            | CP       | Yes              | 2009-12-10  | yes    |
| TS   | 29.199-07   | Open Service Access (OSA); Parlay X web services; Part 7: Account management                                                                                 | CP       | Yes              | 2009-12-10  | yes    |
| TS   | 29.199-08   | Open Service Access (OSA); Parlay X web services; Part 8: Terminal status                                                                                    | CP       | Yes              | 2009-12-10  | yes    |
| TS   | 29.199-09   | Open Service Access (OSA); Parlay X web services; Part 9: Terminal location                                                                                  | CP       | Yes              | 2009-12-10  | yes    |
| TS   | 29.199-10   | Open Service Access (OSA); Parlay X web services; Part 10: Call handling                                                                                     | CP       | Yes              | 2009-12-10  | yes    |
| TS   | 29.199-11   | Open Service Access (OSA); Parlay X web services; Part 11: Audio call                                                                                        | CP       | Yes              | 2009-12-10  | yes    |

| Type | Number    | Title                                                                                                        | WG prime | For publication? | freeze date | frozen |
|------|-----------|--------------------------------------------------------------------------------------------------------------|----------|------------------|-------------|--------|
| TS   | 29.199-12 | Open Service Access (OSA); Parlay X web services; Part 12: Multimedia conference                             | CP       | Yes              | 2009-12-10  | yes    |
| TS   | 29.199-13 | Open Service Access (OSA); Parlay X web services; Part 13: Address list management                           | CP       | Yes              | 2009-12-10  | yes    |
| TS   | 29.199-14 | Open Service Access (OSA); Parlay X web services; Part 14: Presence                                          | CP       | Yes              | 2009-12-10  | yes    |
| TS   | 29.199-15 | Open Service Access (OSA); Parlay X web services; Part 15: Message broadcast                                 | CP       | Yes              | 2009-12-10  | yes    |
| TS   | 29.199-16 | Open Service Access (OSA); Parlay X web services; Part 16: Geocoding                                         | CP       | Yes              | 2009-12-10  | yes    |
| TS   | 29.199-17 | Open Service Access (OSA); Parlay X web services; Part 17: Application-driven Quality of Service (QoS)       | CP       | Yes              | 2009-12-10  | yes    |
| TS   | 29.199-18 | Open Service Access (OSA); Parlay X web services; Part 18: Device capabilities and configuration             | CP       | Yes              | 2009-12-10  | yes    |
| TS   | 29.199-19 | Open Service Access (OSA); Parlay X web services; Part 19: Multimedia streaming control                      | CP       | Yes              | 2009-12-10  | yes    |
| TS   | 29.199-20 | Open Service Access (OSA); Parlay X web services; Part 20: Multimedia multicast session management           | CP       | Yes              | 2009-12-10  | yes    |
| TS   | 29.199-21 | Open Service Access (OSA); Parlay X web services; Part 21: Content management                                | CP       | Yes              | 2009-12-10  | yes    |
| TS   | 29.199-22 | Open Service Access (OSA); Parlay X web services; Part 22: Policy                                            | CP       | Yes              | 2009-12-10  | yes    |
| TS   | 29.202    | Signalling System No. 7 (SS7) signalling transport in core network; Stage 3                                  | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 29.204    | Signalling System No. 7 (SS7) security gateway; Architecture, functional description and protocol details    | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 29.205    | Application of Q.1900 series to bearer independent Circuit Switched (CS) core network architecture; Stage 3  | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 29.212    | Policy and Charging Control (PCC) over Gx/Sd reference point                                                 | C3       | Yes              | 2009-12-10  | yes    |
| TS   | 29.213    | Policy and charging control signalling flows and Quality of Service (QoS) parameter mapping                  | C3       | Yes              | 2009-12-10  | yes    |
| TS   | 29.214    | Policy and charging control over Rx reference point                                                          | C3       | Yes              | 2009-12-10  | yes    |
| TS   | 29.215    | Policy and Charging Control (PCC) over S9 reference point; Stage 3                                           | C3       | Yes              | 2009-12-10  | yes    |
| TS   | 29.228    | IP Multimedia (IM) Subsystem Cx and Dx Interfaces; Signalling flows and message contents                     | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 29.229    | Cx and Dx interfaces based on the Diameter protocol; Protocol details                                        | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 29.230    | Diameter applications; 3GPP specific codes and identifiers                                                   | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 29.231    | Application of SIP-I Protocols to Circuit Switched (CS) core network architecture; Stage 3                   | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 29.232    | Media Gateway Controller (MGC) - Media Gateway (MGW) interface; Stage 3                                      | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 29.234    | 3GPP system to Wireless Local Area Network (WLAN) interworking; Stage 3                                      | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 29.235    | Interworking between SIP-I based circuit-switched core network and other networks                            | C3       | Yes              | 2009-12-10  | yes    |
| TS   | 29.238    | Interconnection Border Control Functions (IBCF) - Transition Gateway (TrGW) interface, Ix interface; Stage 3 | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 29.240    | 3GPP Generic User Profile (GUP); Stage 3; Network                                                            | C4       | Yes              | 2009-12-10  | yes    |

| Type | Number | Title                                                                                                                                                    | WG prime | For publication? | freeze date | frozen |
|------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------|----------|------------------|-------------|--------|
|      |        |                                                                                                                                                          |          |                  | 12-10       |        |
| TS   | 29.272 | Evolved Packet System (EPS); Mobility Management Entity (MME) and Serving GPRS Support Node (SGSN) related interfaces based on Diameter protocol         | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 29.273 | Evolved Packet System (EPS); 3GPP EPS AAA interfaces                                                                                                     | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 29.274 | 3GPP Evolved Packet System (EPS); Evolved General Packet Radio Service (GPRS) Tunnelling Protocol for Control plane (GTPv2-C); Stage 3                   | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 29.275 | Proxy Mobile IPv6 (PMIPv6) based Mobility and Tunnelling protocols; Stage 3                                                                              | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 29.276 | 3GPP Evolved Packet System (EPS); Optimized handover procedures and protocols between E-UTRAN access and cdma2000 HRPD Access; Stage 3                   | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 29.277 | Optimised handover procedures and protocol between EUTRAN access and non-3GPP accesses (S102); Stage 3                                                   | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 29.278 | Customized Applications for Mobile network Enhanced Logic (CAMEL) Phase 4; CAMEL Application Part (CAP) specification for IP Multimedia Subsystems (IMS) | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 29.279 | Mobile IPv4 (MIPv4) based mobility protocols; Stage 3                                                                                                    | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 29.280 | Evolved Packet System (EPS); 3GPP Sv interface (MME to MSC, and SGSN to MSC) for SRVCC                                                                   | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 29.281 | General Packet Radio System (GPRS) Tunnelling Protocol User Plane (GTPv1-U)                                                                              | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 29.282 | Mobile IPv6 vendor specific option format and usage within 3GPP                                                                                          | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 29.292 | Interworking between the IP Multimedia (IM) Core Network (CN) subsystem (IMS) and MSC Server for IMS Centralized Services (ICS)                          | C3       | Yes              | 2009-12-10  | yes    |
| TS   | 29.303 | Domain Name System Procedures; Stage 3                                                                                                                   | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 29.305 | InterWorking Function (IWF) between MAP based and Diameter based interfaces                                                                              | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 29.311 | Service level interworking for Messaging Services                                                                                                        | C3       | Yes              | 2009-12-10  | yes    |
| TS   | 29.328 | IP Multimedia (IM) Subsystem Sh interface; Signalling flows and message contents                                                                         | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 29.329 | Sh interface based on the Diameter protocol; Protocol details                                                                                            | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 29.332 | Media Gateway Control Function (MGCF) - IM Media Gateway; Mn interface                                                                                   | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 29.333 | Multimedia Resource Function Controller (MRFC) - Multimedia Resource Function Processor (MRFP) Mp interface; Stage 3                                     | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 29.334 | IMS Application Level Gateway (IMS-ALG) - IMS Access Gateway (IMS-AGW); Iq Interface; Stage 3                                                            | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 29.335 | User Data Convergence (UDC); User data repository access protocol over the Ud interface; Stage 3                                                         | C4       | Yes              | 2010-03-19  | yes    |
| TS   | 29.364 | IP Multimedia Subsystem (IMS) Application Server (AS) service data descriptions for AS interoperability                                                  | C4       | Yes              | 2009-12-10  | yes    |
| TS   | 29.414 | Core network Nb data transport and transport signalling                                                                                                  | C3       | Yes              | 2009-12-10  | yes    |
| TS   | 29.415 | Core network Nb interface user plane protocols                                                                                                           | C3       | Yes              | 2009-       | yes    |

| Type | Number      | Title                                                                                                                                                                                                            | WG prime | For publication? | freeze date | frozen |
|------|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|------------------|-------------|--------|
|      |             |                                                                                                                                                                                                                  |          |                  | 12-10       |        |
| TS   | 29.658      | SIP Transfer of IP Multimedia Service Tariff Information; Protocol specification                                                                                                                                 | C3       | Yes              | 2009-12-10  | yes    |
| TR   | 29.909      | Diameter-based protocols usage and recommendations in 3GPP                                                                                                                                                       | C3       | Yes              | 2009-12-10  | yes    |
| TR   | 29.994      | Recommended infrastructure measures to overcome specific Mobile Station (MS) and User Equipment (UE) faults                                                                                                      | C1       | Yes              | 2009-12-10  | yes    |
| TR   | 29.998-01   | Open Service Access (OSA); Application Programming Interface (API) mapping for OSA; Part 1: General issues on API mapping                                                                                        | CP       | Yes              | 2009-12-10  | yes    |
| TR   | 29.998-04-1 | Open Service Access (OSA); Application Programming Interface (API) Mapping for Open Service Access; Part 4: Call Control Service Mapping; Subpart 1: API to CAP Mapping                                          | CP       | Yes              | 2009-12-10  | yes    |
| TR   | 29.998-04-4 | Open Service Access (OSA); Application Programming Interface (API) Mapping for Open Service Access; Part 4: Call Control Service Mapping; Subpart 4: Multiparty Call Control ISC                                 | CP       | Yes              | 2009-12-10  | yes    |
| TR   | 29.998-05-1 | Open Service Access (OSA); Application Programming Interface (API) Mapping for Open Service Access; Part 5: User Interaction Service Mapping; Subpart 1: API to CAP Mapping                                      | CP       | Yes              | 2009-12-10  | yes    |
| TR   | 29.998-05-4 | Open Service Access (OSA); Application Programming Interface (API) Mapping for Open Service Access; Part 5: User Interaction Service Mapping; Subpart 4: API to SMS Mapping                                      | CP       | Yes              | 2009-12-10  | yes    |
| TR   | 29.998-06-1 | Open Service Access (OSA); Application Programming Interface (API) Mapping for Open Service Access; Part 6: User location - user status service mapping; Subpart 1: Mapping to Mobile Application Part (MAP)     | CP       | Yes              | 2009-12-10  | yes    |
| TR   | 29.998-06-2 | Open Service Access (OSA); Application Programming Interface (API) Mapping for Open Service Access; Part 6: User location - user status service mapping; Subpart 2: Mapping to Session Initiation Protocol (SIP) | CP       | Yes              | 2009-12-10  | yes    |
| TR   | 29.998-08   | Open Service Access (OSA); Application Programming Interface (API) Mapping for Open Service Access; Part 8: Data Session Control Service Mapping to CAP                                                          | CP       | Yes              | 2009-12-10  | yes    |
| TR   | 30.819      | Telecommunication management; Project scheduling and open issues for SA5, Release 9                                                                                                                              | S5       | No               | 2009-12-10  | yes    |
| TS   | 31.101      | UICC-terminal interface; Physical and logical characteristics                                                                                                                                                    | C6       | Yes              | 2009-12-10  | yes    |
| TS   | 31.102      | Characteristics of the Universal Subscriber Identity Module (USIM) application                                                                                                                                   | C6       | Yes              | 2009-12-10  | yes    |
| TS   | 31.103      | Characteristics of the IP Multimedia Services Identity Module (ISIM) application                                                                                                                                 | C6       | Yes              | 2009-12-10  | yes    |
| TS   | 31.111      | Universal Subscriber Identity Module (USIM) Application Toolkit (USAT)                                                                                                                                           | C6       | Yes              | 2009-12-10  | yes    |
| TS   | 31.115      | Remote APDU Structure for (U)SIM Toolkit applications                                                                                                                                                            | C6       | Yes              | 2009-12-10  | yes    |
| TS   | 31.116      | Remote APDU Structure for (U)SIM Toolkit applications                                                                                                                                                            | C6       | Yes              | 2009-12-10  | yes    |
| TS   | 31.120      | UICC-terminal interface; Physical, electrical and logical test specification                                                                                                                                     | C6       | Yes              |             |        |
| TS   | 31.121      | UICC-terminal interface; Universal Subscriber Identity Module (USIM) application test specification                                                                                                              | C6       | Yes              | 2009-12-10  | yes    |
| TS   | 31.122      | Universal Subscriber Identity Module (USIM) conformance test specification                                                                                                                                       | C6       | Yes              | 2009-12-10  | yes    |
| TS   | 31.124      | Mobile Equipment (ME) conformance test specification; Universal Subscriber Identity Module Application Toolkit (USAT)                                                                                            | C6       | Yes              | 2009-12-10  | yes    |

| Type | Number   | Title                                                                                                                                                                | WG prime | For publication? | freeze date | frozen |
|------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|------------------|-------------|--------|
|      |          | conformance test specification                                                                                                                                       |          |                  |             |        |
| TS   | 31.130   | (U)SIM Application Programming Interface (API); (U)SIM API for Java™ Card                                                                                            | C6       | Yes              | 2009-12-10  | yes    |
| TS   | 31.131   | C-language binding to (U)SIM API                                                                                                                                     | C6       | Yes              | 2009-12-10  | yes    |
| TS   | 31.133   | IP Multimedia Services Identity Module (ISIM) Application Programming Interface (API); ISIM API for Java Card™                                                       | C6       | Yes              | 2009-12-10  | yes    |
| TS   | 31.213   | Test specification for (U)SIM; Application Programming Interface (API) for Java Card™                                                                                | C6       | Yes              | 2009-12-10  | yes    |
| TS   | 31.220   | Characteristics of the Contact Manager for 3GPP UICC applications                                                                                                    | C6       | Yes              | 2009-12-10  | yes    |
| TS   | 31.221   | Contact Manager Application Programming Interface (API); Contact Manager API for Java Card                                                                           | C6       | Yes              | 2009-12-10  | yes    |
| TR   | 31.900   | SIM/USIM internal and external interworking aspects                                                                                                                  | C6       | Yes              | 2009-12-10  | yes    |
| TS   | 32.101   | Telecommunication management; Principles and high level requirements                                                                                                 | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.102   | Telecommunication management; Architecture                                                                                                                           | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.111-1 | Telecommunication management; Fault Management; Part 1: 3G fault management requirements                                                                             | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.111-2 | Telecommunication management; Fault Management; Part 2: Alarm Integration Reference Point (IRP): Information Service (IS)                                            | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.111-3 | Telecommunication management; Fault Management; Part 3: Alarm Integration Reference Point (IRP): Common Object Request Broker Architecture (CORBA) Solution Set (SS) | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.111-5 | Telecommunication management; Fault Management; Part 5: Alarm Integration Reference Point (IRP): eXtensible Markup Language (XML) definitions                        | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.111-7 | Telecommunication management; Fault Management; Part 7: Alarm IRP SOAP Solution Set (SS)                                                                             | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.121   | Telecommunication management; Advanced Alarm Management (AAM) Integration Reference Point (IRP): Requirements                                                        | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.122   | Telecommunication management; Advanced Alarm Management (AAM) Integration Reference Point (IRP): Information Service (IS)                                            | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.123   | Telecommunication management; Advanced Alarm Management (AAM) Integration Reference Point (IRP): Common Object Request Broker Architecture (CORBA) Solution Set (SS) | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.125   | Telecommunication management; Advanced Alarm Management (AAM) Integration Reference Point (IRP): eXtensible Markup Language (XML) file format definition             | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.127   | Telecommunication management; Advanced Alarm Management (AAM) Integration Reference Point (IRP): SOAP Solution Set (SS)                                              | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.140   | Telecommunication management; Subscription Management (SuM) requirements                                                                                             | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.141   | Telecommunication management; Subscription Management (SuM) architecture                                                                                             | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.150   | Telecommunication management; Integration Reference Point (IRP) Concept and definitions                                                                              | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.151   | Telecommunication management; Integration Reference Point (IRP) Information Service (IS) template                                                                    | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.152   | Telecommunication management; Integration Reference Point (IRP) Information Service (IS) Unified Modelling Language (UML)                                            | S5       | Yes              | 2009-12-10  | yes    |

| Type | Number | Title                                                                                                                                                                   | WG prime | For publication? | freeze date | frozen |
|------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|------------------|-------------|--------|
|      |        | repertoire                                                                                                                                                              |          |                  |             |        |
| TS   | 32.153 | Telecommunication management; Integration Reference Point (IRP) technology specific templates, rules and guidelines                                                     | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.154 | Telecommunication management; Backward and Forward Compatibility (BFC); Concept and definitions                                                                         | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.155 | Telecommunication management; Requirements template                                                                                                                     | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.171 | Telecommunication management; Subscription Management (SuM) Network Resource Model (NRM) Integration Reference Point (IRP); Requirements                                | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.172 | Telecommunication management; Subscription Management (SuM) Network Resource Model (NRM) Integration Reference Point (IRP); Information Service (IS)                    | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.175 | Telecommunication management; Subscription Management (SuM) Network Resource Model (NRM) Integration Reference Point (IRP); eXtensible Markup Language (XML) definition | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.181 | Telecommunication management; User Data Convergence (UDC); Framework for Model Handling and Management                                                                  | S5       | Yes              | 2010-06-10  | yes    |
| TS   | 32.182 | Telecommunication management; User Data Convergence (UDC); Common baseline information model (CBIM)                                                                     | S5       | Yes              | 2010-03-25  | yes    |
| TS   | 32.240 | Telecommunication management; Charging management; Charging architecture and principles                                                                                 | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.250 | Telecommunication management; Charging management; Circuit Switched (CS) domain charging                                                                                | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.251 | Telecommunication management; Charging management; Packet Switched (PS) domain charging                                                                                 | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.252 | Telecommunication management; Charging management; Wireless Local Area Network (WLAN) charging                                                                          | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.260 | Telecommunication management; Charging management; IP Multimedia Subsystem (IMS) charging                                                                               | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.270 | Telecommunication management; Charging management; Multimedia Messaging Service (MMS) charging                                                                          | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.271 | Telecommunication management; Charging management; Location Services (LCS) charging                                                                                     | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.272 | Telecommunication management; Charging management; Push-to-talk over Cellular (PoC) charging                                                                            | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.273 | Telecommunication management; Charging management; Multimedia Broadcast and Multicast Service (MBMS) charging                                                           | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.274 | Telecommunication management; Charging management; Short Message Service (SMS) charging                                                                                 | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.275 | Telecommunication management; Charging management; MultiMedia Telephony (MMTel) charging                                                                                | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.280 | Telecommunication management; Charging management; Advice of Charge (AoC) service                                                                                       | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.295 | Telecommunication management; Charging management; Charging Data Record (CDR) transfer                                                                                  | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.296 | Telecommunication management; Charging management; Online Charging System (OCS): Applications and interfaces                                                            | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.297 | Telecommunication management; Charging management; Charging Data Record (CDR) file format and transfer                                                                  | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.298 | Telecommunication management; Charging management; Charging Data Record (CDR) parameter description                                                                     | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.299 | Telecommunication management; Charging management;                                                                                                                      | S5       | Yes              | 2009-yes    |        |

| Type | Number | Title                                                                                                                                                                            | WG prime | For publication? | freeze date | frozen |
|------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|------------------|-------------|--------|
|      |        | Diameter charging applications                                                                                                                                                   |          |                  | 12-10       |        |
| TS   | 32.300 | Telecommunication management; Configuration Management (CM); Name convention for Managed Objects                                                                                 | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.301 | Telecommunication management; Configuration Management (CM); Notification Integration Reference Point (IRP); Requirements                                                        | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.302 | Telecommunication management; Configuration Management (CM); Notification Integration Reference Point (IRP); Information Service (IS)                                            | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.303 | Telecommunication management; Configuration Management (CM); Notification Integration Reference Point (IRP); Common Object Request Broker Architecture (CORBA) Solution Set (SS) | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.305 | Telecommunication management; Configuration Management (CM); Notification Integration Reference Point (IRP); eXtensible Markup Language (XML) definition                         | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.307 | Telecommunication management; Configuration Management (CM); Notification Integration Reference Point (IRP); SOAP Solution Set (SS)                                              | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.311 | Telecommunication management; Generic Integration Reference Point (IRP) management; Requirements                                                                                 | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.312 | Telecommunication management; Generic Integration Reference Point (IRP) management; Information Service (IS)                                                                     | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.313 | Telecommunication management; Generic Integration Reference Point (IRP) management; Common Object Request Broker Architecture (CORBA) Solution Set (SS)                          | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.317 | Telecommunication management; Generic Integration Reference Point (IRP) management; SOAP Solution Set (SS)                                                                       | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.321 | Telecommunication management; Test management Integration Reference Point (IRP); Requirements                                                                                    | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.322 | Telecommunication management; Test management Integration Reference Point (IRP); Information Service (IS)                                                                        | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.323 | Telecommunication management; Test management Integration Reference Point (IRP); Common Object Request Broker Architecture (CORBA) Solution Set (SS)                             | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.325 | Telecommunication management; Test management Integration Reference Point (IRP); eXtensible Markup Language (XML) definitions                                                    | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.327 | Telecommunication management; Test management Integration Reference Point (IRP); SOAP Solution Set (SS)                                                                          | S5       | Yes              | 2010-03-25  | yes    |
| TS   | 32.331 | Telecommunication management; Notification Log (NL) Integration Reference Point (IRP); Requirements                                                                              | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.332 | Telecommunication management; Notification Log (NL) Integration Reference Point (IRP); Information Service (IS)                                                                  | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.333 | Telecommunication management; Notification Log (NL) Integration Reference Point (IRP); Common Object Request Broker Architecture (CORBA) Solution Set (SS)                       | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.335 | Telecommunication management; Notification Log (NL) Integration Reference Point (IRP); eXtensible Markup Language (XML) solution definitions                                     | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.337 | Telecommunication management; Notification Log (NL) Integration Reference Point (IRP); SOAP Solution Set (SS)                                                                    | S5       | Yes              | 2010-03-25  | yes    |
| TS   | 32.341 | Telecommunication management; File Transfer (FT) Integration Reference Point (IRP); Requirements                                                                                 | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.342 | Telecommunication management; File Transfer (FT) Integration                                                                                                                     | S5       | Yes              | 2009-       | yes    |

| Type | Number | Title                                                                                                                                                                | WG prime | For publication? | freeze date | frozen |
|------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|------------------|-------------|--------|
|      |        | Reference Point (IRP); Information Service (IS)                                                                                                                      |          |                  | 12-10       |        |
| TS   | 32.343 | Telecommunication management; File Transfer (FT) Integration Reference Point (IRP); Common Object Request Broker Architecture (CORBA) Solution Set (SS)              | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.345 | Telecommunication management; File Transfer (FT) Integration Reference Point (IRP); eXtensible Markup Language (XML) definitions                                     | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.347 | Telecommunication management; File Transfer (FT) Integration Reference Point (IRP); SOAP Solution Set (SS)                                                           | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.351 | Telecommunication management; Communication Surveillance (CS) Integration Reference Point (IRP); Requirements                                                        | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.352 | Telecommunication management; Communication Surveillance (CS) Integration Reference Point (IRP); Information Service (IS)                                            | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.353 | Telecommunication management; Communication Surveillance (CS) Integration Reference Point (IRP); Common Object Request Broker Architecture (CORBA) Solution Set (SS) | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.355 | Telecommunication management; Communication Surveillance (CS) Integration Reference Point (IRP); eXtensible Markup Language (XML) definitions                        | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.357 | Telecommunication management; Communication Surveillance (CS) Integration Reference Point (IRP); SOAP Solution Set (SS)                                              | S5       | Yes              | 2010-03-25  | yes    |
| TS   | 32.361 | Telecommunication management; Entry Point (EP) Integration Reference Point (IRP); Requirements                                                                       | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.362 | Telecommunication management; Entry Point (EP) Integration Reference Point (IRP); Information Service (IS)                                                           | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.363 | Telecommunication management; Entry Point (EP) Integration Reference Point (IRP); Common Object Request Broker Architecture (CORBA) Solution Set (SS)                | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.365 | Telecommunication management; Entry Point (EP) Integration Reference Point (IRP); eXtensible Markup Language (XML) definitions                                       | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.367 | Telecommunication management; Entry Point (EP) Integration Reference Point (IRP); SOAP Solution Set (SS)                                                             | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.371 | Telecommunication management; Security Management concept and requirements                                                                                           | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.372 | Telecommunication management; Security services for Integration Reference Point (IRP); Information Service (IS)                                                      | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.373 | Telecommunication management; Security services for Integration Reference Point (IRP); Common Object Request Broker Architecture (CORBA) solution                    | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.375 | Telecommunication management; Security services for Integration Reference Point (IRP); File integrity solution                                                       | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.381 | Telecommunication management; Partial Suspension of Itf-N Integration Reference Point (IRP); Requirements                                                            | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.382 | Telecommunication management; Partial Suspension of Itf-N Integration Reference Point (IRP); Information Service (IS)                                                | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.383 | Telecommunication management; Partial Suspension of Itf-N Integration Reference Point (IRP); Common Object Request Broker Architecture (CORBA) Solution Set (SS)     | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.385 | Telecommunication management; Partial Suspension of Itf-N Integration Reference Point (IRP); eXtensible Markup Language (XML) file format definition                 | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.387 | Telecommunication management; Partial Suspension of Itf-N Integration Reference Point (IRP); SOAP Solution Set (SS)                                                  | S5       | Yes              | 2010-03-25  | yes    |

| Type | Number | Title                                                                                                                                                            | WG prime | For publication? | freeze date | frozen |
|------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|------------------|-------------|--------|
| TS   | 32.391 | Telecommunication management; Delta synchronization Integration Reference Point (IRP); Requirements                                                              | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.392 | Telecommunication management; Delta synchronization Integration Reference Point (IRP); Information Service (IS)                                                  | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.393 | Telecommunication management; Delta synchronization Integration Reference Point (IRP); Common Object Request Broker Architecture (CORBA) Solution Set (SS)       | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.395 | Telecommunication management; Delta synchronisation Integration Reference Point (IRP); eXtensible Markup Language (XML) file format definition                   | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.397 | Telecommunication management; Delta synchronization Integration Reference Point (IRP); SOAP Solution Set (SS)                                                    | S5       | Yes              | 2010-03-25  | yes    |
| TS   | 32.401 | Telecommunication management; Performance Management (PM); Concept and requirements                                                                              | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.404 | Telecommunication management; Performance Management (PM); Performance measurements; Definitions and template                                                    | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.405 | Telecommunication management; Performance Management (PM); Performance measurements; Universal Terrestrial Radio Access Network (UTRAN)                          | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.406 | Telecommunication management; Performance Management (PM); Performance measurements; Core Network (CN) Packet Switched (PS) domain                               | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.407 | Telecommunication management; Performance Management (PM); Performance measurements; Core Network (CN) Circuit Switched (CS) domain; UMTS and combined UMTS/GSM  | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.408 | Telecommunication management; Performance Management (PM); Performance measurements; Teleservice                                                                 | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.409 | Telecommunication management; Performance Management (PM); Performance measurements; IP Multimedia Subsystem (IMS)                                               | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.410 | Telecommunication management; Key Performance Indicators (KPI) for UMTS and GSM                                                                                  | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.411 | Telecommunication management; Performance Management (PM) Integration Reference Point (IRP): Requirements                                                        | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.412 | Telecommunication management; Performance Management (PM) Integration Reference Point (IRP): Information Service (IS)                                            | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.413 | Telecommunication management; Performance Management (PM) Integration Reference Point (IRP): Common Object Request Broker Architecture (CORBA) Solution Set (SS) | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.415 | Telecommunication management; Performance Management (PM) Integration Reference Point (IRP); eXtensible Markup Language (XML) definitions                        | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.417 | Telecommunication management; Performance Management (PM) Integration Reference Point (IRP); SOAP Solution Set (SS)                                              | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.421 | Telecommunication management; Subscriber and equipment trace; Trace concepts and requirements                                                                    | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.422 | Telecommunication management; Subscriber and equipment trace; Trace control and configuration management                                                         | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.423 | Telecommunication management; Subscriber and equipment trace; Trace data definition and management                                                               | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.432 | Telecommunication management; Performance measurement: File format definition                                                                                    | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.435 | Telecommunication management; Performance measurement; eXtensible Markup Language (XML) file format definition                                                   | S5       | Yes              | 2009-12-10  | yes    |

| Type | Number | Title                                                                                                                                                                                                    | WG prime | For publication? | freeze date | frozen |
|------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|------------------|-------------|--------|
| TS   | 32.436 | Telecommunication management; Performance measurement: Abstract Syntax Notation 1 (ASN.1) file format definition                                                                                         | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.441 | Telecommunication management; Trace Management Integration Reference Point (IRP); Requirements                                                                                                           | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.442 | Telecommunication management; Trace Management Integration Reference Point (IRP); Information Service (IS)                                                                                               | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.443 | Telecommunication management; Trace Management (Trace) Integration Reference Point (IRP): Common Object Request Broker Architecture (CORBA) Solution Set (SS)                                            | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.445 | Telecommunication management; Trace Management Integration Reference Point (IRP): eXtensible Markup Language (XML) file format definition                                                                | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.447 | Telecommunication management; Trace Management Integration Reference Point (IRP): SOAP Solution Set (SS)                                                                                                 | S5       | Yes              | 2010-03-25  | yes    |
| TS   | 32.450 | Telecommunication management; Key Performance Indicators (KPI) for Evolved Universal Terrestrial Radio Access Network (E-UTRAN): Definitions                                                             | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.451 | Telecommunication management; Key Performance Indicators (KPI) for Evolved Universal Terrestrial Radio Access Network (E-UTRAN); Requirements                                                            | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.500 | Telecommunication management; Self-Organizing Networks (SON); Concepts and requirements                                                                                                                  | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.501 | Telecommunication management; Self-configuration of network elements; Concepts and requirements                                                                                                          | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.502 | Telecommunication management; Self-configuration of network elements Integration Reference Point (IRP); Information Service (IS)                                                                         | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.503 | Telecommunication management; Self-configuration of network elements Integration Reference Point (IRP); Common Object Request Broker Architecture (CORBA) Solution Set (SS)                              | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.505 | Telecommunication management; Self-configuration of network elements Integration Reference Point (IRP): eXtensible Markup Language (XML) file format definition                                          | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.507 | Telecommunication management; Self-configuration of network elements Integration Reference Point (IRP): SOAP Solution Set (SS)                                                                           | S5       | Yes              | 2010-03-25  | yes    |
| TS   | 32.511 | Telecommunication management; Automatic Neighbour Relation (ANR) management; Concepts and requirements                                                                                                   | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.521 | Telecommunication management; Self-Organizing Networks (SON) Policy Network Resource Model (NRM) Integration Reference Point (IRP); Requirements                                                         | S5       | Yes              | 2010-03-25  | yes    |
| TS   | 32.522 | Telecommunication management; Self-Organizing Networks (SON) Policy Network Resource Model (NRM) Integration Reference Point (IRP); Information Service (IS)                                             | S5       | Yes              | 2010-03-25  | yes    |
| TS   | 32.523 | Telecommunication management; Self-Organizing Networks (SON); Policy Network Resource Model (NRM) Integration Reference Point (IRP); Common Object Request Broker Architecture (CORBA) Solution Set (SS) | S5       | Yes              | 2010-06-10  | yes    |
| TS   | 32.525 | Telecommunication management; Self-Organizing Networks (SON) Policy Network Resource Model (NRM) Integration Reference Point (IRP); eXtensible Markup Language (XML) file format definition              | S5       | Yes              | 2010-06-10  | yes    |
| TS   | 32.531 | Telecommunication management; Software management (SwM); Concepts and Integration Reference Point (IRP) Requirements                                                                                     | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.532 | Telecommunication management; Software management (SwM);                                                                                                                                                 | S5       | Yes              | 2009-       | yes    |

| Type | Number | Title                                                                                                                                                                                               | WG prime | For publication? | freeze date | frozen |
|------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|------------------|-------------|--------|
|      |        | Integration Reference Point (IRP); Information Service (IS)                                                                                                                                         |          |                  | 12-10       |        |
| TS   | 32.533 | Telecommunication management; Software management (SwM); Integration Reference Point (IRP); Common Object Request Broker Architecture (CORBA) Solution Set (SS)                                     | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.535 | Telecommunication management; Software Management Integration Reference Point (IRP); eXtensible Markup Language (XML) definitions                                                                   | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.537 | Telecommunication management; Software management (SwM); Integration Reference Point (IRP); SOAP Solution Set (SS)                                                                                  | S5       | Yes              | 2010-03-25  | yes    |
| TS   | 32.571 | Telecommunication management; Home Node B (HNB) and Home eNode B (HeNB) management; Type 2 interface concepts and requirements                                                                      | S5       | Yes              | 2010-03-25  | yes    |
| TS   | 32.572 | Telecommunication management; Home Node B (HNB) and Home eNode B (HeNB) management; Type 2 interface models and mapping functions                                                                   | S5       | Yes              | 2010-03-25  | yes    |
| TS   | 32.581 | Telecommunication management; Home Node B (HNB) Operations, Administration, Maintenance and Provisioning (OAM&P); Concepts and requirements for Type 1 interface HNB to HNB Management System (HMS) | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.582 | Telecommunication management; Home Node B (HNB) Operations, Administration, Maintenance and Provisioning (OAM&P); Information model for Type 1 interface HNB to HNB Management System (HMS)         | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.583 | Telecommunication management; Home Node B (HNB) Operations, Administration, Maintenance and Provisioning (OAM&P); Procedure flows for Type 1 interface HNB to HNB Management System (HMS)           | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.584 | Telecommunication management; Home Node B (HNB) Operations, Administration, Maintenance and Provisioning (OAM&P); XML definitions for Type 1 interface HNB to HNB Management System (HMS)           | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.600 | Telecommunication management; Configuration Management (CM); Concept and high-level requirements                                                                                                    | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.601 | Telecommunication management; Configuration Management (CM); Basic CM Integration Reference Point (IRP); Requirements                                                                               | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.602 | Telecommunication management; Configuration Management (CM); Basic CM Integration Reference Point (IRP); Information Service (IS)                                                                   | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.603 | Telecommunication management; Configuration Management (CM); Basic CM Integration Reference Point (IRP); Common Object Request Broker Architecture (CORBA) Solution Set (SS)                        | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.607 | Telecommunication management; Configuration Management (CM); Basic CM Integration Reference Point (IRP); SOAP Solution Set (SS)                                                                     | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.611 | Telecommunication management; Configuration Management (CM); Bulk CM Integration Reference Point (IRP); Requirements                                                                                | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.612 | Telecommunication management; Configuration Management (CM); Bulk CM Integration Reference Point (IRP); Information Service (IS)                                                                    | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.613 | Telecommunication management; Configuration Management (CM); Bulk CM Integration Reference Point (IRP); Common Object Request Broker Architecture (CORBA) Solution Set (SS)                         | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.615 | Telecommunication management; Configuration Management (CM); Bulk CM Integration Reference Point (IRP); eXtensible Markup Language (XML) file format definition                                     | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.617 | Telecommunication management; Configuration Management                                                                                                                                              | S5       | Yes              | 2009-       | yes    |

| Type | Number | Title                                                                                                                                                                                         | WG prime | For publication? | freeze date | frozen |
|------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|------------------|-------------|--------|
|      |        | (CM); Bulk CM Integration Reference Point (IRP): Bulk CM IRP SOAP Solution Set (SS)                                                                                                           |          |                  | 12-10       |        |
| TS   | 32.621 | Telecommunication management; Configuration Management (CM); Generic network resources Integration Reference Point (IRP); Requirements                                                        | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.622 | Telecommunication management; Configuration Management (CM); Generic network resources Integration Reference Point (IRP); Network Resource Model (NRM)                                        | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.623 | Telecommunication management; Configuration Management (CM); Generic network resources Integration Reference Point (IRP); Common Object Request Broker Architecture (CORBA) Solution Set (SS) | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.625 | Telecommunication management; Configuration Management (CM); Generic network resources Integration Reference Point (IRP): Bulk CM eXtensible Markup Language (XML) file format definition     | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.631 | Telecommunication management; Configuration Management (CM); Core network resources Integration Reference Point (IRP); Requirements                                                           | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.632 | Telecommunication management; Configuration Management (CM); Core Network Resources Integration Reference Point (IRP); Network Resource Model (NRM)                                           | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.633 | Telecommunication management; Configuration Management (CM); Core network resources Integration Reference Point (IRP); Common Object Request Broker Architecture (CORBA) Solution Set (SS)    | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.635 | Telecommunication management; Configuration Management (CM); Core network resources Integration Reference Point (IRP); Bulk CM eXtensible Markup Language (XML) file format definition        | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.641 | Telecommunication management; Configuration Management (CM); UTRAN network resources Integration Reference Point (IRP); Requirements                                                          | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.642 | Telecommunication management; Configuration Management (CM); UTRAN network resources Integration Reference Point (IRP); Network Resource Model (NRM)                                          | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.643 | Telecommunication management; Configuration Management (CM); UTRAN network resources Integration Reference Point (IRP); Common Object Request Broker Architecture (CORBA) Solution Set (SS)   | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.645 | Telecommunication management; Configuration Management (CM); UTRAN network resources Integration Reference Point (IRP); Bulk CM eXtensible Markup Language (XML) file format definition       | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.661 | Telecommunication management; Configuration Management (CM); Kernel CM Requirements                                                                                                           | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.662 | Telecommunication management; Configuration Management (CM); Kernel CM Information Service (IS)                                                                                               | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.663 | Telecommunication management; Configuration Management (CM); Kernel CM Integration Reference Point (IRP); Common Object Request Broker Architecture (CORBA) Solution Set (SS)                 | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.665 | Telecommunication management; Configuration Management (CM); Kernel CM Integration Reference Point (IRP); eXtensible Markup Language (XML) definitions                                        | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.667 | Telecommunication management; Configuration Management (CM); Kernel CM Integration Reference Point (IRP); SOAP Solution Set (SS)                                                              | S5       | Yes              | 2009-12-10  | yes    |

| Type | Number | Title                                                                                                                                                                                                                   | WG prime | For publication? | freeze date | frozen |
|------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|------------------|-------------|--------|
| TS   | 32.671 | Telecommunication management; Configuration Management (CM); State Management Integration Reference Point (IRP); Requirements                                                                                           | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.672 | Telecommunication management; Configuration Management (CM); State Management Integration Reference Point (IRP); Information Service (IS)                                                                               | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.673 | Telecommunication management; Configuration Management (CM); State Management Integration Reference Point (IRP); Common Object Request Broker Architecture (CORBA) Solution Set (SS)                                    | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.675 | Telecommunication management; Configuration Management (CM); State Management Integration Reference Point (IRP); Bulk CM eXtensible Markup Language (XML) file format definition                                        | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.690 | Telecommunication management; Inventory Management (IM); Requirements                                                                                                                                                   | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.691 | Telecommunication management; Inventory Management (IM) network resources Integration Reference Point (IRP): Requirements                                                                                               | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.692 | Telecommunication management; Inventory Management (IM) network resources Integration Reference Point (IRP); Network Resource Model (NRM)                                                                               | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.695 | Telecommunication management; Inventory Management (IM) network resources Integration Reference Point (IRP); Bulk Configuration Management (CM) eXtensible Markup Language (XML) file format definition                 | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.711 | Telecommunication management; Configuration Management (CM); Transport Network (TN) interface Network Resource Model (NRM) Integration Reference Point (IRP); Requirements                                              | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.712 | Telecommunication management; Configuration Management (CM); Transport Network (TN) interface Network Resource Model (NRM) Integration Reference Point (IRP); Information Service (IS)                                  | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.713 | Telecommunication management; Configuration Management (CM); Transport Network (TN) Network Resource Model (NRM) Integration Reference Point (IRP); Common Object Request Broker Architecture (CORBA) Solution Set (SS) | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.715 | Telecommunication management; Configuration Management (CM) Transport Network (TN); Network Resource Model (NRM) Integration Reference Point (IRP); Bulk CM eXtensible Markup Language (XML) file format definition     | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.721 | Telecommunication management; Configuration Management (CM); Repeater network resources Integration Reference Point (IRP); Requirements                                                                                 | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.722 | Telecommunication management; Configuration Management (CM); Repeater network resources Integration Reference Point (IRP); information Service (IS)                                                                     | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.723 | Telecommunication management; Configuration Management (CM); Repeater network resources Integration Reference Point (IRP); Common Object Request Broker Architecture (CORBA) Solution Set (SS)                          | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.725 | Telecommunication management; Configuration Management (CM); Repeater network resources Integration Reference Point (IRP); Bulk CM eXtensible Markup Language (XML) file format definition                              | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.731 | Telecommunication management; IP Multimedia Subsystem (IMS) Network Resource Model (NRM) Integration Reference Point (IRP); Requirements                                                                                | S5       | Yes              | 2009-12-10  | yes    |

| Type | Number | Title                                                                                                                                                                                                                                         | WG prime | For publication? | freeze date | frozen |
|------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|------------------|-------------|--------|
| TS   | 32.732 | Telecommunication management; IP Multimedia Subsystem (IMS) Network Resource Model (NRM) Integration Reference Point (IRP); Information Service (IS)                                                                                          | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.733 | Telecommunication management; IP Multimedia Subsystem (IMS) Network Resource Model (NRM) Integration Reference Point (IRP); Common Object Request Broker Architecture (CORBA) Solution Set (SS)                                               | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.735 | Telecommunication management; IP Multimedia Subsystem (IMS) Network Resource Model (NRM) Integration Reference Point (IRP); Bulk CM eXtensible Markup Language (XML) file format definition                                                   | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.741 | Telecommunication management; Configuration Management (CM); Signalling Transport Network (STN) interface Network Resource Model (NRM) Integration Reference Point (IRP); Requirements                                                        | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.742 | Telecommunication management; Configuration Management (CM); Signalling Transport Network (STN) interface Network Resource Model (NRM) Integration Reference Point (IRP); Information Service (IS)                                            | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.743 | Telecommunication management; Configuration Management (CM); Signalling Transport Network (STN) interface Network Resource Model (NRM) Integration Reference Point (IRP); Common Object Request Broker Architecture (CORBA) Solution Set (SS) | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.745 | Telecommunication management; Configuration Management (CM); Signalling Transport Network (STN) interface Network Resource Model (NRM) Integration Reference Point (IRP); Bulk CM eXtensible Markup Language (XML) file format definition     | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.751 | Telecommunication management; Evolved Packet Core (EPC) Network Resource Model (NRM) Integration Reference Point (IRP); Requirements                                                                                                          | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.752 | Telecommunication management; Evolved Packet Core (EPC) Network Resource Model (NRM) Integration Reference Point (IRP); Information Service (IS)                                                                                              | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.753 | Telecommunication management; Evolved Packet Core (EPC) Network Resource Model (NRM) Integration Reference Point (IRP); Common Object Request Broker Architecture (CORBA) Solution Set (SS)                                                   | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.755 | Telecommunication management; Evolved Packet Core (EPC) Network Resource Model (NRM) Integration Reference Point (IRP); eXtensible Markup Language (XML) definitions                                                                          | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.761 | Telecommunication management; Evolved Universal Terrestrial Radio Access Network (E-UTRAN) Network Resource Model (NRM) Integration Reference Point (IRP); Requirements                                                                       | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.762 | Telecommunication management; Evolved Universal Terrestrial Radio Access Network (E-UTRAN) Network Resource Model (NRM) Integration Reference Point (IRP); Information Service (IS)                                                           | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.763 | Telecommunication management; Evolved Universal Terrestrial Radio Access Network (E-UTRAN) Network Resource Model (NRM) Integration Reference Point (IRP); Common Object Request Broker Architecture (CORBA) Solution Set (SS)                | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.765 | Telecommunication management; Evolved Universal Terrestrial Radio Access Network (E-UTRAN) Network Resource Model (NRM) Integration Reference Point (IRP); eXtensible Markup Language (XML) definitions                                       | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.771 | Telecommunication management; Home Node B (HNB) Subsystem (HNS); Network Resource Model (NRM); Integration                                                                                                                                    | S5       | Yes              | 2009-12-10  | yes    |

| Type | Number | Title                                                                                                                                                                                                            | WG prime | For publication? | freeze date | frozen |
|------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|------------------|-------------|--------|
|      |        | Reference Point (IRP); Requirements                                                                                                                                                                              |          |                  |             |        |
| TS   | 32.772 | Telecommunication management; Home Node B (HNB) Subsystem (HNS); Network Resource Model (NRM); Integration Reference Point (IRP); Information Service (IS)                                                       | S5       | Yes              | 2010-03-25  | yes    |
| TS   | 32.773 | Telecommunication management; Home Node B (HNB) Subsystem (HNS); Network Resource Model (NRM); Integration Reference Point (IRP); Common Object Request Broker Architecture (CORBA) Solution Set (SS)            | S5       | Yes              | 2010-03-25  | yes    |
| TS   | 32.775 | Telecommunication management; Home Node B (HNB) Subsystem (HNS); Network Resource Model (NRM); Integration Reference Point (IRP); eXtensible Markup Language (XML) file format definition                        | S5       | Yes              | 2010-03-25  | yes    |
| TS   | 32.781 | Telecommunication management; Home enhanced Node B (HeNB) Subsystem (HeNS); Network Resource Model (NRM); Integration Reference Point (IRP); Requirements                                                        | S5       | Yes              | 2009-12-10  | yes    |
| TS   | 32.782 | Telecommunication management; Home enhanced Node B (HeNB) Subsystem (HeNS); Network Resource Model (NRM); Integration Reference Point (IRP); Information Service (IS)                                            | S5       | Yes              | 2010-03-25  | yes    |
| TS   | 32.783 | Telecommunication management; Home enhanced Node B (HeNB) Subsystem (HeNS); Network Resource Model (NRM); Integration Reference Point (IRP); Common Object Request Broker Architecture (CORBA) Solution Set (SS) | S5       | Yes              | 2010-03-25  | yes    |
| TS   | 32.785 | Telecommunication management; Home enhanced Node B (HeNB) Subsystem (HeNS); Network Resource Model (NRM); Integration Reference Point (IRP); Bulk CM eXtensible Markup Language (XML) file format definition     | S5       | Yes              | 2010-03-25  | yes    |
| TR   | 32.821 | Telecommunication management; Study of Self-Organizing Networks (SON) related Operations, Administration and Maintenance (OAM) for Home Node B (HNB)                                                             | S5       | No               | 2009-12-10  | yes    |
| TR   | 32.822 | Telecommunication management; Study on System Maintenance over Itf-N                                                                                                                                             | S5       | No               | 2009-12-10  | yes    |
| TR   | 32.823 | Telecommunication management; Self-Organizing Networks (SON); Study on self-healing                                                                                                                              | S5       | No               | 2009-12-10  | yes    |
| TR   | 32.824 | Telecommunication management; Service Oriented Architecture (SOA) Integration Reference Point (IRP) study                                                                                                        | S5       | No               | 2009-12-10  | yes    |
| TS   | 33.102 | 3G security; Security architecture                                                                                                                                                                               | S3       | Yes              | 2009-12-10  | yes    |
| TS   | 33.105 | 3G Security; Cryptographic algorithm requirements                                                                                                                                                                | S3       | Yes              | 2009-12-10  | yes    |
| TS   | 33.106 | 3G security; Lawful interception requirements                                                                                                                                                                    | S3       | Yes              | 2009-12-10  | yes    |
| TS   | 33.107 | 3G security; Lawful interception architecture and functions                                                                                                                                                      | S3       | Yes              | 2009-12-10  | yes    |
| TS   | 33.108 | 3G security; Handover interface for Lawful Interception (LI)                                                                                                                                                     | S3       | Yes              | 2009-12-10  | yes    |
| TS   | 33.110 | Key establishment between a Universal Integrated Circuit Card (UICC) and a terminal                                                                                                                              | S3       | Yes              | 2009-12-10  | yes    |
| TS   | 33.141 | Presence service; Security                                                                                                                                                                                       | S3       | Yes              | 2009-12-10  | yes    |
| TS   | 33.203 | 3G security; Access security for IP-based services                                                                                                                                                               | S3       | Yes              | 2009-12-10  | yes    |
| TS   | 33.204 | 3G Security; Network Domain Security (NDS); Transaction Capabilities Application Part (TCAP) user security                                                                                                       | S3       | Yes              | 2009-12-10  | yes    |
| TS   | 33.210 | 3G security; Network Domain Security (NDS); IP network layer security                                                                                                                                            | S3       | Yes              | 2009-12-10  | yes    |

| Type | Number | Title                                                                                                                                                                                                           | WG prime | For publication? | freeze date | frozen |
|------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|------------------|-------------|--------|
| TS   | 33.220 | Generic Authentication Architecture (GAA); Generic Bootstrapping Architecture (GBA)                                                                                                                             | S3       | Yes              | 2009-12-10  | yes    |
| TS   | 33.221 | Generic Authentication Architecture (GAA); Support for subscriber certificates                                                                                                                                  | S3       | Yes              | 2009-12-10  | yes    |
| TS   | 33.222 | Generic Authentication Architecture (GAA); Access to network application functions using Hypertext Transfer Protocol over Transport Layer Security (HTTPS)                                                      | S3       | Yes              | 2009-12-10  | yes    |
| TS   | 33.223 | Generic Authentication Architecture (GAA); Generic Bootstrapping Architecture (GBA) Push function                                                                                                               | S3       | Yes              | 2009-12-10  | yes    |
| TS   | 33.224 | Generic Authentication Architecture (GAA); Generic Bootstrapping Architecture (GBA) push layer                                                                                                                  | S3       | Yes              | 2009-12-10  | yes    |
| TS   | 33.234 | 3G security; Wireless Local Area Network (WLAN) interworking security                                                                                                                                           | S3       | Yes              | 2009-12-10  | yes    |
| TS   | 33.246 | 3G Security; Security of Multimedia Broadcast/Multicast Service (MBMS)                                                                                                                                          | S3       | Yes              | 2009-12-10  | yes    |
| TS   | 33.259 | Key establishment between a UICC hosting device and a remote device                                                                                                                                             | S3       | Yes              | 2009-12-10  | yes    |
| TS   | 33.310 | Network Domain Security (NDS); Authentication Framework (AF)                                                                                                                                                    | S3       | Yes              | 2009-12-10  | yes    |
| TS   | 33.320 | Security of Home Node B (HNB) / Home evolved Node B (HeNB)                                                                                                                                                      | S3       | Yes              | 2009-12-10  | yes    |
| TS   | 33.328 | IP Multimedia Subsystem (IMS) media plane security                                                                                                                                                              | S3       | Yes              | 2009-12-10  | yes    |
| TS   | 33.401 | 3GPP System Architecture Evolution (SAE); Security architecture                                                                                                                                                 | S3       | Yes              | 2009-12-10  | yes    |
| TS   | 33.402 | 3GPP System Architecture Evolution (SAE); Security aspects of non-3GPP accesses                                                                                                                                 | S3       | Yes              | 2009-12-10  | yes    |
| TR   | 33.812 | Feasibility study on the security aspects of remote provisioning and change of subscription for Machine to Machine (M2M) equipment                                                                              | S3       | No               | 2009-12-10  | yes    |
| TR   | 33.821 | Rationale and track of security decisions in Long Term Evolution (LTE) RAN / 3GPP System Architecture Evolution (SAE)                                                                                           | S3       | No               | 2009-12-10  | yes    |
| TR   | 33.828 | IP Multimedia Subsystem (IMS) media plane security                                                                                                                                                              | S3       | No               | 2010-03-25  | yes    |
| TR   | 33.905 | Recommendations for Trusted Open Platforms                                                                                                                                                                      | S3       | Yes              | 2009-12-10  | yes    |
| TR   | 33.919 | 3G Security; Generic Authentication Architecture (GAA); System description                                                                                                                                      | S3       | Yes              | 2009-12-10  | yes    |
| TR   | 33.924 | Identity management and 3GPP security interworking; Identity management and Generic Authentication Architecture (GAA) interworking                                                                              | S3       | Yes              | 2009-12-10  | yes    |
| TR   | 33.937 | Study of mechanisms for Protection against Unsolicited Communication for IMS (PUCI)                                                                                                                             | S3       | Yes              | 2009-12-10  | yes    |
| TR   | 33.980 | Liberty Alliance and 3GPP security interworking; Interworking of Liberty Alliance Identity Federation Framework (ID-FF), Identity Web Services Framework (ID-WSF) and Generic Authentication Architecture (GAA) | S3       | Yes              | 2009-12-10  | yes    |
| TS   | 34.108 | Common test environments for User Equipment (UE); Conformance testing                                                                                                                                           | R5       | Yes              | 2010-03-19  | yes    |
| TS   | 34.109 | Terminal logical test interface; Special conformance testing functions                                                                                                                                          | R2       | Yes              | 2009-12-10  | yes    |
| TS   | 34.114 | User Equipment (UE) / Mobile Station (MS) Over The Air (OTA) antenna performance; Conformance testing                                                                                                           | R5       | Yes              | 2010-03-19  | yes    |

| Type | Number   | Title                                                                                                                                                                                                                                                      | WG prime | For publication? | freeze date | frozen |
|------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|------------------|-------------|--------|
| TS   | 34.121-1 | User Equipment (UE) conformance specification; Radio transmission and reception (FDD); Part 1: Conformance specification                                                                                                                                   | R5       | Yes              | 2010-03-19  | yes    |
| TS   | 34.121-2 | User Equipment (UE) conformance specification; Radio transmission and reception (FDD); Part 2: Implementation Conformance Statement (ICS)                                                                                                                  | R5       | Yes              | 2010-03-19  | yes    |
| TS   | 34.122   | Terminal conformance specification; Radio transmission and reception (TDD)                                                                                                                                                                                 | R5       | Yes              | 2010-03-19  | yes    |
| TS   | 34.123-1 | User Equipment (UE) conformance specification; Part 1: Protocol conformance specification                                                                                                                                                                  | R5       | Yes              | 2010-03-19  | yes    |
| TS   | 34.123-2 | User Equipment (UE) conformance specification; Part 2: Implementation conformance statement (ICS) proforma specification                                                                                                                                   | R5       | Yes              | 2010-03-19  | yes    |
| TS   | 34.123-3 | User Equipment (UE) conformance specification; Part 3: Abstract test suite (ATS)                                                                                                                                                                           | R5       | Yes              | 2010-12-10  | yes    |
| TS   | 34.124   | Electromagnetic compatibility (EMC) requirements for mobile terminals and ancillary equipment                                                                                                                                                              | R4       | Yes              | 2009-12-10  | yes    |
| TS   | 34.131   | Test Specification for C-language binding to (Universal) Subscriber Interface Module ((U)SIM) Application Programming Interface (API)                                                                                                                      | C6       | Yes              | 2009-12-10  | yes    |
| TS   | 34.171   | Terminal conformance specification; Assisted Global Positioning System (A-GPS); Frequency Division Duplex (FDD)                                                                                                                                            | R5       | Yes              | 2010-03-19  | yes    |
| TS   | 34.229-1 | Internet Protocol (IP) multimedia call control protocol based on Session Initiation Protocol (SIP) and Session Description Protocol (SDP); User Equipment (UE) conformance specification; Part 1: Protocol conformance specification                       | R5       | Yes              | 2010-03-19  | yes    |
| TS   | 34.229-2 | Internet Protocol (IP) multimedia call control protocol based on Session Initiation Protocol (SIP) and Session Description Protocol (SDP); User Equipment (UE) conformance specification; Part 2: Implementation Conformance Statement (ICS) specification | R5       | Yes              | 2010-03-19  | yes    |
| TS   | 34.229-3 | Internet Protocol (IP) multimedia call control protocol based on Session Initiation Protocol (SIP) and Session Description Protocol (SDP); User Equipment (UE) conformance specification; Part 3: Abstract test suite (ATS)                                | R5       | Yes              | 2011-06-03  | yes    |
| TR   | 34.902   | Derivation of test tolerances for multi-cell Radio Resource Management (RRM) conformance tests                                                                                                                                                             | R5       | Yes              | 2011-09-16  | yes    |
| TR   | 34.926   | Electromagnetic compatibility (EMC); Table of international requirements for mobile terminals and ancillary equipment                                                                                                                                      | R4       | Yes              | 2009-12-10  | yes    |
| TS   | 35.201   | 3G Security; Specification of the 3GPP confidentiality and integrity algorithms; Document 1: f8 and f9 specification                                                                                                                                       | S3       | Yes              | 2009-12-10  | yes    |
| TS   | 35.202   | 3G Security; Specification of the 3GPP confidentiality and integrity algorithms; Document 2: Kasumi specification                                                                                                                                          | S3       | Yes              | 2009-12-10  | yes    |
| TS   | 35.203   | 3G Security; Specification of the 3GPP confidentiality and integrity algorithms; Document 3: Implementors' test data                                                                                                                                       | S3       | Yes              | 2009-12-10  | yes    |
| TS   | 35.204   | 3G Security; Specification of the 3GPP confidentiality and integrity algorithms; Document 4: Design conformance test data                                                                                                                                  | S3       | Yes              | 2009-12-10  | yes    |
| TS   | 35.205   | 3G Security; Specification of the MILENAGE algorithm set: An example algorithm set for the 3GPP authentication and key generation functions f1, f1*, f2, f3, f4, f5 and f5*; Document 1: General                                                           | S3       | Yes              | 2009-12-10  | yes    |
| TS   | 35.206   | 3G Security; Specification of the MILENAGE algorithm set: An example algorithm set for the 3GPP authentication and key generation functions f1, f1*, f2, f3, f4, f5 and f5*; Document 2: Algorithm specification                                           | S3       | Yes              | 2009-12-10  | yes    |
| TS   | 35.207   | 3G Security; Specification of the MILENAGE algorithm set: An                                                                                                                                                                                               | S3       | Yes              | 2009-       | yes    |

| Type | Number   | Title                                                                                                                                                                                                                                 | WG prime | For publication? | freeze date | frozen |
|------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|------------------|-------------|--------|
|      |          | example algorithm set for the 3GPP authentication and key generation functions f1, f1*, f2, f3, f4, f5 and f5*; Document 3: Implementors' test data                                                                                   |          |                  | 12-10       |        |
| TS   | 35.208   | 3G Security; Specification of the MILENAGE algorithm set: An example algorithm set for the 3GPP authentication and key generation functions f1, f1*, f2, f3, f4, f5 and f5*; Document 4: Design conformance test data                 | S3       | Yes              | 2009-12-10  | yes    |
| TS   | 35.215   | Specification of the 3GPP Confidentiality and Integrity Algorithms UEA2 & UIA2; Document 1: UEA2 and UIA2 specifications                                                                                                              | S3       | Yes              | 2009-12-10  | yes    |
| TS   | 35.216   | Specification of the 3GPP Confidentiality and Integrity Algorithms UEA2 & UIA2; Document 2: SNOW 3G specification                                                                                                                     | S3       | Yes              | 2009-12-10  | yes    |
| TS   | 35.217   | Specification of the 3GPP Confidentiality and Integrity Algorithms UEA2 & UIA2; Document 3: Implementors' test data                                                                                                                   | S3       | Yes              | 2009-12-10  | yes    |
| TS   | 35.218   | Specification of the 3GPP Confidentiality and Integrity Algorithms UEA2 & UIA2; Document 4: Design conformance test data                                                                                                              | S3       | Yes              | 2009-12-10  | yes    |
| TR   | 35.909   | 3G Security; Specification of the MILENAGE algorithm set: an example algorithm set for the 3GPP authentication and key generation functions f1, f1*, f2, f3, f4, f5 and f5*; Document 5: Summary and results of design and evaluation | S3       | Yes              | 2009-12-10  | yes    |
| TR   | 35.919   | Specification of the 3GPP Confidentiality and Integrity Algorithms UEA2 & UIA2; Document 5: Design and evaluation report                                                                                                              | S3       | Yes              | 2009-12-10  | yes    |
| TS   | 37.104   | E-UTRA, UTRA and GSM/EDGE; Multi-Standard Radio (MSR) Base Station (BS) radio transmission and reception                                                                                                                              | R4       | Yes              | 2009-12-10  | yes    |
| TS   | 37.113   | E-UTRA, UTRA and GSM/EDGE; Multi-Standard Radio (MSR) Base Station (BS) Electromagnetic Compatibility (EMC)                                                                                                                           | R4       | Yes              | 2010-06-04  | yes    |
| TS   | 37.141   | E-UTRA, UTRA and GSM/EDGE; Multi-Standard Radio (MSR) Base Station (BS) conformance testing                                                                                                                                           | R4       | Yes              | 2010-06-04  | yes    |
| TS   | 37.571-1 | Universal Terrestrial Radio Access (UTRA) and Evolved UTRA (E-UTRA) and Evolved Packet Core (EPC); User Equipment (UE) conformance specification for UE positioning; Part 1: Conformance test specification                           | R5       | Yes              | 2011-12-09  | yes    |
| TS   | 37.571-2 | Universal Terrestrial Radio Access (UTRA) and Evolved UTRA (E-UTRA) and Evolved Packet Core (EPC); User Equipment (UE) conformance specification for UE positioning; Part 2: Protocol conformance                                     | R5       | Yes              | 2011-12-09  | yes    |
| TS   | 37.571-3 | Universal Terrestrial Radio Access (UTRA) and Evolved UTRA (E-UTRA) and Evolved Packet Core (EPC); User Equipment (UE) conformance specification for UE positioning; Part 3: Implementation Conformance Statement (ICS)               | R5       | Yes              | 2011-12-09  | yes    |
| TS   | 37.571-4 | Universal Terrestrial Radio Access (UTRA) and Evolved UTRA (E-UTRA) and Evolved Packet Core (EPC); User Equipment (UE) conformance specification for UE positioning; Part 4: Test suites                                              | R5       | Yes              |             |        |
| TS   | 37.571-5 | Universal Terrestrial Radio Access (UTRA) and Evolved UTRA (E-UTRA) and Evolved Packet Core (EPC); User Equipment (UE) conformance specification for UE positioning; Part 5: Test scenarios and assistance data                       | R5       | Yes              | 2011-09-16  | yes    |
| TR   | 37.900   | Radio Frequency (RF) requirements for Multicarrier and Multiple Radio Access Technology (Multi-RAT) Base Station (BS)                                                                                                                 | R4       | Yes              | 2010-06-04  | yes    |

## Annex A (informative): Change history

| Change history |                              |        |           |                              |                                                                                                                                                             |
|----------------|------------------------------|--------|-----------|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TSG SA#        | Version                      | CR     | Tdoc SA   | New Version                  | Subject/Comment                                                                                                                                             |
| SP-12          | 3GPP TS 21.103 version 0.0.0 | -      | SP-010275 | 3GPP TS 21.103 version 0.1.0 | First draft                                                                                                                                                 |
|                | 0.1.0                        |        | SP-010382 | 1.0.0                        | table of specs revised                                                                                                                                      |
| SP-13          | 1.0.0                        |        | SP-010418 | 1.1.0                        | table of specs revised                                                                                                                                      |
| SP-15          | 1.1.0                        |        | SP-020095 | 1.2.0                        | table of specs revised; columns to show freeze status added                                                                                                 |
| SP-15          | 1.2.0                        |        | SP-020202 | 2.0.0                        | table of specs revised                                                                                                                                      |
| SP-16          | 2.0.0                        |        | SP-020271 | 2.1.0                        | table of specs revised                                                                                                                                      |
|                | 2.1.0                        |        | SP-020398 | 2.2.0                        | table of specs revised                                                                                                                                      |
|                | 2.2.0                        |        | SP-020410 |                              | table of specs revised; unknown freeze target dates blanked                                                                                                 |
|                |                              |        |           | 5.0.0                        | approved                                                                                                                                                    |
| SP-17          | 5.0.0                        | 001 r1 | SP-020628 | 5.1.0                        | updates lists of specs, editorial corrections to titles of specs                                                                                            |
| SP-18          | 5.1.0                        | 002 r1 | SP-020831 | 5.2.0                        | Correction to list of specs, editorial corrections to titles of specs                                                                                       |
| SP-19          | 5.2.0                        | 003 r1 | SP-030077 | 5.3.0                        | Correction to list of specs, editorial corrections to titles of specs                                                                                       |
| SP-20          | 3GPP TS 21.103 version 5.3.0 | 004    | SP-030229 | 3GPP TS 21.101 version 5.4.0 | Correction to list of specs                                                                                                                                 |
|                |                              |        | SP-030235 |                              | Renumber from 21.103 to 21.101                                                                                                                              |
| SP-22          | 5.4.0                        | 017    | SP-030574 | 5.5.0                        | Correction to list of specs, editorial corrections to spec titles                                                                                           |
| SP-23          | 5.5.0                        | 020 r2 | SP-040221 | 5.6.0                        | Corrections to list of specifications                                                                                                                       |
| SP-24          | 5.6.0                        | 021 r1 | SP-040358 | 5.7.0                        | Corrections to list of specifications                                                                                                                       |
| SP-26          | 5.7.0                        | 025 r1 | SP-040880 | 6.0.0                        | Corrections to list of specifications                                                                                                                       |
| SP-27          | 6.0.0                        | 029    | SP-050126 | 6.1.0                        | Corrections to list of specifications                                                                                                                       |
| SP-28          | 6.1.0                        | 031 r1 | SP-050356 | 6.2.0                        | Corrections to list of specifications                                                                                                                       |
| SP-29          | 6.2.0                        | 032    | SP-050470 |                              | Change instances of Release 5 to Release 6                                                                                                                  |
|                |                              | 033    | SP-050462 | 6.3.0                        | Corrections to list of specifications                                                                                                                       |
| SP-30          | 6.3.0                        | 034 r1 | SP-050845 | 6.4.0                        | Corrections to list of specifications                                                                                                                       |
| post SP-31     | 6.4.0                        |        |           | 6.4.1                        | Correction to title of reference to 21.900. Correction to spec list table entries for 23.125 and 32.251 to show that they are intended for SDO publication. |
| post SP-31     | 6.4.1                        |        |           | 6.4.2                        | Corrects cover date.                                                                                                                                        |
| SP-34          | 6.4.2                        | 038    | SP-060901 | 6.5.0                        | Correction to list of Specs and minor editorials                                                                                                            |
| SP-35          | 6.5.0                        | 038    | SP-070188 | 6.6.0                        | Corrections to list of specifications                                                                                                                       |
| SP-36          | 6.6.0                        | 041    | SP-070344 | 6.7.0                        | Corrections to list of specifications                                                                                                                       |
| SP-37          | 6.7.0                        | 042    | SP-070519 | 7.0.0                        | Upgrade to Rel-7                                                                                                                                            |
| SP-38          | 7.0.0                        | 047    | SP-070770 |                              | Corrections to list of specifications                                                                                                                       |
|                |                              | 052    |           | 7.1.0                        | Update of informative text                                                                                                                                  |
| SP-40          | 7.1.0                        | 053    | SP-080435 | 7.2.0                        | Corrections to list of specifications                                                                                                                       |
| SP-42          | 7.2.0                        | 054 r1 | SP-080722 | 7.3.0                        | Corrections to list of specifications                                                                                                                       |
| SP-43          | 7.3.0                        | 057 r1 | SP-090033 | 8.0.0                        | List of Rel-8 specifications                                                                                                                                |
| SP-44          | 8.0.0                        | 058 r1 | SP-090382 | 8.1.0                        | Corrections to list of specifications                                                                                                                       |
| SP-46          | 8.1.0                        | 064 r1 | SP-090695 | 8.2.0                        | Corrections to list of specifications                                                                                                                       |
| SP-47          | 8.2.0                        | 065    | SP-100012 | 9.0.0                        | Update list of specs                                                                                                                                        |
| SP-51          | 9.0.0                        |        |           | 9.0.1                        | Correction of Release 8 to Release 9 in Scope clause                                                                                                        |
| SP-52          | 9.0.1                        | 067    | SP-110298 | 9.1.0                        | Corrections to list of specifications                                                                                                                       |
| SP-55          | 9.1.0                        | 070 r1 | SP-120114 | 9.2.0                        | Changes to list of Specs: UTRAN systems                                                                                                                     |




<!-- ===== SOURCE FILE: raw__1_.md ===== -->



# **3rd Generation Partnership Project; Technical Specification Group Core Network and Terminals; 3GPP TS 21.111 V9.0.0 (2009-12) USIM and IC card requirements (Release 9)** ---

*Technical Specification*

![3GPP logo](30a26f2d17ca95672702bf50fb4f0242_img.jpg)

---

The 3GPP logo is displayed within a rectangular box. It features the letters '3GPP' in a stylized, bold font. The '3' is on the left, followed by two 'G's and a 'P'. Below the 'G's, there are three horizontal red lines of decreasing length, resembling signal waves. A small 'TM' trademark symbol is located in the top right corner of the box.

3GPP logo

Keywords  
UMTS, SIM, card, LTE

## **3GPP**

Postal address

---

3GPP support office address

---

650 Route des Lucioles - Sophia Antipolis  
Valbonne - FRANCE  
Tel.: +33 4 92 94 42 00 Fax: +33 4 93 65 47 16

Internet

---

<http://www.3gpp.org>

# **Copyright Notification**

No part may be reproduced except as authorized by written permission.  
The copyright and the foregoing restriction extend to reproduction in all media.

© 2009, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TTA, TTC).  
All rights reserved.

UMTS™ is a Trade Mark of ETSI registered for the benefit of its members  
3GPP™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners  
LTE™ is a Trade Mark of ETSI currently being registered for the benefit of its Members and of the 3GPP Organizational Partners  
GSM® and the GSM logo are registered and owned by the GSM Association

# --- Contents

|                                                              |    |
|--------------------------------------------------------------|----|
| Foreword .....                                               | 5  |
| 1 Scope.....                                                 | 6  |
| 2 References.....                                            | 6  |
| 2.1 Normative references .....                               | 6  |
| 2.2 Void.....                                                | 7  |
| 3 Definitions, symbols and abbreviations.....                | 7  |
| 3.1 Definitions.....                                         | 7  |
| 3.2 Void.....                                                | 7  |
| 3.3 Abbreviations .....                                      | 7  |
| 4 General requirements .....                                 | 7  |
| 5 Security requirements .....                                | 7  |
| 5.1 File access conditions.....                              | 8  |
| 5.2 User authentication.....                                 | 8  |
| 5.3 User data stored in ME.....                              | 8  |
| 5.4 Authentication .....                                     | 8  |
| 5.5 Data integrity of signalling elements .....              | 9  |
| 5.6 User identity confidentiality.....                       | 9  |
| 5.7 Length of security parameters .....                      | 9  |
| 6 Logical issues.....                                        | 9  |
| 6.1 Application selection.....                               | 9  |
| 6.2 Simultaneous access.....                                 | 9  |
| 7 Service Requirements .....                                 | 9  |
| 7.1 Void.....                                                | 9  |
| 7.2 Data transfer .....                                      | 9  |
| 7.3 Application execution environment .....                  | 10 |
| 7.4 Profile exchange.....                                    | 10 |
| 7.5 Version identification.....                              | 10 |
| 8 Physical Characteristics .....                             | 10 |
| 8.1 Void.....                                                | 10 |
| 8.2 Void.....                                                | 10 |
| 9 Electrical characteristics and transmission protocols..... | 10 |
| 9.1 Void.....                                                | 11 |
| 10 Contents of the Elementary Files.....                     | 11 |
| 10.1 USIM information storage requirements.....              | 11 |
| 10.2 Phone Book .....                                        | 11 |
| 10.2.1 Support of two name fields per entry .....            | 12 |
| 10.2.2 Support of multiple phone numbers per entry .....     | 12 |
| 10.2.3 Support of email address .....                        | 12 |
| 10.2.4 Support of user definable groupings.....              | 12 |
| 10.2.5 Support of hidden entries.....                        | 12 |
| 10.2.6 Number of entries .....                               | 12 |
| 10.2.7 Void.....                                             | 12 |
| 10.3 Storage of call details .....                           | 12 |
| 10.4 Void.....                                               | 13 |
| 11 3G/GSM interworking .....                                 | 13 |
| 11.1 Void.....                                               | 13 |
| 11.2 3G subscribers in a GSM network .....                   | 13 |
| 12 Contact Manager.....                                      | 13 |
| Annex A (informative): Change history.....                   | 16 |

# --- Foreword

This Technical Specification has been produced by the 3GPP.

The contents of the present document are subject to continuing work within the TSG and may change following formal TSG approval. Should the TSG modify the contents of this TS, it will be re-released by the TSG with an identifying change of release date and an increase in version number as follows:

Version x.y.z

where:

- x the first digit:
  - 1 presented to TSG for information;
  - 2 presented to TSG for approval;
  - 3 or greater indicates TSG approved document under change control.
- y the second digit is incremented for all changes of substance, i.e. technical enhancements, corrections, updates, etc.
- z the third digit is incremented when editorial only changes have been incorporated in the document.

# --- 1 Scope

This document defines the requirements of the USIM (Universal Subscriber Identity Module) and the IC card for 3G (UICC). These are derived from the service and security requirements defined in TS 22.100 [1] and TS 22.101 [2]. The USIM is a 3G application on an IC card. It inter-operates with a 3G terminal and provides access to 3G services. This document is intended to serve as a basis for the detailed specification of the USIM and the UICC, and the interface to the 3G terminal.

# --- 2 References

## 2.1 Normative references

The following documents contain provisions which, through reference in this text, constitute provisions of the present document.

- References are either specific (identified by date of publication, edition number, version number, etc.) or non-specific.
- For a specific reference, subsequent revisions do not apply.
- For a non-specific reference, the latest version applies. In the case of a reference to a 3GPP document (including a GSM document), a non-specific reference implicitly refers to the latest version of that document in the same Release as the present document.

- [1] 3GPP TS 22.100 v3.x.x: "UMTS phase 1" (Release 99).
- [2] 3GPP TS 22.101: "Service principles".
- [3] 3GPP TS 31.101: "UICC-Terminal Interface; Physical and Logical Characteristics".
- [4] Void.
- [5] ETSI TS 101 220: "ETSI Numbering System for AIDs".
- [6] 3GPP TS 31.111: "USIM Application Toolkit (USAT)".
- [7] 3GPP TS 33.102: "3G Security: Security Architecture".
- [8] 3GPP TS 51.011, Rel-4: "Specification of the Subscriber Identity Module - Mobile Equipment (SIM - ME) interface".
- [9] Void.
- [10] Void.
- [11] ISO/IEC 7816-3: "Information technology - Identification cards - Integrated circuit(s) cards with contacts - Part 3: Electronic signals and transmission protocols".
- [12] ISO/IEC 7816-4: "Identification cards - Integrated circuit cards, Part 4: Organization, security and commands for interchange".
- [13] Void.

## 2.2 Void ---

# 3 Definitions, symbols and abbreviations

## 3.1 Definitions

For the purposes of the present document, the following definitions apply:

## 3.2 Void

## 3.3 Abbreviations

For the purposes of the present document, the following abbreviations apply:

|      |                                          |
|------|------------------------------------------|
| ADN  | Abbreviated Dialling Number              |
| ATR  | Answer To Reset                          |
| DF   | Dedicated File                           |
| EF   | Elementary File                          |
| ICC  | Integrated Circuit Card                  |
| IK   | Integrity Key                            |
| IMSI | International Mobile Subscriber Identity |
| ME   | Mobile Equipment                         |
| MF   | Master File                              |
| PIN  | Personal Identification Number           |
| PPS  | Protocol and Parameter Selection         |
| SIM  | Subscriber Identity Module               |
| USIM | Universal Subscriber Identity Module     |

# --- 4 General requirements

The UICC shall be a removable hardware module. The USIM on a UICC shall contain an identity which unambiguously identifies a subscriber.

For access to 3G services, a UICC containing a valid USIM shall be present at all times, other than for emergency calls.

The specifications shall support the security requirements as defined in 3GPP TS 33.102 [7].

The USIM shall provide storage for subscription and subscriber related information.

The UICC/USIM may also contain applications which use the features defined in the USIM Application Toolkit specification 3GPP TS 31.111 [6].

# --- 5 Security requirements

The USIM shall be used to provide security features. If the UICC is removed from the 3G terminal, the service shall be terminated immediately. The functions of the USIM include authenticating itself to the network and vice versa, authenticating the user and providing additional security functions as defined in 3GPP TS 33.102 [7].

The USIM shall be unambiguously identified.

Means shall be provided to prevent fraudulent use of stolen UICCs.

It shall not be possible to access data intended for USIM internal use, e.g. authentication keys.

Further details of the following requirements are given in 3GPP TS 33.102 [7].

## 5.1 File access conditions

Actions, such as READ, UPDATE on UICC data shall be controlled by access conditions. These shall be satisfied prior to the action being performed.

Since a UICC may contain multiple (3G and non-3G) applications, a flexible method of controlling file access shall be provided.

## 5.2 User authentication

The USIM shall support means to authenticate the user, to provide, for example, protection against the use of stolen cards. For the USIM, authentication shall be performed by the verification of a numeric PIN of four (4) to eight (8) decimal digits.

A function to disable user authentication may exist which may be inhibited by the application provider, in which case the user shall always use the PIN. Otherwise, the user may decide whether or not to make use of the user authentication function. If disabled, the user authentication function remains disabled until the user specifically re-enables it.

Following correct PIN presentation, the ME may perform functions and actions on USIM data, which are protected by the relevant access condition.

If an incorrect PIN is entered, an indication shall be given to the user. After three (3) consecutive incorrect entries the relevant PIN is blocked, i.e. functions and actions on data protected by the access condition shall no longer be possible, even if between attempts the UICC has been removed, the USIM has been deselected or the ME has been switched off. Once a PIN is blocked, further PIN verifications shall be denied.

The USIM shall support a mechanism for unblocking a blocked PIN. Unblocking of a PIN is performed by using the relevant PIN Unblocking Key.

PINs, but not Unblock PINs, shall be changeable by the user following correct entry of either the current PIN or Unblock PIN.

The Unblock PIN shall consist of eight (8) decimal digits and shall not be changeable by the user. If an incorrect Unblock PIN is presented, an indication shall be given to the user. After ten (10) consecutive incorrect entries, the Unblock PIN shall be blocked, even if between attempts the UICC has been removed, the USIM has been deselected or the ME has been switched off. Unblocking of a blocked PIN shall not be possible.

It shall not be possible to read PINs or Unblock PINs.

## 5.3 User data stored in ME

Subject to the exception below, all user related information transferred into the ME during network operations shall be deleted from the ME after removal of the UICC, deselection of the USIM, deactivation of the ME, or following an electrical reset of the UICC. This includes any data that was transferred to the ME by USIM Application Toolkit commands.

User related security codes such as PIN and Unblock PIN may only be stored by the ME during the procedures involving such a code and shall be discarded by the ME immediately after completion of the procedure.

Optionally, an ME may retain some less security-sensitive data at UICC removal, USIM deselection or ME switch-off. Such data are e.g. SMS, ADN/SSC, FDN/SSC, LND. These data, when stored in the ME, shall only be readable/retrievable if the same USIM is reactivated (as determined by the IMSI). If the IMSI is retained in the ME for this purpose, it shall be stored securely and shall not be able to be read out.

## 5.4 Authentication

A means shall be specified to mutually authenticate the USIM and the network by showing knowledge of a secret key K which is shared between and available only to the USIM and in the user's Home Environment. The method is composed of a challenge/response and key establishment protocol combined with a sequence number-based one-pass protocol for network authentication.

## 5.5 Data integrity of signalling elements

Some signalling information elements are considered sensitive and must be integrity protected. An integrity function shall be applied on certain signalling information elements transmitted between the ME and the network.

The 3GPP Integrity Algorithm (UIA) is used with an Integrity Key (IK) to compute a message authentication code for a given message. The setting of IK is triggered by the authentication procedure. IK shall be stored on the USIM.

## 5.6 User identity confidentiality

A mechanism shall be specified to provide user identity confidentiality by means of a temporary identity.

## 5.7 Length of security parameters

In order to allow for enhancements of the security level in 3G, the following requirements shall be covered:

- all security-related parameters for 3G shall be accompanied by a length indicator;
- the USIM shall support variable-length security parameters.

If the USIM supports the GSM security mechanisms in addition to 3G security, fixed length security parameters according to 3GPP TS 51.011 [8] shall be supported in addition.

# --- 6 Logical issues

## 6.1 Application selection

In a multiapplication environment, a flexible application selection method is required. The application identifier defined in ETSI TS 101 220 [5] should be used for application selection. Direct application selection, including selection by partial DF name and the EF<sub>DIR</sub> concept of ISO/IEC 7816-4 [12] shall be followed. In particular, a mechanism for the ME and the UICC shall be specified in order to allow the user, when the ME is in idle mode, to select and activate one application amongst those which are available and supported by the ME (this will permit the user to choose, for instance, between 2 different USIM applications). At switch on, the last active USIM shall be automatically selected. The last active USIM shall be stored on the UICC. By default if there is no last active USIM defined in the UICC, the user shall be able to select the active USIM amongst those available on the UICC.

## 6.2 Simultaneous access

A mechanism shall be specified for simultaneous access to several files or applications.

# --- 7 Service Requirements

## 7.1 Void

## 7.2 Data transfer

A mechanism allowing highly secure transfer of applications and/or associated data to/from the UICC/USIM shall be specified in line with the requirements in 3GPP TS 22.101 [2]. This requires a secure transfer mechanism.

## 7.3 Application execution environment

An application execution environment may exist on the UICC/USIM which includes functionality defined in 3GPP TS 31.111 [6].

## 7.4 Profile exchange

A mechanism for the ME, the USIM and the network to exchange service capabilities shall be specified. The following exchange of service capabilities may occur:

- ME services capabilities may be provided to the USIM/UICC;
- USIM/UICC services capabilities may be provided to the ME (and thus potentially to the network);
- network services capabilities may be provided to the USIM/UICC via the ME.

## 7.5 Version identification

A means for identification of the version of the USIM shall be provided.

# --- 8 Physical Characteristics

The physical characteristics shall be in accordance with the specifications in 3GPP TS 31.101 [3].

## 8.1 Void

## 8.2 Void

# --- 9 Electrical characteristics and transmission protocols

Electronic signals and transmission protocols shall be in accordance with the specifications in 3GPP TS 31.101 [3].

The electrical specifications shall at least cover the 1.8V and 3V voltage ranges as specified in 3GPP TS 31.101 [3]. Lower voltages may be added in the future. 3G terminals shall not support 5V on the ME-UICC interface. Both ME and UICC shall support operational class indication as defined in ISO/IEC 7816-3 [11].

Both ME and UICC shall support at least two voltage classes.

Both UICC and ME shall support PPS as defined in ISO/IEC 7816-3 [11] with at least the values defined in 3GPP TS 31.101 [3].

The ME shall have the capabilities of initiating a warm reset as defined in ISO/IEC 7816-3 [11]. The UICC shall support warm reset as defined in ISO/IEC 7816-3 [11].

NOTE: The warm reset is used during a session when there is a need to restart the USIM due to internal modifications of data caused by user actions or network data downloading.

The UICC may indicate in the ATR to the warm reset that the specific mode is entered automatically, using the parameters that were used prior to the warm reset. In case of a cold reset, the UICC shall enter the negotiable mode.

In addition to the T=0 protocol which is mandatory for the UICC and the ME, the T=1 protocol shall be mandatory for the ME. It is optional for the UICC.

The speed enhancement as specified in 3GPP TS 31.101 [3] shall be supported by both the ME and the UICC.

## 9.1 Void

# --- 10 Contents of the Elementary Files

## 10.1 USIM information storage requirements

The USIM shall contain information elements for 3G network operations. The USIM may contain information elements related to the subscriber, 3G services and home environment or service provider related information.

The UICC shall provide storage capability for the following:

- UICC related information:
  - IC card identification: a number uniquely identifying the UICC and the card issuer;
  - Preferred language(s);
  - Directory of applications.

- USIM related information:
  - Administrative information: indicates mode of operation of the USIM, e.g. normal, type approval;
  - USIM service table: indicates which optional services are provided by the USIM;
  - IMSI;
  - Language indication;
  - Location information;
  - Cipher key (Kc) and cipher key sequence number;
  - Access control class(es);
  - Forbidden PLMNs;
  - Ciphering Key for GPRS;
  - GPRS location information;
  - Cell Broadcast related information;
  - Emergency call codes;
  - Phone numbers (ADN, FDN, SDN);
  - Short messages and related parameters;
  - Capability and Configuration parameters;
  - Higher Priority PLMN search period;
  - list of carrier frequencies to be used for cell selection.
- Information accessible to the USIM and other applications:
  - ADN.

In addition, the USIM shall manage and provide storage for the following information in accordance with the security requirements of clause 5:

- PIN;
- PIN enabled/disabled indicator;
- PIN error counter;
- Unblock PIN;
- Unblock PIN error counter;
- Data integrity keys;
- Subscriber authentication keys.

## 10.2 Phone Book

A Phone Book entry consists of a record in an ADN file and, optionally, additional records which are placed in different EFs. In the latter case, a mechanism shall be defined to link all records in the same Phone Book entry. These features shall be supported by the ME while their support by the UICC is optional.

### 10.2.1 Support of two name fields per entry

The support of two name fields per entry shall be specified to allow, for example, for two different representations of the same name (for example, in Japanese characters and in Latin characters).

### 10.2.2 Support of multiple phone numbers per entry

The support of multiple phone numbers per entry shall be specified, for example, office, home, fax, mobile or pager. In addition to that, information for identifying those attributes are needed.

### 10.2.3 Support of email address

The support of email addresses linked to Phone Book entries shall be specified. In addition to that, information for identifying these addresses is needed.

### 10.2.4 Support of user definable groupings

The specification shall support the grouping of Phone Book entries into groups defined by the user, for example,

business and private.

### 10.2.5 Support of hidden entries

The specification shall support means of marking Phone Book entries as "hidden".

### 10.2.6 Number of entries

The specification shall support storage of at least 500 entries.

### 10.2.7 Void

## 10.3 Storage of call details

The specification shall support provision of storage for call detail information. The call detail information consists of the following attributes:

- mobile terminated calls:  
calling party number, date and time, calling party's name and status of call (i.e. answered or missed), duration;
- mobile originated calls:  
called party number, date and time, called party's name and duration;
- accumulated duration of preceding calls, separately for mobile originated and mobile terminated calls.

Call detail attributes are optional. A value to mark them as "undefined" shall be available.

NOTE 1: The calling/called party's name may be available from the Phone Book.

## 10.4 Void ---

# 11 3G/GSM interworking

## 11.1 Void

## 11.2 3G subscribers in a GSM network

3GPP TS 22.101 [2] requires that UMTS shall provide some mechanisms which permit UMTS subscribers to roam easily onto pre-UMTS systems and access the services.

Thus, the specification shall allow the UICC to be used with a dual mode (GSM/ 3G) ME and a GSM ME for the provision of GSM service.

---

# 12 Contact Manager

## 12.1 General

The Contact Manager provides an interface for the management of contact information including rich content without any structural limitations.

There shall be a mechanism for the ME to detect that the UICC containing the Contact Manager has changed. This mechanism may be used by the ME to ask the user whether synchronization of data between the ME and the UICC Contact Manager should occur.

This section defines the functional requirements of the Contact Manager. An ME and a 3GPP application supporting the Contact Manager shall comply with all these requirements.

## 12.2 Security requirements

The Contact Manager may contain personal information. It shall be possible to restrict the access to this information to authorized users or entities (e.g. by binding the access to the verification of the USIM PIN).

### 12.4.3 Interworking with the 3G Phone Book

In case both the ME and the 3GPP application support both the 3G Phone Book (i.e. as defined in section 10.2 of the present document) and the Contact Manager the Contact Manager shall be used. There shall be a mechanism for the 3GPP application to indicate the support of the Contact Manager.

### 12.4.4 Content description

#### 12.4.4.1 Number of contacts

The Contact Manager specification shall not unreasonably restrict the number of contacts.

#### 12.4.4.2 Contact structure

The Contact Manager shall consist of contacts, which are made up of various fields (e.g. phone number, name, photo). A filtering mechanism according to OMA DS Field Filtering shall be supported.

It shall be possible to have several instances of a field in a contact when appropriate (e.g. a contact may have two fax numbers).

An extensible coding scheme shall be defined which allows to describe a contact including all its fields. An existing scheme (e.g. "vcard") shall be used, if appropriate.

A minimum set of field types recognised by the 3GPP application and the ME shall be defined (e.g. name, phone number, URL, Email address, address, sound, pictures, notes).

It shall be possible to store and associate multimedia information (stored on the 3GPP application) with a contact (e.g. photo, logo, video, ring tone, voice tag).

It shall be possible to associate an icon or a label to each contact field type (e.g. associate an icon representing a phone to the number field. "Home address" could be configured as the label of the "mailing address" field type).

It shall be possible to configure the structure and the display order of the contact fields (e.g. first name then Instant Messaging address then number, etc) depending on ME capabilities.

#### 12.4.4.3 Group management

It shall be possible to define new groups (e.g. My Tennis Club).

It shall be possible to pre-define groups (e.g. Friend, Work, Family and VIP).

It shall be possible to store and associate multimedia information (stored on the 3GPP application) with a group (e.g. photo, logo, video, ring tone, icon).

It shall be possible to bind contacts to one or several groups.

#### 12.4.4.4 User Action Management

It shall be possible to configure a list of possible actions that could be proposed to the user when the contact is selected (e.g. Launch Browser, Send SMS, Send MMS, Instant messaging, Make a voice over IP call, Make a video call, Make a conference call, Game player, Send Email).

### 12.4.5 Interface capabilities description

An external and an internal interface to the Contact Manager shall be defined.

The external interface between the Contact Manager and a UICC external entity, i.e. the ME, shall rely on a transport protocol layer that is independent of the physical interface (i.e. the ISO interface and the new high-speed interface).

This is to allow the definition of one solution that can use either the existing ISO interface or the new high-speed interface. The external interface definition shall also ease interfacing the PC applications with the Contact Manager.

Both the ME and the UICC shall be capable of initiating contact information synchronization based on a configurable policy. The internal interface allows other UICC resident applications to access the Contact Manager e.g. through a dedicated API. This enables the creation of additional services utilizing the Contact Manager data and properties. There shall be a mechanism for the user to allow or prevent remote access to the Contact Manager.

The external and internal interface shall provide means to:

- identify Contact Manager capabilities
- perform the following operations on a contact or a group: create, retrieve, modify, delete, search

In addition the internal interface shall provide mechanisms to:

- register/deregister an UICC resident application to the Contact Manager.
- allow a resident UICC application to access Contact Manager data and properties based on user permission.
- allow the Contact Manager to notify events to registered UICC application and to pass event related information when applicable. Events notifying the applications shall include:
  - contact information is modified locally
  - contact information is modified remotely
  - change of contact manager configuration

### 12.4.6 Efficient browsing and searching

The Contact Manager interfaces should allow efficient searching and browsing of the contacts (i.e. the user experience browsing the Contact Manager should be acceptable).

### 12.4.7 Associated services

#### 12.4.7.1 Memory management

It shall be possible to determine the number of stored contacts and the amount of the available and used Contact Manager memory.

# Annex A (informative): Change history

The table below indicates all change requests that have been incorporated into the present document since it was initially approved by 3GPP TSG T and subsequently 3GPP TSG CT.

| Change history |       |             |      |     |     |                                                                                                                                                                         |       |       |
|----------------|-------|-------------|------|-----|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|-------|
| Date           | TSG # | TSG Doc.    | CR   | Rev | Cat | Subject/Comment                                                                                                                                                         | Old   | New   |
| 1999-06        | TP-03 | TP-99085    |      |     |     | Draft specification first approved at TSG-T #3                                                                                                                          | 2.0.0 | 3.0.0 |
| 1999-12        | TP-06 | TP-99255    | 001  |     | D   | References to new specifications and editorial changes                                                                                                                  | 3.0.0 | 3.0.1 |
| 2000-04        | TP-07 | TP-000017   | 002  |     | F   | Location of the UIA (3GPP integrity algorithm) aligned with 33.102                                                                                                      | 3.0.1 | 3.1.0 |
| 2000-07        | TP-08 | TP-000097   | 003  |     | F   | Clarification of USIM application selection                                                                                                                             | 3.1.0 | 3.2.0 |
|                |       | TP-000097   | 004  |     | F   | Alignment with 33.102: removal of Enhanced User Identity Confidentiality (EUIC) from R99                                                                                |       |       |
| 2000-10        | TP-09 | TP-000150   | 005  |     | F   | Partial AID selection requirements                                                                                                                                      | 3.2.0 | 3.3.0 |
| 2001-03        | TP-11 | -           | -    |     |     | Issued as version 4.0.0 in order to create a complete set of specifications for release 4. The contents of version 4.0.0 are identical to the contents of version 3.3.0 | 3.3.0 | 4.0.0 |
| 2002-06        | TP-16 | -           | -    |     |     | Issued as version 5.0.0 in order to create a complete set of specifications for release 5. The contents of version 5.0.0 are identical to the contents of version 4.0.0 | 4.0.0 | 5.0.0 |
| 2002-09        | TP-17 | TP-020208   | 009  |     | A   | Clarification on the use of the USIM and the SIM                                                                                                                        | 5.0.0 | 5.1.0 |
| 2004-03        | TP-23 | TP-040023   | 010  |     | C   | Update with respect to the third form factor and removal of an unused reference                                                                                         | 5.1.0 | 6.0.0 |
| 2004-06        | TP-24 | TP-040100   | 011  |     | D   | Release 6 alignment                                                                                                                                                     | 6.0.0 | 6.1.0 |
| 2005-06        | CT-28 | CP-050136   | 015  |     | A   | ISO/IEC 7816-Series Revision                                                                                                                                            | 6.1.0 | 6.2.0 |
| 2006-05        | CT-32 | CP-060349   | 0017 | 1   | F   | Review of TS 21.111, USIM and IC Card Requirements                                                                                                                      | 6.2.0 | 6.3.0 |
| 2006-09        | CT-33 | action item | -    |     | -   | MCC to raise spec to Rel-7                                                                                                                                              | 6.3.0 | 7.0.0 |
| 2007-03        | CT-35 | CP-070070   | 0019 | 2   | B   | Requirements for the Enhanced USIM phonebook                                                                                                                            | 7.0.0 | 8.0.0 |
| 2007-10        |       |             |      |     |     | Editorial correction to cover page                                                                                                                                      | 8.0.0 | 8.0.1 |
| 2007-12        | CT-38 | CP-070839   | 0020 | 2   | B   | Completion of the requirements for the Enhanced USIM phonebook<br>Renaming of the feature to Contact Manager.<br>Contact Manager moved to a dedicated section           | 8.0.1 | 8.1.0 |
| 2008-05        | CT-40 | CP-080384   | 0023 | 2   | F   | Update and correct references and pointers to references                                                                                                                | 8.1.0 | 8.2.0 |
| 2009-12        | CT-46 | CP-091042   | 0025 | 2   | F   | References update                                                                                                                                                       | 8.2.0 | 8.3.0 |
| 2009-12        | CT-46 | -           | -    | -   | -   | Upgrade of the specification to Rel-9                                                                                                                                   | 8.3.0 | 9.0.0 |


<!-- ===== SOURCE FILE: raw__2_.md ===== -->







# --- Contents

- Foreword ..... 4
- 1 Scope..... 5
- 2 References..... 5
- 3 Definitions, symbols and abbreviations..... 5
  - 3.1 Definitions..... 5
  - 3.2 Symbols..... 5
  - 3.3 Abbreviations ..... 5
- 4 General..... 5
- 5 Specifications and Reports..... 6
- Annex A (informative): Change history..... 29

# --- Foreword

This Technical Specification has been produced by the 3<sup>rd</sup> Generation Partnership Project (3GPP).

The contents of the present document are subject to continuing work within the TSG and may change following formal TSG approval. Should the TSG modify the contents of the present document, it will be re-released by the TSG with an identifying change of release date and an increase in version number as follows:

Version x.y.z

where:

- x the first digit:
  - 1 presented to TSG for information;
  - 2 presented to TSG for approval;
  - 3 or greater indicates TSG approved document under change control.
- y the second digit is incremented for all changes of substance, i.e. technical enhancements, corrections, updates, etc.
- z the third digit is incremented when editorial only changes have been incorporated in the document.

# --- 1 Scope

The present document identifies the 3GPP system specifications for Release 9. The specifications and reports of 3GPP Release 8 have a major version number 9 (i.e. 9.x.y). The listed Specifications are required to build a system based on the Evolved Packet System.

The high-level architecture of such a system is defined in 3GPP TS 23.002 [2] (figure 1b).

# --- 2 References

The following documents contain provisions which, through reference in this text, constitute provisions of the present document.

- References are either specific (identified by date of publication, edition number, version number, etc.) or non-specific.
- For a specific reference, subsequent revisions do not apply.
- For a non-specific reference, the latest version applies. In the case of a reference to a 3GPP document (including a GSM document), a non-specific reference implicitly refers to the latest version of that document *in the same Release as the present document*.

[1] 3GPP TR 21.905: "Vocabulary for 3GPP Specifications".

[2] 3GPP TS 23.002: "Network architecture".

# --- 3 Definitions, symbols and abbreviations

## 3.1 Definitions

For the purposes of the present document, the terms and definitions given in TR 21.905 [1] apply.

## 3.2 Symbols

(Void)

## 3.3 Abbreviations

For the purposes of the present document, the abbreviations given in TR 21.905 [1] apply.

# --- 4 General

The numbering scheme for specifications is described in 3GPP TR 21.900 [2].

# 5 Specifications and Reports

NOTE 1: The "for publication?" column of the table below indicates whether or not the documents are intended for adoption by the partner Standards Development Organizations as their own publications. Those marked "no" are internal working documents of the 3GPP TSGs.

NOTE 2: "Type" indicates Technical Specification (TS) or Technical Report (TR).

| Type | Number | Title                                                                                               | Group | For publication? |
|------|--------|-----------------------------------------------------------------------------------------------------|-------|------------------|
| TS   | 21.111 | USIM and IC card requirements                                                                       | C6    | Yes              |
| TS   | 21.201 | Technical Specifications and Technical Reports for an Evolved Packet System (EPS) based 3GPP system | SP    | Yes              |
| TS   | 21.202 | Technical Specifications and Technical Reports relating to the Common IP Multimedia Subsystem (IMS) | SP    | Yes              |
| TR   | 21.801 | Specification drafting rules                                                                        | SP    | No               |
| TR   | 21.900 | Technical Specification Group working methods                                                       | SP    | Yes              |
| TR   | 21.902 | Evolution of 3GPP system                                                                            | SP    | Yes              |
| TR   | 21.905 | Vocabulary for 3GPP Specifications                                                                  | SP    | Yes              |
| TS   | 22.011 | Service accessibility                                                                               | S1    | Yes              |
| TS   | 22.016 | International Mobile station Equipment Identities (IMEI)                                            | S1    | Yes              |
| TS   | 22.022 | Personalisation of Mobile Equipment (ME); Mobile functionality specification                        | S1    | Yes              |
| TS   | 22.024 | Description of Charge Advice Information (CAI)                                                      | S1    | Yes              |
| TS   | 22.030 | Man-Machine Interface (MMI) of the User Equipment (UE)                                              | S1    | Yes              |
| TS   | 22.031 | 3G Security; Fraud Information Gathering System (FIGS); Service description; Stage 1                | S3    | Yes              |
| TS   | 22.032 | Immediate Service Termination (IST); Service description; Stage 1                                   | S3    | Yes              |
| TS   | 22.038 | (U)SIM Application Toolkit (USAT); Service description; Stage 1                                     | S1    | Yes              |
| TS   | 22.041 | Operator Determined Barring (ODB)                                                                   | S1    | Yes              |
| TS   | 22.042 | Network Identity and TimeZone (NITZ); Service description; Stage 1                                  | S1    | Yes              |
| TS   | 22.053 | Tandem Free Operation (TFO); Service description; Stage 1                                           | S4    | Yes              |
| TS   | 22.057 | Mobile Execution Environment (MExE); Service description; Stage 1                                   | S1    | Yes              |
| TS   | 22.060 | General Packet Radio Service (GPRS); Service description; Stage 1                                   | S1    | Yes              |
| TS   | 22.066 | Support of Mobile Number Portability (MNP); Service description; Stage 1                            | S1    | Yes              |
| TS   | 22.071 | Location Services (LCS); Service description; Stage 1                                               | S1    | Yes              |
| TS   | 22.076 | Noise suppression for the AMR codec; Service description; Stage 1                                   | S4    | Yes              |
| TS   | 22.097 | Multiple Subscriber Profile (MSP) Phase 2; Service description; Stage 1                             | S1    | Yes              |
| TS   | 22.101 | Service aspects; Service principles                                                                 | S1    | Yes              |
| TS   | 22.105 | Services and service capabilities                                                                   | S1    | Yes              |
| TS   | 22.115 | Service aspects; Charging and billing                                                               | S1    | Yes              |
| TS   | 22.127 | Service requirement for the Open Services Access (OSA); Stage 1                                     | S1    | Yes              |
| TS   | 22.129 | Service aspects; Handover requirements between UTRAN and GERAN or other radio systems               | S1    | Yes              |
| TS   | 22.135 | Multicall; Service description; Stage 1                                                             | S1    | Yes              |
| TS   | 22.140 | Multimedia Messaging Service (MMS); Stage 1                                                         | S1    | Yes              |
| TS   | 22.141 | Presence service; Stage 1                                                                           | S1    | Yes              |
| TS   | 22.146 | Multimedia Broadcast/Multicast Service (MBMS); Stage 1                                              | S1    | Yes              |
| TS   | 22.153 | Multimedia priority service                                                                         | S1    | Yes              |

| Type | Number | Title                                                                                                       | Group | For publication? |
|------|--------|-------------------------------------------------------------------------------------------------------------|-------|------------------|
| TS   | 22.173 | IP Multimedia Core Network Subsystem (IMS) Multimedia Telephony Service and supplementary services; Stage 1 | S1    | Yes              |
| TS   | 22.174 | Push Service; Service aspects; Stage 1                                                                      | S1    | Yes              |
| TS   | 22.182 | Customized Alerting Tones (CAT) requirements; Stage 1                                                       | S1    | Yes              |
| TS   | 22.226 | Global Text Telephony (GTT); Stage 1                                                                        | S1    | Yes              |
| TS   | 22.228 | Service requirements for the Internet Protocol (IP) multimedia core network subsystem (IMS); Stage 1        | S1    | Yes              |
| TS   | 22.233 | Transparent end-to-end packet-switched streaming service; Stage 1                                           | S1    | Yes              |
| TS   | 22.234 | Requirements on 3GPP system to Wireless Local Area Network (WLAN) interworking                              | S1    | Yes              |
| TS   | 22.240 | Service requirements for 3GPP Generic User Profile (GUP); Stage 1                                           | S1    | Yes              |
| TS   | 22.242 | Digital Rights Management (DRM); Stage 1                                                                    | S1    | Yes              |
| TS   | 22.243 | Speech recognition framework for automated voice services; Stage 1                                          | S1    | Yes              |
| TS   | 22.246 | Multimedia Broadcast/Multicast Service (MBMS) user services; Stage 1                                        | S1    | Yes              |
| TS   | 22.250 | IP Multimedia Subsystem (IMS) Group Management; Stage 1                                                     | S1    | Yes              |
| TS   | 22.259 | Service requirements for Personal Network Management (PNM); Stage 1                                         | S1    | Yes              |
| TS   | 22.278 | Service requirements for the Evolved Packet System (EPS)                                                    | S1    | Yes              |
| TS   | 22.279 | Combined Circuit Switched (CS) and IP Multimedia Subsystem (IMS) sessions; Stage 1                          | S1    | Yes              |
| TS   | 22.340 | IP Multimedia Subsystem (IMS) messaging; Stage 1                                                            | S1    | Yes              |
| TR   | 22.903 | Study on Videotelephony teleservice                                                                         | S1    | Yes              |
| TR   | 22.908 | Study on Paging Permission with Access Control (PPAC)                                                       | S1    | Yes              |
| TR   | 22.934 | Feasibility study on 3GPP system to Wireless Local Area Network (WLAN) interworking                         | S1    | Yes              |
| TR   | 22.935 | Feasibility study on Location Services (LCS) for Wireless Local Area Network (WLAN) interworking            | S1    | Yes              |
| TR   | 22.936 | Multi-system terminals                                                                                      | S1    | Yes              |
| TR   | 22.937 | Requirements for service continuity between mobile and Wireless Local Area Network (WLAN) networks          | S1    | Yes              |
| TR   | 22.940 | IP Multimedia Subsystem (IMS) messaging                                                                     | S1    | Yes              |
| TR   | 22.942 | Study on Value Added Services (VAS) for Short Message Service (SMS)                                         | S1    | Yes              |
| TR   | 22.944 | Report on service requirements for UE functionality split                                                   | S1    | Yes              |
| TR   | 22.948 | Study of requirements of IP-Multimedia Subsystem (IMS) convergent multimedia conferencing                   | S1    | Yes              |
| TR   | 22.949 | Study on a generalized privacy capability                                                                   | S1    | Yes              |
| TR   | 22.950 | Priority service feasibility study                                                                          | S1    | Yes              |
| TR   | 22.951 | Service aspects and requirements for network sharing                                                        | S1    | Yes              |
| TR   | 22.952 | Priority service guide                                                                                      | S1    | Yes              |
| TR   | 22.953 | Multimedia priority service feasibility study                                                               | S1    | Yes              |
| TR   | 22.967 | Transferring of emergency call data                                                                         | S1    | Yes              |
| TR   | 22.968 | Study for requirements for a Public Warning System (PWS) service                                            | S1    | Yes              |
| TR   | 22.973 | IMS Multimedia Telephony service; and supplementary services                                                | S1    | Yes              |
| TR   | 22.977 | Feasibility study for speech-enabled services                                                               | S1    | Yes              |
| TR   | 22.978 | All-IP network (AIPN) feasibility study                                                                     | S1    | Yes              |
| TR   | 22.979 | Feasibility study on combined Circuit Switched (CS) calls and IP Multimedia Subsystem (IMS) sessions        | S1    | Yes              |
| TR   | 22.980 | Network composition feasibility study                                                                       | S1    | Yes              |
| TR   | 22.982 | Study of Customised Alerting Tone (CAT) requirements                                                        | S1    | Yes              |

| Type | Number | Title                                                                                                                                | Group | For publication? |
|------|--------|--------------------------------------------------------------------------------------------------------------------------------------|-------|------------------|
| TR   | 22.983 | Services alignment and migration                                                                                                     | S1    | Yes              |
| TS   | 23.002 | Network architecture                                                                                                                 | S2    | Yes              |
| TS   | 23.007 | Restoration procedures                                                                                                               | C4    | Yes              |
| TS   | 23.008 | Organization of subscriber data                                                                                                      | C4    | Yes              |
| TS   | 23.012 | Location management procedures                                                                                                       | C4    | Yes              |
| TS   | 23.018 | Basic call handling; Technical realization                                                                                           | C4    | Yes              |
| TS   | 23.038 | Alphabets and language-specific information                                                                                          | C1    | Yes              |
| TS   | 23.042 | Compression algorithm for text messaging services                                                                                    | C1    | Yes              |
| TS   | 23.107 | Quality of Service (QoS) concept and architecture                                                                                    | S2    | Yes              |
| TS   | 23.110 | Universal Mobile Telecommunications System (UMTS) access stratum; Services and functions                                             | S2    | Yes              |
| TS   | 23.119 | Gateway Location Register (GLR); Stage2                                                                                              | C4    | Yes              |
| TS   | 23.135 | Multicall supplementary service; Stage 2                                                                                             | C4    | Yes              |
| TS   | 23.141 | Presence service; Architecture and functional description                                                                            | S2    | Yes              |
| TS   | 23.142 | Value-added Services for SMS (VAS4SMS); Interface and signalling flow                                                                | C4    | Yes              |
| TS   | 23.153 | Out of band transcoder control; Stage 2                                                                                              | C4    | Yes              |
| TS   | 23.167 | IP Multimedia Subsystem (IMS) emergency sessions                                                                                     | S2    | Yes              |
| TS   | 23.198 | Open Service Access (OSA); Stage 2                                                                                                   | CP    | Yes              |
| TS   | 23.203 | Policy and charging control architecture                                                                                             | S2    | Yes              |
| TS   | 23.204 | Support of Short Message Service (SMS) over generic 3GPP Internet Protocol (IP) access; Stage 2                                      | S2    | Yes              |
| TS   | 23.205 | Bearer-independent circuit-switched core network; Stage 2                                                                            | C4    | Yes              |
| TS   | 23.207 | End-to-end Quality of Service (QoS) concept and architecture                                                                         | S2    | Yes              |
| TS   | 23.216 | Single Radio Voice Call Continuity (SRVCC); Stage 2                                                                                  | S2    | Yes              |
| TS   | 23.218 | IP Multimedia (IM) session handling; IM call model; Stage 2                                                                          | C1    | Yes              |
| TS   | 23.221 | Architectural requirements                                                                                                           | S2    | Yes              |
| TS   | 23.226 | Global text telephony (GTT); Stage 2                                                                                                 | S2    | Yes              |
| TS   | 23.228 | IP Multimedia Subsystem (IMS); Stage 2                                                                                               | S2    | Yes              |
| TS   | 23.234 | 3GPP system to Wireless Local Area Network (WLAN) interworking; System description                                                   | S2    | Yes              |
| TS   | 23.236 | Intra-domain connection of Radio Access Network (RAN) nodes to multiple Core Network (CN) nodes                                      | S2    | Yes              |
| TS   | 23.237 | IP Multimedia Subsystem (IMS) Service Continuity; Stage 2                                                                            | S2    | Yes              |
| TS   | 23.240 | 3GPP Generic User Profile (GUP); Architecture (Stage 2)                                                                              | S2    | Yes              |
| TS   | 23.246 | Multimedia Broadcast/Multicast Service (MBMS); Architecture and functional description                                               | S2    | Yes              |
| TS   | 23.251 | Network sharing; Architecture and functional description                                                                             | S2    | Yes              |
| TS   | 23.259 | Personal Network Management (PNM); Procedures and information flows; Stage 2                                                         | C1    | Yes              |
| TS   | 23.271 | Functional stage 2 description of Location Services (LCS)                                                                            | S2    | Yes              |
| TS   | 23.272 | Circuit Switched (CS) fallback in Evolved Packet System (EPS); Stage 2                                                               | S2    | Yes              |
| TS   | 23.279 | Combining Circuit Switched (CS) and IP Multimedia Subsystem (IMS) services; Stage 2                                                  | S2    | Yes              |
| TS   | 23.292 | IP Multimedia Subsystem (IMS) centralized services; Stage 2                                                                          | S2    | Yes              |
| TS   | 23.327 | Mobility between 3GPP-Wireless Local Area Network (WLAN) interworking and 3GPP systems                                               | S2    | Yes              |
| TS   | 23.333 | Multimedia Resource Function Controller (MRFC) - Multimedia Resource Function Processor (MRFP) Mp interface: Procedures descriptions | C4    | Yes              |

| Type | Number | Title                                                                                                                               | Group | For publication? |
|------|--------|-------------------------------------------------------------------------------------------------------------------------------------|-------|------------------|
| TS   | 23.334 | IP Multimedia Subsystem (IMS) Application Level Gateway (IMS-ALG) – IMS Access Gateway (IMS-AGW) interface: Procedures descriptions | C4    | Yes              |
| TS   | 23.335 | User Data Convergence (UDC); Technical realization and information flows; Stage 2                                                   | C4    | Yes              |
| TS   | 23.380 | IMS Restoration Procedures                                                                                                          | C4    | Yes              |
| TS   | 23.401 | General Packet Radio Service (GPRS) enhancements for Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access            | S2    | Yes              |
| TS   | 23.402 | Architecture enhancements for non-3GPP accesses                                                                                     | S2    | Yes              |
| TR   | 23.820 | Study of IMS restoration procedures                                                                                                 | C4    | No               |
| TR   | 23.830 | Architecture aspects of Home Node B (HNB) / Home enhanced Node B (HeNB)                                                             | S2    | No               |
| TR   | 23.903 | Redial solution for voice-video switching                                                                                           | S2    | Yes              |
| TR   | 23.919 | Direct tunnel deployment guideline                                                                                                  | S2    | Yes              |
| TR   | 23.976 | Push architecture                                                                                                                   | S2    | Yes              |
| TR   | 23.979 | 3GPP enablers for Open Mobile Alliance (OMA); Push-to-talk over Cellular (PoC) services; Stage 2                                    | S2    | Yes              |
| TR   | 23.981 | Interworking aspects and migration scenarios for IPv4-based IP Multimedia Subsystem (IMS) implementations                           | S2    | Yes              |
| TS   | 24.007 | Mobile radio interface signalling layer 3; General Aspects                                                                          | C1    | Yes              |
| TS   | 24.008 | Mobile radio interface Layer 3 specification; Core network protocols; Stage 3                                                       | C1    | Yes              |
| TS   | 24.010 | Mobile radio interface layer 3; Supplementary services specification; General aspects                                               | C4    | Yes              |
| TS   | 24.011 | Point-to-Point (PP) Short Message Service (SMS) support on mobile radio interface                                                   | C1    | Yes              |
| TS   | 24.030 | Location Services (LCS); Supplementary service operations; Stage 3                                                                  | C4    | Yes              |
| TS   | 24.080 | Mobile radio interface layer 3 supplementary services specification; Formats and coding                                             | C4    | Yes              |
| TS   | 24.081 | Line Identification supplementary services; Stage 3                                                                                 | C4    | Yes              |
| TS   | 24.109 | Bootstrapping interface (Ub) and network application function interface (Ua); Protocol details                                      | C1    | Yes              |
| TS   | 24.135 | Multicall supplementary service; Stage 3                                                                                            | C4    | Yes              |
| TS   | 24.141 | Presence service using the IP Multimedia (IM) Core Network (CN) subsystem; Stage 3                                                  | C1    | Yes              |
| TS   | 24.147 | Conferencing using the IP Multimedia (IM) Core Network (CN) subsystem; Stage 3                                                      | C1    | Yes              |
| TS   | 24.166 | 3GPP IP Multimedia Subsystem (IMS) conferencing Management Object (MO)                                                              | C1    | Yes              |
| TS   | 24.167 | 3GPP IMS Management Object (MO); Stage 3                                                                                            | C1    | Yes              |
| TS   | 24.171 | Control Plane Location Services (LCS) procedures in the Evolved Packet System (EPS)                                                 | C4    | Yes              |
| TS   | 24.173 | IMS Multimedia telephony communication service and supplementary services; Stage 3                                                  | C1    | Yes              |
| TS   | 24.182 | IP Multimedia Subsystem (IMS) Customized Alerting Tones (CAT); Protocol specification                                               | C1    | Yes              |
| TS   | 24.216 | Communication Continuity Management Object (MO)                                                                                     | C1    | Yes              |
| TS   | 24.229 | IP multimedia call control protocol based on Session Initiation Protocol (SIP) and Session Description Protocol (SDP); Stage 3      | C1    | Yes              |
| TS   | 24.234 | 3GPP system to Wireless Local Area Network (WLAN) interworking; WLAN User Equipment (WLAN UE) to network protocols; Stage 3         | C1    | Yes              |
| TS   | 24.237 | IP Multimedia (IM) Core Network (CN) subsystem IP Multimedia Subsystem (IMS) service continuity; Stage 3                            | C1    | Yes              |
| TS   | 24.238 | Session Initiation Protocol (SIP) based user configuration; Stage 3                                                                 | C1    | Yes              |

| Type | Number | Title                                                                                                                                                                       | Group | For publication? |
|------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|------------------|
| TS   | 24.239 | Flexible Alerting (FA) using IP Multimedia (IM) Core Network (CN) subsystem; Protocol specification                                                                         | C1    | Yes              |
| TS   | 24.247 | Messaging service using the IP Multimedia (IM) Core Network (CN) subsystem; Stage 3                                                                                         | C1    | Yes              |
| TS   | 24.259 | Personal Network Management (PNM); Stage 3                                                                                                                                  | C1    | Yes              |
| TS   | 24.279 | Combining Circuit Switched (CS) and IP Multimedia Subsystem (IMS) services; Stage 3                                                                                         | C1    | Yes              |
| TS   | 24.285 | Allowed Closed Subscriber Group (CSG) list; Management Object (MO)                                                                                                          | C1    | Yes              |
| TS   | 24.286 | IP Multimedia (IM) Core Network (CN) subsystem Centralized Services (ICS); Management Object (MO)                                                                           | C1    | Yes              |
| TS   | 24.292 | IP Multimedia (IM) Core Network (CN) subsystem Centralized Services (ICS); Stage 3                                                                                          | C1    | Yes              |
| TS   | 24.294 | IP Multimedia Subsystem (IMS) Centralized Services (ICS) protocol via I1 interface                                                                                          | C1    | Yes              |
| TS   | 24.301 | Non-Access-Stratum (NAS) protocol for Evolved Packet System (EPS); Stage 3                                                                                                  | C1    | Yes              |
| TS   | 24.302 | Access to the 3GPP Evolved Packet Core (EPC) via non-3GPP access networks; Stage 3                                                                                          | C1    | Yes              |
| TS   | 24.303 | Mobility management based on Dual-Stack Mobile IPv6; Stage 3                                                                                                                | C1    | Yes              |
| TS   | 24.304 | Mobility management based on Mobile IPv4; User Equipment (UE) - foreign agent interface; Stage 3                                                                            | C1    | Yes              |
| TS   | 24.305 | Selective Disabling of 3GPP User Equipment Capabilities (SDOUE) Management Object (MO)                                                                                      | C1    | Yes              |
| TS   | 24.312 | Access Network Discovery and Selection Function (ANDSF) Management Object (MO)                                                                                              | C1    | Yes              |
| TS   | 24.323 | 3GPP IP Multimedia Subsystem (IMS) service level tracing Management Object (MO)                                                                                             | C1    | Yes              |
| TS   | 24.341 | Support of SMS over IP networks; Stage 3                                                                                                                                    | C1    | Yes              |
| TS   | 24.604 | Communication Diversion (CDIV) using IP Multimedia (IM) Core Network (CN) subsystem; Protocol specification                                                                 | C1    | Yes              |
| TS   | 24.605 | Conference (CONF) using IP Multimedia (IM) Core Network (CN) subsystem; Protocol specification                                                                              | C1    | Yes              |
| TS   | 24.606 | Message Waiting Indication (MWI) using IP Multimedia (IM) Core Network (CN) subsystem; Protocol specification                                                               | C1    | Yes              |
| TS   | 24.607 | Originating Identification Presentation (OIP) and Originating Identification Restriction (OIR) using IP Multimedia (IM) Core Network (CN) subsystem; Protocol specification | C1    | Yes              |
| TS   | 24.608 | Terminating Identification Presentation (TIP) and Terminating Identification Restriction (TIR) using IP Multimedia (IM) Core Network (CN) subsystem; Protocol specification | C1    | Yes              |
| TS   | 24.610 | Communication HOLD (HOLD) using IP Multimedia (IM) Core Network (CN) subsystem; Protocol specification                                                                      | C1    | Yes              |
| TS   | 24.611 | Anonymous Communication Rejection (ACR) and Communication Barring (CB) using IP Multimedia (IM) Core Network (CN) subsystem; Protocol specification                         | C1    | Yes              |
| TS   | 24.615 | Communication Waiting (CW) using IP Multimedia (IM) Core Network (CN) subsystem; Protocol Specification                                                                     | C1    | Yes              |
| TS   | 24.616 | Malicious Communication Identification (MCID) using IP Multimedia (IM) Core Network (CN) subsystem; Protocol specification                                                  | C1    | Yes              |
| TS   | 24.623 | Extensible Markup Language (XML) Configuration Access Protocol (XCAP) over the Ut interface for Manipulating Supplementary Services                                         | C1    | Yes              |
| TS   | 24.628 | Common Basic Communication procedures using IP Multimedia (IM) Core Network (CN) subsystem; Protocol specification                                                          | C1    | Yes              |
| TS   | 24.629 | Explicit Communication Transfer (ECT) using IP Multimedia (IM) Core Network (CN) subsystem; Protocol specification                                                          | C1    | Yes              |

| Type | Number | Title                                                                                                                                                                                   | Group | For publication? |
|------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|------------------|
| TS   | 24.642 | Completion of Communications to Busy Subscriber (CCBS) and Completion of Communications by No Reply (CCNR) using IP Multimedia (IM) Core Network (CN) subsystem; Protocol specification | C1    | Yes              |
| TS   | 24.647 | Advice Of Charge (AOC) using IP Multimedia (IM) Core Network (CN) subsystem                                                                                                             | C1    | Yes              |
| TS   | 24.654 | Closed User Group (CUG) using IP Multimedia (IM) Core Network (CN) subsystem, Protocol Specification                                                                                    | C1    | Yes              |
| TR   | 24.930 | Signalling flows for the session setup in the IP Multimedia core network Subsystem (IMS) based on Session Initiation Protocol (SIP) and Session Description Protocol (SDP); Stage 3     | C1    | Yes              |
| TR   | 25.913 | Requirements for Evolved UTRA (E-UTRA) and Evolved UTRAN (E-UTRAN)                                                                                                                      | RP    | Yes              |
| TS   | 26.071 | Mandatory speech CODEC speech processing functions; AMR speech Codec; General description                                                                                               | S4    | Yes              |
| TS   | 26.073 | ANSI-C code for the Adaptive Multi Rate (AMR) speech codec                                                                                                                              | S4    | Yes              |
| TS   | 26.074 | Mandatory speech codec speech processing functions; Adaptive Multi-Rate (AMR) speech codec test sequences                                                                               | S4    | Yes              |
| TS   | 26.077 | Minimum performance requirements for noise suppresser; Application to the Adaptive Multi-Rate (AMR) speech encoder                                                                      | S4    | Yes              |
| TS   | 26.090 | Mandatory Speech Codec speech processing functions; Adaptive Multi-Rate (AMR) speech codec; Transcoding functions                                                                       | S4    | Yes              |
| TS   | 26.091 | Mandatory Speech Codec speech processing functions; Adaptive Multi-Rate (AMR) speech codec; Error concealment of lost frames                                                            | S4    | Yes              |
| TS   | 26.092 | Mandatory speech codec speech processing functions; Adaptive Multi-Rate (AMR) speech codec; Comfort noise aspects                                                                       | S4    | Yes              |
| TS   | 26.093 | Mandatory speech codec speech processing functions Adaptive Multi-Rate (AMR) speech codec; Source controlled rate operation                                                             | S4    | Yes              |
| TS   | 26.094 | Mandatory speech codec speech processing functions; Adaptive Multi-Rate (AMR) speech codec; Voice Activity Detector (VAD)                                                               | S4    | Yes              |
| TS   | 26.101 | Mandatory speech codec speech processing functions; Adaptive Multi-Rate (AMR) speech codec frame structure                                                                              | S4    | Yes              |
| TS   | 26.102 | Mandatory speech codec; Adaptive Multi-Rate (AMR) speech codec; Interface to Iu, Uu and Nb                                                                                              | S4    | Yes              |
| TS   | 26.104 | ANSI-C code for the floating-point Adaptive Multi-Rate (AMR) speech codec                                                                                                               | S4    | Yes              |
| TS   | 26.114 | IP Multimedia Subsystem (IMS); Multimedia telephony; Media handling and interaction                                                                                                     | S4    | Yes              |
| TS   | 26.115 | Echo control for speech and multimedia services                                                                                                                                         | S4    | Yes              |
| TS   | 26.131 | Terminal acoustic characteristics for telephony; Requirements                                                                                                                           | S4    | Yes              |
| TS   | 26.132 | Speech and video telephony terminal acoustic test specification                                                                                                                         | S4    | Yes              |
| TS   | 26.140 | Multimedia Messaging Service (MMS); Media formats and codecs                                                                                                                            | S4    | Yes              |
| TS   | 26.141 | IP Multimedia System (IMS) Messaging and Presence; Media formats and codecs                                                                                                             | S4    | Yes              |
| TS   | 26.142 | Dynamic and Interactive Multimedia Scenes (DIMS)                                                                                                                                        | S4    | Yes              |
| TS   | 26.150 | Syndicated Feed Reception (SFR) within 3GPP environments; Protocols and codecs                                                                                                          | S4    | Yes              |
| TS   | 26.171 | Speech codec speech processing functions; Adaptive Multi-Rate - Wideband (AMR-WB) speech codec; General description                                                                     | S4    | Yes              |
| TS   | 26.173 | ANSI-C code for the Adaptive Multi-Rate - Wideband (AMR-WB) speech codec                                                                                                                | S4    | Yes              |
| TS   | 26.174 | Speech codec speech processing functions; Adaptive Multi-Rate - Wideband (AMR-WB) speech codec test sequences                                                                           | S4    | Yes              |
| TS   | 26.177 | Speech Enabled Services (SES); Distributed Speech Recognition (DSR) extended advanced front-end test sequences                                                                          | S4    | Yes              |
| TS   | 26.190 | Speech codec speech processing functions; Adaptive Multi-Rate - Wideband (AMR-WB) speech codec; Transcoding functions                                                                   | S4    | Yes              |

| Type | Number | Title                                                                                                                                               | Group | For publication? |
|------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------|-------|------------------|
| TS   | 26.191 | Speech codec speech processing functions; Adaptive Multi-Rate - Wideband (AMR-WB) speech codec; Error concealment of erroneous or lost frames       | S4    | Yes              |
| TS   | 26.192 | Speech codec speech processing functions; Adaptive Multi-Rate - Wideband (AMR-WB) speech codec; Comfort noise aspects                               | S4    | Yes              |
| TS   | 26.193 | Speech codec speech processing functions; Adaptive Multi-Rate - Wideband (AMR-WB) speech codec; Source controlled rate operation                    | S4    | Yes              |
| TS   | 26.194 | Speech codec speech processing functions; Adaptive Multi-Rate - Wideband (AMR-WB) speech codec; Voice Activity Detector (VAD)                       | S4    | Yes              |
| TS   | 26.201 | Speech codec speech processing functions; Adaptive Multi-Rate - Wideband (AMR-WB) speech codec; Frame structure                                     | S4    | Yes              |
| TS   | 26.202 | Speech codec speech processing functions; Adaptive Multi-Rate - Wideband (AMR-WB) speech codec; Interface to Iu, Uu and Nb                          | S4    | Yes              |
| TS   | 26.204 | Speech codec speech processing functions; Adaptive Multi-Rate - Wideband (AMR-WB) speech codec; ANSI-C code                                         | S4    | Yes              |
| TS   | 26.233 | Transparent end-to-end Packet-switched Streaming service (PSS); General description                                                                 | S4    | Yes              |
| TS   | 26.234 | Transparent end-to-end Packet-switched Streaming Service (PSS); Protocols and codecs                                                                | S4    | Yes              |
| TS   | 26.235 | Packet switched conversational multimedia applications; Default codecs                                                                              | S4    | Yes              |
| TS   | 26.236 | Packet switched conversational multimedia applications; Transport protocols                                                                         | S4    | Yes              |
| TS   | 26.237 | IP Multimedia Subsystem (IMS) based Packet Switch Streaming (PSS) and Multimedia Broadcast/Multicast Service (MBMS) User Service; Protocols         | S4    | Yes              |
| TS   | 26.243 | ANSI-C code for the fixed-point distributed speech recognition extended advanced front-end                                                          | S4    | Yes              |
| TS   | 26.244 | Transparent end-to-end packet switched streaming service (PSS); 3GPP file format (3GP)                                                              | S4    | Yes              |
| TS   | 26.245 | Transparent end-to-end Packet switched Streaming Service (PSS); Timed text format                                                                   | S4    | Yes              |
| TS   | 26.246 | Transparent end-to-end Packet-switched Streaming Service (PSS); 3GPP SMIL language profile                                                          | S4    | Yes              |
| TS   | 26.273 | ANSI-C code for the fixed-point Extended Adaptive Multi-Rate - Wideband (AMR-WB+) speech codec                                                      | S4    | Yes              |
| TS   | 26.274 | Audio codec processing functions; Extended Adaptive Multi-Rate - Wideband (AMR-WB+) speech codec; Conformance testing                               | S4    | Yes              |
| TS   | 26.290 | Audio codec processing functions; Extended Adaptive Multi-Rate - Wideband (AMR-WB+) codec; Transcoding functions                                    | S4    | Yes              |
| TS   | 26.304 | Extended Adaptive Multi-Rate - Wideband (AMR-WB+) codec; Floating-point ANSI-C code                                                                 | S4    | Yes              |
| TS   | 26.346 | Multimedia Broadcast/Multicast Service (MBMS); Protocols and codecs                                                                                 | S4    | Yes              |
| TS   | 26.401 | General audio codec audio processing functions; Enhanced aacPlus general audio codec; General description                                           | S4    | Yes              |
| TS   | 26.402 | General audio codec audio processing functions; Enhanced aacPlus general audio codec; Additional decoder tools                                      | S4    | Yes              |
| TS   | 26.403 | General audio codec audio processing functions; Enhanced aacPlus general audio codec; Encoder specification; Advanced Audio Coding (AAC) part       | S4    | Yes              |
| TS   | 26.404 | General audio codec audio processing functions; Enhanced aacPlus general audio codec; Enhanced aacPlus encoder Spectral Band Replication (SBR) part | S4    | Yes              |
| TS   | 26.405 | General audio codec audio processing functions; Enhanced aacPlus general audio codec; Encoder specification parametric stereo part                  | S4    | Yes              |
| TS   | 26.406 | General audio codec audio processing functions; Enhanced aacPlus general audio codec; Conformance testing                                           | S4    | Yes              |
| TS   | 26.410 | General audio codec audio processing functions; Enhanced aacPlus general audio codec; Floating-point ANSI-C code                                    | S4    | Yes              |

| Type | Number | Title                                                                                                                                                                                                                   | Group | For publication? |
|------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|------------------|
| TS   | 26.411 | General audio codec audio processing functions; Enhanced aacPlus general audio codec; Fixed-point ANSI-C code                                                                                                           | S4    | Yes              |
| TS   | 26.412 | Source code for 3GP file format                                                                                                                                                                                         | S4    | Yes              |
| TS   | 26.430 | Timed graphics                                                                                                                                                                                                          | S4    | Yes              |
| TR   | 26.902 | Video codec performance                                                                                                                                                                                                 | S4    | Yes              |
| TR   | 26.903 | Improved video support for Packet Switched Streaming (PSS) and Multimedia Broadcast/Multicast Service (MBMS) Services                                                                                                   | S4    | Yes              |
| TR   | 26.914 | Multimedia telephony over IP Multimedia Subsystem (IMS); Optimization opportunities                                                                                                                                     | S4    | Yes              |
| TR   | 26.935 | Packet Switched (PS) conversational multimedia applications; Performance characterisation of default codecs                                                                                                             | S4    | Yes              |
| TR   | 26.936 | Performance characterization of 3GPP audio codecs                                                                                                                                                                       | S4    | Yes              |
| TR   | 26.937 | Transparent end-to-end Packet-switched Streaming Service (PSS); Real-time Transport Protocol (RTP) usage model                                                                                                          | S4    | Yes              |
| TR   | 26.943 | Recognition performance evaluations of codecs for Speech Enabled Services (SES)                                                                                                                                         | S4    | Yes              |
| TR   | 26.946 | Multimedia Broadcast/Multicast Service (MBMS) user service guidelines                                                                                                                                                   | S4    | Yes              |
| TR   | 26.975 | Performance characterization of the Adaptive Multi-Rate (AMR) speech codec                                                                                                                                              | S4    | Yes              |
| TR   | 26.976 | Performance characterization of the Adaptive Multi-Rate Wideband (AMR-WB) speech codec                                                                                                                                  | S4    | Yes              |
| TR   | 26.978 | Results of the Adaptive Multi-Rate (AMR) noise suppression selection phase                                                                                                                                              | S4    | Yes              |
| TS   | 27.001 | General on Terminal Adaptation Functions (TAF) for Mobile Stations (MS)                                                                                                                                                 | C3    | Yes              |
| TS   | 27.002 | Terminal Adaptation Functions (TAF) for services using asynchronous bearer capabilities                                                                                                                                 | C3    | Yes              |
| TS   | 27.003 | Terminal Adaptation Functions (TAF) for services using synchronous bearer capabilities                                                                                                                                  | C3    | Yes              |
| TS   | 27.005 | Use of Data Terminal Equipment - Data Circuit terminating Equipment (DTE - DCE) interface for Short Message Service (SMS) and Cell Broadcast Service (CBS)                                                              | C1    | Yes              |
| TS   | 27.007 | AT command set for User Equipment (UE)                                                                                                                                                                                  | C1    | Yes              |
| TS   | 27.010 | Terminal Equipment to User Equipment (TE-UE) multiplexer protocol                                                                                                                                                       | C3    | Yes              |
| TS   | 27.060 | Packet domain; Mobile Station (MS) supporting Packet Switched services                                                                                                                                                  | C3    | Yes              |
| TS   | 29.010 | Information element mapping between Mobile Station - Base Station System (MS - BSS) and Base Station System - Mobile-services Switching Centre (BSS - MSC); Signalling Procedures and the Mobile Application Part (MAP) | C4    | Yes              |
| TS   | 29.061 | Interworking between the Public Land Mobile Network (PLMN) supporting packet based services and Packet Data Networks (PDN)                                                                                              | C3    | Yes              |
| TS   | 29.108 | Application of the Radio Access Network Application Part (RANAP) on the E-interface                                                                                                                                     | R3    | Yes              |
| TS   | 29.109 | Generic Authentication Architecture (GAA); Zh and Zn Interfaces based on the Diameter protocol; Stage 3                                                                                                                 | C4    | Yes              |
| TS   | 29.118 | Mobility Management Entity (MME) - Visitor Location Register (VLR) SGs interface specification                                                                                                                          | C1    | Yes              |
| TS   | 29.161 | Interworking between the Public Land Mobile Network (PLMN) supporting packet based services with Wireless Local Area Network (WLAN) access and Packet data Networks (PDN)                                               | C3    | Yes              |
| TS   | 29.162 | Interworking between the IM CN subsystem and IP networks                                                                                                                                                                | C3    | Yes              |
| TS   | 29.163 | Interworking between the IP Multimedia (IM) Core Network (CN) subsystem and Circuit Switched (CS) networks                                                                                                              | C3    | Yes              |
| TS   | 29.165 | Inter-IMS Network to Network Interface (NNI)                                                                                                                                                                            | C3    | Yes              |
| TS   | 29.168 | Cell Broadcast Centre interfaces with the Evolved Packet Core; Stage 3                                                                                                                                                  | C4    | Yes              |

| Type | Number      | Title                                                                                                                                                                         | Group | For publication? |
|------|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|------------------|
| TS   | 29.171      | Location Services (LCS); LCS Application Protocol (LCS-AP) between the Mobile Management Entity (MME) and Evolved Serving Mobile Location Centre (E-SMLC); SLs interface      | C4    | Yes              |
| TS   | 29.172      | Location Services (LCS); Evolved Packet Core (EPC) LCS Protocol (ELP) between the Gateway Mobile Location Centre (GMLC) and the Mobile Management Entity (MME); SLg interface | C4    | Yes              |
| TS   | 29.173      | Location Services (LCS); Diameter-based SLh interface for Control Plane LCS                                                                                                   | C4    | Yes              |
| TS   | 29.198-01   | Open Service Access (OSA) Application Programming Interface (API); Part 1: Overview                                                                                           | CP    | Yes              |
| TS   | 29.198-02   | Open Service Access (OSA) Application Programming Interface (API); Part 2: Common data definitions                                                                            | CP    | Yes              |
| TS   | 29.198-03   | Open Service Access (OSA) Application Programming Interface (API); Part 3: Framework                                                                                          | CP    | Yes              |
| TS   | 29.198-04-1 | Open Service Access (OSA) Application Programming Interface (API); Part 4: Call control; Subpart 1: Call control common definitions                                           | CP    | Yes              |
| TS   | 29.198-04-2 | Open Service Access (OSA) Application Programming Interface (API); Part 4: Call control; Subpart 2: Generic call control Service Capability Feature (SCF)                     | CP    | Yes              |
| TS   | 29.198-04-3 | Open Service Access (OSA) Application Programming Interface (API); Part 4: Call control; Subpart 3: Multi-party call control Service Capability Feature (SCF)                 | CP    | Yes              |
| TS   | 29.198-04-4 | Open Service Access (OSA) Application Programming Interface (API); Part 4: Call control; Subpart 4: Multimedia call control Service Capability Feature (SCF)                  | CP    | Yes              |
| TS   | 29.198-04-5 | Open Service Access (OSA) Application Programming Interface (API); Part 4: Call control; Subpart 5: Conference call control Service Capability Feature (SCF)                  | CP    | Yes              |
| TS   | 29.198-05   | Open Service Access (OSA) Application Programming Interface (API); Part 5: User interaction Service Capability Feature (SCF)                                                  | CP    | Yes              |
| TS   | 29.198-06   | Open Service Access (OSA) Application Programming Interface (API); Part 6: Mobility Service Capability Feature (SCF)                                                          | CP    | Yes              |
| TS   | 29.198-07   | Open Service Access (OSA) Application Programming Interface (API); Part 7: Terminal capabilities Service Capability Feature (SCF)                                             | CP    | Yes              |
| TS   | 29.198-08   | Open Service Access (OSA) Application Programming Interface (API); Part 8: Data session control Service Capability Feature (SCF)                                              | CP    | Yes              |
| TS   | 29.198-10   | Open Service Access (OSA) Application Programming Interface (API); Part 10: Connectivity manager Service Capability Feature (SCF)                                             | CP    | Yes              |
| TS   | 29.198-11   | Open Service Access (OSA) Application Programming Interface (API); Part 11: Account management Service Capability Feature (SCF)                                               | CP    | Yes              |
| TS   | 29.198-12   | Open Service Access (OSA) Application Programming Interface (API); Part 12: Charging Service Capability Feature (SCF)                                                         | CP    | Yes              |
| TS   | 29.198-13   | Open Service Access (OSA) Application Programming Interface (API); Part 13: Policy management Service Capability Feature (SCF)                                                | CP    | Yes              |
| TS   | 29.198-14   | Open Service Access (OSA) Application Programming Interface (API); Part 14: Presence and Availability Management (PAM) Service Capability Feature (SCF)                       | CP    | Yes              |
| TS   | 29.198-15   | Open Service Access (OSA) Application Programming Interface (API); Part 15: Multi-media Messaging (MM) Service Capability Feature (SCF)                                       | CP    | Yes              |
| TS   | 29.198-16   | Open Service Access (OSA) Application Programming Interface (API); Part 16: Service broker Service Capability Feature (SCF)                                                   | CP    | Yes              |
| TS   | 29.199-01   | Open Service Access (OSA); Parlay X web services; Part 1: Common                                                                                                              | CP    | Yes              |
| TS   | 29.199-02   | Open Service Access (OSA); Parlay X web services; Part 2: Third party call                                                                                                    | CP    | Yes              |
| TS   | 29.199-03   | Open Service Access (OSA); Parlay X web services; Part 3: Call notification                                                                                                   | CP    | Yes              |
| TS   | 29.199-04   | Open Service Access (OSA); Parlay X web services; Part 4: Short messaging                                                                                                     | CP    | Yes              |

| Type | Number    | Title                                                                                                     | Group | For publication? |
|------|-----------|-----------------------------------------------------------------------------------------------------------|-------|------------------|
| TS   | 29.199-05 | Open Service Access (OSA); Parlay X web services; Part 5: Multimedia messaging                            | CP    | Yes              |
| TS   | 29.199-06 | Open Service Access (OSA); Parlay X web services; Part 6: Payment                                         | CP    | Yes              |
| TS   | 29.199-07 | Open Service Access (OSA); Parlay X web services; Part 7: Account management                              | CP    | Yes              |
| TS   | 29.199-08 | Open Service Access (OSA); Parlay X web services; Part 8: Terminal status                                 | CP    | Yes              |
| TS   | 29.199-09 | Open Service Access (OSA); Parlay X web services; Part 9: Terminal location                               | CP    | Yes              |
| TS   | 29.199-10 | Open Service Access (OSA); Parlay X web services; Part 10: Call handling                                  | CP    | Yes              |
| TS   | 29.199-11 | Open Service Access (OSA); Parlay X web services; Part 11: Audio call                                     | CP    | Yes              |
| TS   | 29.199-12 | Open Service Access (OSA); Parlay X web services; Part 12: Multimedia conference                          | CP    | Yes              |
| TS   | 29.199-13 | Open Service Access (OSA); Parlay X web services; Part 13: Address list management                        | CP    | Yes              |
| TS   | 29.199-14 | Open Service Access (OSA); Parlay X web services; Part 14: Presence                                       | CP    | Yes              |
| TS   | 29.199-15 | Open Service Access (OSA); Parlay X web services; Part 15: Message broadcast                              | CP    | Yes              |
| TS   | 29.199-16 | Open Service Access (OSA); Parlay X web services; Part 16: Geocoding                                      | CP    | Yes              |
| TS   | 29.199-17 | Open Service Access (OSA); Parlay X web services; Part 17: Application-driven Quality of Service (QoS)    | CP    | Yes              |
| TS   | 29.199-18 | Open Service Access (OSA); Parlay X web services; Part 18: Device capabilities and configuration          | CP    | Yes              |
| TS   | 29.199-19 | Open Service Access (OSA); Parlay X web services; Part 19: Multimedia streaming control                   | CP    | Yes              |
| TS   | 29.199-20 | Open Service Access (OSA); Parlay X web services; Part 20: Multimedia multicast session management        | CP    | Yes              |
| TS   | 29.199-21 | Open Service Access (OSA); Parlay X web services; Part 21: Content management                             | CP    | Yes              |
| TS   | 29.199-22 | Open Service Access (OSA); Parlay X web services; Part 22: Policy                                         | CP    | Yes              |
| TS   | 29.202    | Signalling System No. 7 (SS7) signalling transport in core network; Stage 3                               | C4    | Yes              |
| TS   | 29.204    | Signalling System No. 7 (SS7) security gateway; Architecture, functional description and protocol details | C4    | Yes              |
| TS   | 29.212    | Policy and Charging Control (PCC) over Gx/Sd reference point                                              | C3    | Yes              |
| TS   | 29.213    | Policy and charging control signalling flows and Quality of Service (QoS) parameter mapping               | C3    | Yes              |
| TS   | 29.214    | Policy and charging control over Rx reference point                                                       | C3    | Yes              |
| TS   | 29.215    | Policy and Charging Control (PCC) over S9 reference point; Stage 3                                        | C3    | Yes              |
| TS   | 29.228    | IP Multimedia (IM) Subsystem Cx and Dx Interfaces; Signalling flows and message contents                  | C4    | Yes              |
| TS   | 29.229    | Cx and Dx interfaces based on the Diameter protocol; Protocol details                                     | C4    | Yes              |
| TS   | 29.230    | Diameter applications; 3GPP specific codes and identifiers                                                | C4    | Yes              |
| TS   | 29.231    | Application of SIP-I Protocols to Circuit Switched (CS) core network architecture; Stage 3                | C4    | Yes              |
| TS   | 29.232    | Media Gateway Controller (MGC) - Media Gateway (MGW) interface; Stage 3                                   | C4    | Yes              |
| TS   | 29.234    | 3GPP system to Wireless Local Area Network (WLAN) interworking; Stage 3                                   | C4    | Yes              |

| Type | Number      | Title                                                                                                                                                                            | Group | For publication? |
|------|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|------------------|
| TS   | 29.235      | Interworking between SIP-I based circuit-switched core network and other networks                                                                                                | C3    | Yes              |
| TS   | 29.238      | Interconnection Border Control Functions (IBCF) - Transition Gateway (TrGW) interface, Ix interface; Stage 3                                                                     | C4    | Yes              |
| TS   | 29.240      | 3GPP Generic User Profile (GUP); Stage 3; Network                                                                                                                                | C4    | Yes              |
| TS   | 29.272      | Evolved Packet System (EPS); Mobility Management Entity (MME) and Serving GPRS Support Node (SGSN) related interfaces based on Diameter protocol                                 | C4    | Yes              |
| TS   | 29.273      | Evolved Packet System (EPS); 3GPP EPS AAA interfaces                                                                                                                             | C4    | Yes              |
| TS   | 29.274      | 3GPP Evolved Packet System (EPS); Evolved General Packet Radio Service (GPRS) Tunnelling Protocol for Control plane (GTPv2-C); Stage 3                                           | C4    | Yes              |
| TS   | 29.275      | Proxy Mobile IPv6 (PMIPv6) based Mobility and Tunnelling protocols; Stage 3                                                                                                      | C4    | Yes              |
| TS   | 29.276      | 3GPP Evolved Packet System (EPS); Optimized handover procedures and protocols between E-UTRAN access and cdma2000 HRPD Access; Stage 3                                           | C4    | Yes              |
| TS   | 29.277      | Optimised handover procedures and protocol between EUTRAN access and non-3GPP accesses (S102); Stage 3                                                                           | C4    | Yes              |
| TS   | 29.279      | Mobile IPv4 (MIPv4) based mobility protocols; Stage 3                                                                                                                            | C4    | Yes              |
| TS   | 29.280      | Evolved Packet System (EPS); 3GPP Sv interface (MME to MSC, and SGSN to MSC) for SRVCC                                                                                           | C4    | Yes              |
| TS   | 29.281      | General Packet Radio System (GPRS) Tunnelling Protocol User Plane (GTPv1-U)                                                                                                      | C4    | Yes              |
| TS   | 29.282      | Mobile IPv6 vendor specific option format and usage within 3GPP                                                                                                                  | C4    | Yes              |
| TS   | 29.292      | Interworking between the IP Multimedia (IM) Core Network (CN) subsystem (IMS) and MSC Server for IMS Centralized Services (ICS)                                                  | C3    | Yes              |
| TS   | 29.303      | Domain Name System Procedures; Stage 3                                                                                                                                           | C4    | Yes              |
| TS   | 29.305      | InterWorking Function (IWF) between MAP based and Diameter based interfaces                                                                                                      | C4    | Yes              |
| TS   | 29.311      | Service level interworking for Messaging Services                                                                                                                                | C3    | Yes              |
| TS   | 29.328      | IP Multimedia (IM) Subsystem Sh interface; Signalling flows and message contents                                                                                                 | C4    | Yes              |
| TS   | 29.329      | Sh interface based on the Diameter protocol; Protocol details                                                                                                                    | C4    | Yes              |
| TS   | 29.332      | Media Gateway Control Function (MGCF) - IM Media Gateway; Mn interface                                                                                                           | C4    | Yes              |
| TS   | 29.333      | Multimedia Resource Function Controller (MRFC) - Multimedia Resource Function Processor (MRFP) Mp interface; Stage 3                                                             | C4    | Yes              |
| TS   | 29.334      | IMS Application Level Gateway (IMS-ALG) - IMS Access Gateway (IMS-AGW); Iq Interface; Stage 3                                                                                    | C4    | Yes              |
| TS   | 29.335      | User Data Convergence (UDC); User data repository access protocol over the Ud interface; Stage 3                                                                                 | C4    | Yes              |
| TS   | 29.364      | IP Multimedia Subsystem (IMS) Application Server (AS) service data descriptions for AS interoperability                                                                          | C4    | Yes              |
| TS   | 29.414      | Core network Nb data transport and transport signalling                                                                                                                          | C3    | Yes              |
| TS   | 29.415      | Core network Nb interface user plane protocols                                                                                                                                   | C3    | Yes              |
| TS   | 29.658      | SIP Transfer of IP Multimedia Service Tariff Information; Protocol specification                                                                                                 | C3    | Yes              |
| TR   | 29.909      | Diameter-based protocols usage and recommendations in 3GPP                                                                                                                       | C3    | Yes              |
| TR   | 29.994      | Recommended infrastructure measures to overcome specific Mobile Station (MS) and User Equipment (UE) faults                                                                      | C1    | Yes              |
| TR   | 29.998-01   | Open Service Access (OSA); Application Programming Interface (API) mapping for OSA; Part 1: General issues on API mapping                                                        | CP    | Yes              |
| TR   | 29.998-04-1 | Open Service Access (OSA); Application Programming Interface (API) Mapping for Open Service Access; Part 4: Call Control Service Mapping; Subpart 1: API to CAP Mapping          | CP    | Yes              |
| TR   | 29.998-04-4 | Open Service Access (OSA); Application Programming Interface (API) Mapping for Open Service Access; Part 4: Call Control Service Mapping; Subpart 4: Multiparty Call Control ISC | CP    | Yes              |

| Type | Number      | Title                                                                                                                                                                                                            | Group | For publication? |
|------|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|------------------|
| TR   | 29.998-05-1 | Open Service Access (OSA); Application Programming Interface (API) Mapping for Open Service Access; Part 5: User Interaction Service Mapping; Subpart 1: API to CAP Mapping                                      | CP    | Yes              |
| TR   | 29.998-05-4 | Open Service Access (OSA); Application Programming Interface (API) Mapping for Open Service Access; Part 5: User Interaction Service Mapping; Subpart 4: API to SMS Mapping                                      | CP    | Yes              |
| TR   | 29.998-06-1 | Open Service Access (OSA); Application Programming Interface (API) Mapping for Open Service Access; Part 6: User location - user status service mapping; Subpart 1: Mapping to Mobile Application Part (MAP)     | CP    | Yes              |
| TR   | 29.998-06-2 | Open Service Access (OSA); Application Programming Interface (API) Mapping for Open Service Access; Part 6: User location - user status service mapping; Subpart 2: Mapping to Session Initiation Protocol (SIP) | CP    | Yes              |
| TR   | 29.998-08   | Open Service Access (OSA); Application Programming Interface (API) Mapping for Open Service Access; Part 8: Data Session Control Service Mapping to CAP                                                          | CP    | Yes              |
| TS   | 31.101      | UICC-terminal interface; Physical and logical characteristics                                                                                                                                                    | C6    | Yes              |
| TS   | 31.102      | Characteristics of the Universal Subscriber Identity Module (USIM) application                                                                                                                                   | C6    | Yes              |
| TS   | 31.103      | Characteristics of the IP Multimedia Services Identity Module (ISIM) application                                                                                                                                 | C6    | Yes              |
| TS   | 31.111      | Universal Subscriber Identity Module (USIM) Application Toolkit (USAT)                                                                                                                                           | C6    | Yes              |
| TS   | 31.115      | Remote APDU Structure for (U)SIM Toolkit applications                                                                                                                                                            | C6    | Yes              |
| TS   | 31.116      | Remote APDU Structure for (U)SIM Toolkit applications                                                                                                                                                            | C6    | Yes              |
| TS   | 31.120      | UICC-terminal interface; Physical, electrical and logical test specification                                                                                                                                     | C6    | Yes              |
| TS   | 31.121      | UICC-terminal interface; Universal Subscriber Identity Module (USIM) application test specification                                                                                                              | C6    | Yes              |
| TS   | 31.122      | Universal Subscriber Identity Module (USIM) conformance test specification                                                                                                                                       | C6    | Yes              |
| TS   | 31.124      | Mobile Equipment (ME) conformance test specification; Universal Subscriber Identity Module Application Toolkit (USAT) conformance test specification                                                             | C6    | Yes              |
| TS   | 31.130      | (U)SIM Application Programming Interface (API); (U)SIM API for Java™ Card                                                                                                                                        | C6    | Yes              |
| TS   | 31.131      | C-language binding to (U)SIM API                                                                                                                                                                                 | C6    | Yes              |
| TS   | 31.133      | IP Multimedia Services Identity Module (ISIM) Application Programming Interface (API); ISIM API for Java Card™                                                                                                   | C6    | Yes              |
| TS   | 31.213      | Test specification for (U)SIM; Application Programming Interface (API) for Java Card™                                                                                                                            | C6    | Yes              |
| TS   | 31.220      | Characteristics of the Contact Manager for 3GPP UICC applications                                                                                                                                                | C6    | Yes              |
| TS   | 31.221      | Contact Manager Application Programming Interface (API); Contact Manager API for Java Card                                                                                                                       | C6    | Yes              |
| TR   | 31.900      | SIM/USIM internal and external interworking aspects                                                                                                                                                              | C6    | Yes              |
| TS   | 32.101      | Telecommunication management; Principles and high level requirements                                                                                                                                             | S5    | Yes              |
| TS   | 32.102      | Telecommunication management; Architecture                                                                                                                                                                       | S5    | Yes              |
| TS   | 32.111-1    | Telecommunication management; Fault Management; Part 1: 3G fault management requirements                                                                                                                         | S5    | Yes              |
| TS   | 32.111-2    | Telecommunication management; Fault Management; Part 2: Alarm Integration Reference Point (IRP): Information Service (IS)                                                                                        | S5    | Yes              |
| TS   | 32.111-3    | Telecommunication management; Fault Management; Part 3: Alarm Integration Reference Point (IRP): Common Object Request Broker Architecture (CORBA) Solution Set (SS)                                             | S5    | Yes              |
| TS   | 32.111-5    | Telecommunication management; Fault Management; Part 5: Alarm Integration Reference Point (IRP): eXtensible Markup Language (XML) definitions                                                                    | S5    | Yes              |
| TS   | 32.111-7    | Telecommunication management; Fault Management; Part 7: Alarm IRP SOAP Solution Set (SS)                                                                                                                         | S5    | Yes              |
| TS   | 32.121      | Telecommunication management; Advanced Alarm Management (AAM) Integration Reference Point (IRP): Requirements                                                                                                    | S5    | Yes              |

| Type | Number | Title                                                                                                                                                                   | Group | For publication? |
|------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|------------------|
| TS   | 32.122 | Telecommunication management; Advanced Alarm Management (AAM) Integration Reference Point (IRP): Information Service (IS)                                               | S5    | Yes              |
| TS   | 32.123 | Telecommunication management; Advanced Alarm Management (AAM) Integration Reference Point (IRP); Common Object Request Broker Architecture (CORBA) Solution Set (SS)    | S5    | Yes              |
| TS   | 32.125 | Telecommunication management; Advanced Alarm Management (AAM) Integration Reference Point (IRP): eXtensible Markup Language (XML) file format definition                | S5    | Yes              |
| TS   | 32.140 | Telecommunication management; Subscription Management (SuM) requirements                                                                                                | S5    | Yes              |
| TS   | 32.141 | Telecommunication management; Subscription Management (SuM) architecture                                                                                                | S5    | Yes              |
| TS   | 32.150 | Telecommunication management; Integration Reference Point (IRP) Concept and definitions                                                                                 | S5    | Yes              |
| TS   | 32.151 | Telecommunication management; Integration Reference Point (IRP) Information Service (IS) template                                                                       | S5    | Yes              |
| TS   | 32.152 | Telecommunication management; Integration Reference Point (IRP) Information Service (IS) Unified Modelling Language (UML) repertoire                                    | S5    | Yes              |
| TS   | 32.153 | Telecommunication management; Integration Reference Point (IRP) technology specific templates, rules and guidelines                                                     | S5    | Yes              |
| TS   | 32.154 | Telecommunication management; Backward and Forward Compatibility (BFC); Concept and definitions                                                                         | S5    | Yes              |
| TS   | 32.155 | Telecommunication management; Requirements template                                                                                                                     | S5    | Yes              |
| TS   | 32.171 | Telecommunication management; Subscription Management (SuM) Network Resource Model (NRM) Integration Reference Point (IRP); Requirements                                | S5    | Yes              |
| TS   | 32.172 | Telecommunication management; Subscription Management (SuM) Network Resource Model (NRM) Integration Reference Point (IRP): Information Service (IS)                    | S5    | Yes              |
| TS   | 32.175 | Telecommunication management; Subscription Management (SuM) Network Resource Model (NRM) Integration Reference Point (IRP): eXtensible Markup Language (XML) definition | S5    | Yes              |
| TS   | 32.240 | Telecommunication management; Charging management; Charging architecture and principles                                                                                 | S5    | Yes              |
| TS   | 32.251 | Telecommunication management; Charging management; Packet Switched (PS) domain charging                                                                                 | S5    | Yes              |
| TS   | 32.252 | Telecommunication management; Charging management; Wireless Local Area Network (WLAN) charging                                                                          | S5    | Yes              |
| TS   | 32.260 | Telecommunication management; Charging management; IP Multimedia Subsystem (IMS) charging                                                                               | S5    | Yes              |
| TS   | 32.270 | Telecommunication management; Charging management; Multimedia Messaging Service (MMS) charging                                                                          | S5    | Yes              |
| TS   | 32.271 | Telecommunication management; Charging management; Location Services (LCS) charging                                                                                     | S5    | Yes              |
| TS   | 32.272 | Telecommunication management; Charging management; Push-to-talk over Cellular (PoC) charging                                                                            | S5    | Yes              |
| TS   | 32.273 | Telecommunication management; Charging management; Multimedia Broadcast and Multicast Service (MBMS) charging                                                           | S5    | Yes              |
| TS   | 32.274 | Telecommunication management; Charging management; Short Message Service (SMS) charging                                                                                 | S5    | Yes              |
| TS   | 32.275 | Telecommunication management; Charging management; MultiMedia Telephony (MMTel) charging                                                                                | S5    | Yes              |
| TS   | 32.280 | Telecommunication management; Charging management; Advice of Charge (AoC) service                                                                                       | S5    | Yes              |
| TS   | 32.295 | Telecommunication management; Charging management; Charging Data Record (CDR) transfer                                                                                  | S5    | Yes              |

| Type | Number | Title                                                                                                                                                                            | Group | For publication? |
|------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|------------------|
| TS   | 32.296 | Telecommunication management; Charging management; Online Charging System (OCS): Applications and interfaces                                                                     | S5    | Yes              |
| TS   | 32.297 | Telecommunication management; Charging management; Charging Data Record (CDR) file format and transfer                                                                           | S5    | Yes              |
| TS   | 32.299 | Telecommunication management; Charging management; Diameter charging applications                                                                                                | S5    | Yes              |
| TS   | 32.300 | Telecommunication management; Configuration Management (CM); Name convention for Managed Objects                                                                                 | S5    | Yes              |
| TS   | 32.301 | Telecommunication management; Configuration Management (CM); Notification Integration Reference Point (IRP); Requirements                                                        | S5    | Yes              |
| TS   | 32.302 | Telecommunication management; Configuration Management (CM); Notification Integration Reference Point (IRP); Information Service (IS)                                            | S5    | Yes              |
| TS   | 32.303 | Telecommunication management; Configuration Management (CM); Notification Integration Reference Point (IRP); Common Object Request Broker Architecture (CORBA) Solution Set (SS) | S5    | Yes              |
| TS   | 32.305 | Telecommunication management; Configuration Management (CM); Notification Integration Reference Point (IRP); eXtensible Markup Language (XML) definition                         | S5    | Yes              |
| TS   | 32.307 | Telecommunication management; Configuration Management (CM); Notification Integration Reference Point (IRP); SOAP Solution Set (SS)                                              | S5    | Yes              |
| TS   | 32.311 | Telecommunication management; Generic Integration Reference Point (IRP) management; Requirements                                                                                 | S5    | Yes              |
| TS   | 32.312 | Telecommunication management; Generic Integration Reference Point (IRP) management; Information Service (IS)                                                                     | S5    | Yes              |
| TS   | 32.313 | Telecommunication management; Generic Integration Reference Point (IRP) management; Common Object Request Broker Architecture (CORBA) Solution Set (SS)                          | S5    | Yes              |
| TS   | 32.317 | Telecommunication management; Generic Integration Reference Point (IRP) management; SOAP Solution Set (SS)                                                                       | S5    | Yes              |
| TS   | 32.321 | Telecommunication management; Test management Integration Reference Point (IRP); Requirements                                                                                    | S5    | Yes              |
| TS   | 32.322 | Telecommunication management; Test management Integration Reference Point (IRP); Information Service (IS)                                                                        | S5    | Yes              |
| TS   | 32.323 | Telecommunication management; Test management Integration Reference Point (IRP); Common Object Request Broker Architecture (CORBA) Solution Set (SS)                             | S5    | Yes              |
| TS   | 32.325 | Telecommunication management; Test management Integration Reference Point (IRP); eXtensible Markup Language (XML) definitions                                                    | S5    | Yes              |
| TS   | 32.331 | Telecommunication management; Notification Log (NL) Integration Reference Point (IRP); Requirements                                                                              | S5    | Yes              |
| TS   | 32.332 | Telecommunication management; Notification Log (NL) Integration Reference Point (IRP); Information Service (IS)                                                                  | S5    | Yes              |
| TS   | 32.333 | Telecommunication management; Notification Log (NL) Integration Reference Point (IRP); Common Object Request Broker Architecture (CORBA) Solution Set (SS)                       | S5    | Yes              |
| TS   | 32.335 | Telecommunication management; Notification Log (NL) Integration Reference Point (IRP); eXtensible Markup Language (XML) solution definitions                                     | S5    | Yes              |
| TS   | 32.337 | Telecommunication management; Notification Log (NL) Integration Reference Point (IRP); SOAP Solution Set (SS)                                                                    | S5    | Yes              |
| TS   | 32.341 | Telecommunication management; File Transfer (FT) Integration Reference Point (IRP); Requirements                                                                                 | S5    | Yes              |
| TS   | 32.342 | Telecommunication management; File Transfer (FT) Integration Reference Point (IRP); Information Service (IS)                                                                     | S5    | Yes              |
| TS   | 32.343 | Telecommunication management; File Transfer (FT) Integration Reference Point (IRP); Common Object Request Broker Architecture (CORBA) Solution Set (SS)                          | S5    | Yes              |
| TS   | 32.345 | Telecommunication management; File Transfer (FT) Integration Reference Point (IRP); eXtensible Markup Language (XML) definitions                                                 | S5    | Yes              |

| Type | Number | Title                                                                                                                                                                | Group | For publication? |
|------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|------------------|
| TS   | 32.347 | Telecommunication management; File Transfer (FT) Integration Reference Point (IRP); SOAP Solution Set (SS)                                                           | S5    | Yes              |
| TS   | 32.351 | Telecommunication management; Communication Surveillance (CS) Integration Reference Point (IRP); Requirements                                                        | S5    | Yes              |
| TS   | 32.352 | Telecommunication management; Communication Surveillance (CS) Integration Reference Point (IRP); Information Service (IS)                                            | S5    | Yes              |
| TS   | 32.353 | Telecommunication management; Communication Surveillance (CS) Integration Reference Point (IRP); Common Object Request Broker Architecture (CORBA) Solution Set (SS) | S5    | Yes              |
| TS   | 32.361 | Telecommunication management; Entry Point (EP) Integration Reference Point (IRP); Requirements                                                                       | S5    | Yes              |
| TS   | 32.362 | Telecommunication management; Entry Point (EP) Integration Reference Point (IRP); Information Service (IS)                                                           | S5    | Yes              |
| TS   | 32.363 | Telecommunication management; Entry Point (EP) Integration Reference Point (IRP); Common Object Request Broker Architecture (CORBA) Solution Set (SS)                | S5    | Yes              |
| TS   | 32.365 | Telecommunication management; Entry Point (EP) Integration Reference Point (IRP); eXtensible Markup Language (XML) definitions                                       | S5    | Yes              |
| TS   | 32.367 | Telecommunication management; Entry Point (EP) Integration Reference Point (IRP); SOAP Solution Set (SS)                                                             | S5    | Yes              |
| TS   | 32.371 | Telecommunication management; Security Management concept and requirements                                                                                           | S5    | Yes              |
| TS   | 32.372 | Telecommunication management; Security services for Integration Reference Point (IRP); Information Service (IS)                                                      | S5    | Yes              |
| TS   | 32.373 | Telecommunication management; Security services for Integration Reference Point (IRP); Common Object Request Broker Architecture (CORBA) solution                    | S5    | Yes              |
| TS   | 32.375 | Telecommunication management; Security services for Integration Reference Point (IRP); File integrity solution                                                       | S5    | Yes              |
| TS   | 32.381 | Telecommunication management; Partial Suspension of Itf-N Integration Reference Point (IRP); Requirements                                                            | S5    | Yes              |
| TS   | 32.382 | Telecommunication management; Partial Suspension of Itf-N Integration Reference Point (IRP); Information Service (IS)                                                | S5    | Yes              |
| TS   | 32.383 | Telecommunication management; Partial Suspension of Itf-N Integration Reference Point (IRP); Common Object Request Broker Architecture (CORBA) Solution Set (SS)     | S5    | Yes              |
| TS   | 32.385 | Telecommunication management; Partial Suspension of Itf-N Integration Reference Point (IRP); eXtensible Markup Language (XML) file format definition                 | S5    | Yes              |
| TS   | 32.391 | Telecommunication management; Delta synchronization Integration Reference Point (IRP); Requirements                                                                  | S5    | Yes              |
| TS   | 32.392 | Telecommunication management; Delta synchronization Integration Reference Point (IRP); Information Service (IS)                                                      | S5    | Yes              |
| TS   | 32.393 | Telecommunication management; Delta synchronization Integration Reference Point (IRP); Common Object Request Broker Architecture (CORBA) Solution Set (SS)           | S5    | Yes              |
| TS   | 32.395 | Telecommunication management; Delta synchronisation Integration Reference Point (IRP); eXtensible Markup Language (XML) file format definition                       | S5    | Yes              |
| TS   | 32.401 | Telecommunication management; Performance Management (PM); Concept and requirements                                                                                  | S5    | Yes              |
| TS   | 32.404 | Telecommunication management; Performance Management (PM); Performance measurements; Definitions and template                                                        | S5    | Yes              |
| TS   | 32.405 | Telecommunication management; Performance Management (PM); Performance measurements; Universal Terrestrial Radio Access Network (UTRAN)                              | S5    | Yes              |
| TS   | 32.406 | Telecommunication management; Performance Management (PM); Performance measurements; Core Network (CN) Packet Switched (PS) domain                                   | S5    | Yes              |
| TS   | 32.408 | Telecommunication management; Performance Management (PM); Performance measurements; Teleservice                                                                     | S5    | Yes              |

| Type | Number | Title                                                                                                                                                                       | Group | For publication? |
|------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|------------------|
| TS   | 32.409 | Telecommunication management; Performance Management (PM); Performance measurements; IP Multimedia Subsystem (IMS)                                                          | S5    | Yes              |
| TS   | 32.410 | Telecommunication management; Key Performance Indicators (KPI) for UMTS and GSM                                                                                             | S5    | Yes              |
| TS   | 32.411 | Telecommunication management; Performance Management (PM) Integration Reference Point (IRP): Requirements                                                                   | S5    | Yes              |
| TS   | 32.412 | Telecommunication management; Performance Management (PM) Integration Reference Point (IRP): Information Service (IS)                                                       | S5    | Yes              |
| TS   | 32.413 | Telecommunication management; Performance Management (PM) Integration Reference Point (IRP): Common Object Request Broker Architecture (CORBA) Solution Set (SS)            | S5    | Yes              |
| TS   | 32.415 | Telecommunication management; Performance Management (PM) Integration Reference Point (IRP); eXtensible Markup Language (XML) definitions                                   | S5    | Yes              |
| TS   | 32.417 | Telecommunication management; Performance Management (PM) Integration Reference Point (IRP); SOAP Solution Set (SS)                                                         | S5    | Yes              |
| TS   | 32.421 | Telecommunication management; Subscriber and equipment trace; Trace concepts and requirements                                                                               | S5    | Yes              |
| TS   | 32.422 | Telecommunication management; Subscriber and equipment trace; Trace control and configuration management                                                                    | S5    | Yes              |
| TS   | 32.423 | Telecommunication management; Subscriber and equipment trace; Trace data definition and management                                                                          | S5    | Yes              |
| TS   | 32.425 | Telecommunication management; Performance Management (PM); Performance measurements Evolved Universal Terrestrial Radio Access Network (E-UTRAN)                            | S5    | Yes              |
| TS   | 32.426 | Telecommunication management; Performance Management (PM); Performance measurements Evolved Packet Core (EPC) network                                                       | S5    | Yes              |
| TS   | 32.432 | Telecommunication management; Performance measurement: File format definition                                                                                               | S5    | Yes              |
| TS   | 32.435 | Telecommunication management; Performance measurement; eXtensible Markup Language (XML) file format definition                                                              | S5    | Yes              |
| TS   | 32.436 | Telecommunication management; Performance measurement: Abstract Syntax Notation 1 (ASN.1) file format definition                                                            | S5    | Yes              |
| TS   | 32.441 | Telecommunication management; Trace Management Integration Reference Point (IRP); Requirements                                                                              | S5    | Yes              |
| TS   | 32.442 | Telecommunication management; Trace Management Integration Reference Point (IRP); Information Service (IS)                                                                  | S5    | Yes              |
| TS   | 32.443 | Telecommunication management; Trace Management (Trace) Integration Reference Point (IRP): Common Object Request Broker Architecture (CORBA) Solution Set (SS)               | S5    | Yes              |
| TS   | 32.445 | Telecommunication management; Trace Management Integration Reference Point (IRP): eXtensible Markup Language (XML) file format definition                                   | S5    | Yes              |
| TS   | 32.450 | Telecommunication management; Key Performance Indicators (KPI) for Evolved Universal Terrestrial Radio Access Network (E-UTRAN): Definitions                                | S5    | Yes              |
| TS   | 32.451 | Telecommunication management; Key Performance Indicators (KPI) for Evolved Universal Terrestrial Radio Access Network (E-UTRAN); Requirements                               | S5    | Yes              |
| TS   | 32.500 | Telecommunication management; Self-Organizing Networks (SON); Concepts and requirements                                                                                     | S5    | Yes              |
| TS   | 32.501 | Telecommunication management; Self-configuration of network elements; Concepts and requirements                                                                             | S5    | Yes              |
| TS   | 32.502 | Telecommunication management; Self-configuration of network elements Integration Reference Point (IRP); Information Service (IS)                                            | S5    | Yes              |
| TS   | 32.503 | Telecommunication management; Self-configuration of network elements Integration Reference Point (IRP); Common Object Request Broker Architecture (CORBA) Solution Set (SS) | S5    | Yes              |
| TS   | 32.507 | Telecommunication management; Self-configuration of network elements Integration Reference Point (IRP); SOAP Solution Set (SS)                                              | S5    | Yes              |

| Type | Number | Title                                                                                                                                                                                                            | Group | For publication? |
|------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|------------------|
| TS   | 32.511 | Telecommunication management; Automatic Neighbour Relation (ANR) management; Concepts and requirements                                                                                                           | S5    | Yes              |
| TS   | 32.521 | Telecommunication management; Self-Organizing Networks (SON) Policy Network Resource Model (NRM) Integration Reference Point (IRP); Requirements                                                                 | S5    | Yes              |
| TS   | 32.522 | Telecommunication management; Self-Organizing Networks (SON) Policy Network Resource Model (NRM) Integration Reference Point (IRP); Information Service (IS)                                                     | S5    | Yes              |
| TS   | 32.523 | Telecommunication management; Self-Organizing Networks (SON); Policy Network Resource Model (NRM) Integration Reference Point (IRP); Common Object Request Broker Architecture (CORBA) Solution Set (SS)         | S5    | Yes              |
| TS   | 32.525 | Telecommunication management; Self-Organizing Networks (SON) Policy Network Resource Model (NRM) Integration Reference Point (IRP); eXtensible Markup Language (XML) file format definition                      | S5    | Yes              |
| TS   | 32.531 | Telecommunication management; Software management (SwM); Concepts and Integration Reference Point (IRP) Requirements                                                                                             | S5    | Yes              |
| TS   | 32.532 | Telecommunication management; Software management (SwM); Integration Reference Point (IRP); Information Service (IS)                                                                                             | S5    | Yes              |
| TS   | 32.533 | Telecommunication management; Software management (SwM); Integration Reference Point (IRP); Common Object Request Broker Architecture (CORBA) Solution Set (SS)                                                  | S5    | Yes              |
| TS   | 32.571 | Telecommunication management; Home Node B (HNB) and Home eNode B (HeNB) management; Type 2 interface concepts and requirements                                                                                   | S5    | Yes              |
| TS   | 32.572 | Telecommunication management; Home Node B (HNB) and Home eNode B (HeNB) management; Type 2 interface models and mapping functions                                                                                | S5    | Yes              |
| TS   | 32.581 | Telecommunication management; Home Node B (HNB) Operations, Administration, Maintenance and Provisioning (OAM&P); Concepts and requirements for Type 1 interface HNB to HNB Management System (HMS)              | S5    | Yes              |
| TS   | 32.582 | Telecommunication management; Home Node B (HNB) Operations, Administration, Maintenance and Provisioning (OAM&P); Information model for Type 1 interface HNB to HNB Management System (HMS)                      | S5    | Yes              |
| TS   | 32.583 | Telecommunication management; Home Node B (HNB) Operations, Administration, Maintenance and Provisioning (OAM&P); Procedure flows for Type 1 interface HNB to HNB Management System (HMS)                        | S5    | Yes              |
| TS   | 32.584 | Telecommunication management; Home Node B (HNB) Operations, Administration, Maintenance and Provisioning (OAM&P); XML definitions for Type 1 interface HNB to HNB Management System (HMS)                        | S5    | Yes              |
| TS   | 32.591 | Telecommunication management; Home enhanced Node B (HeNB) Operations, Administration, Maintenance and Provisioning (OAM&P); Concepts and requirements for Type 1 interface HeNB to HeNB Management System (HeMS) | S5    | Yes              |
| TS   | 32.592 | Telecommunication management; Home enhanced Node B (HeNB) Operations, Administration, Maintenance and Provisioning (OAM&P); Information model for Type 1 interface HeNB to HeNB Management System (HeMS)         | S5    | Yes              |
| TS   | 32.593 | Telecommunication management; Home enhanced Node B (HeNB) Operations, Administration, Maintenance and Provisioning (OAM&P); Procedure flows for Type 1 interface HeNB to HeNB Management System (HeMS)           | S5    | Yes              |
| TS   | 32.594 | Telecommunication management; Home enhanced Node B (HeNB) Operations, Administration, Maintenance and Provisioning (OAM&P); XML definitions for Type 1 interface HeNB to HeNB Management System (HeMS)           | S5    | Yes              |
| TS   | 32.600 | Telecommunication management; Configuration Management (CM); Concept and high-level requirements                                                                                                                 | S5    | Yes              |
| TS   | 32.601 | Telecommunication management; Configuration Management (CM); Basic CM Integration Reference Point (IRP); Requirements                                                                                            | S5    | Yes              |
| TS   | 32.602 | Telecommunication management; Configuration Management (CM); Basic CM Integration Reference Point (IRP); Information Service (IS)                                                                                | S5    | Yes              |

| Type | Number | Title                                                                                                                                                                                         | Group | For publication? |
|------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|------------------|
| TS   | 32.603 | Telecommunication management; Configuration Management (CM); Basic CM Integration Reference Point (IRP); Common Object Request Broker Architecture (CORBA) Solution Set (SS)                  | S5    | Yes              |
| TS   | 32.607 | Telecommunication management; Configuration Management (CM); Basic CM Integration Reference Point (IRP); SOAP Solution Set (SS)                                                               | S5    | Yes              |
| TS   | 32.611 | Telecommunication management; Configuration Management (CM); Bulk CM Integration Reference Point (IRP): Requirements                                                                          | S5    | Yes              |
| TS   | 32.612 | Telecommunication management; Configuration Management (CM); Bulk CM Integration Reference Point (IRP): Information Service (IS)                                                              | S5    | Yes              |
| TS   | 32.613 | Telecommunication management; Configuration Management (CM); Bulk CM Integration Reference Point (IRP): Common Object Request Broker Architecture (CORBA) Solution Set (SS)                   | S5    | Yes              |
| TS   | 32.615 | Telecommunication management; Configuration Management (CM); Bulk CM Integration Reference Point (IRP): eXtensible Markup Language (XML) file format definition                               | S5    | Yes              |
| TS   | 32.617 | Telecommunication management; Configuration Management (CM); Bulk CM Integration Reference Point (IRP): Bulk CM IRP SOAP Solution Set (SS)                                                    | S5    | Yes              |
| TS   | 32.621 | Telecommunication management; Configuration Management (CM); Generic network resources Integration Reference Point (IRP): Requirements                                                        | S5    | Yes              |
| TS   | 32.622 | Telecommunication management; Configuration Management (CM); Generic network resources Integration Reference Point (IRP); Network Resource Model (NRM)                                        | S5    | Yes              |
| TS   | 32.623 | Telecommunication management; Configuration Management (CM); Generic network resources Integration Reference Point (IRP); Common Object Request Broker Architecture (CORBA) Solution Set (SS) | S5    | Yes              |
| TS   | 32.625 | Telecommunication management; Configuration Management (CM); Generic network resources Integration Reference Point (IRP): Bulk CM eXtensible Markup Language (XML) file format definition     | S5    | Yes              |
| TS   | 32.631 | Telecommunication management; Configuration Management (CM); Core network resources Integration Reference Point (IRP): Requirements                                                           | S5    | Yes              |
| TS   | 32.632 | Telecommunication management; Configuration Management (CM); Core Network Resources Integration Reference Point (IRP); Network Resource Model (NRM)                                           | S5    | Yes              |
| TS   | 32.633 | Telecommunication management; Configuration Management (CM); Core network resources Integration Reference Point (IRP); Common Object Request Broker Architecture (CORBA) Solution Set (SS)    | S5    | Yes              |
| TS   | 32.635 | Telecommunication management; Configuration Management (CM); Core network resources Integration Reference Point (IRP); Bulk CM eXtensible Markup Language (XML) file format definition        | S5    | Yes              |
| TS   | 32.661 | Telecommunication management; Configuration Management (CM); Kernel CM Requirements                                                                                                           | S5    | Yes              |
| TS   | 32.662 | Telecommunication management; Configuration Management (CM); Kernel CM Information Service (IS)                                                                                               | S5    | Yes              |
| TS   | 32.663 | Telecommunication management; Configuration Management (CM); Kernel CM Integration Reference Point (IRP); Common Object Request Broker Architecture (CORBA) Solution Set (SS)                 | S5    | Yes              |
| TS   | 32.665 | Telecommunication management; Configuration Management (CM); Kernel CM Integration Reference Point (IRP); eXtensible Markup Language (XML) definitions                                        | S5    | Yes              |
| TS   | 32.667 | Telecommunication management; Configuration Management (CM); Kernel CM Integration Reference Point (IRP); SOAP Solution Set (SS)                                                              | S5    | Yes              |
| TS   | 32.671 | Telecommunication management; Configuration Management (CM); State Management Integration Reference Point (IRP): Requirements                                                                 | S5    | Yes              |
| TS   | 32.672 | Telecommunication management; Configuration Management (CM); State Management Integration Reference Point (IRP); Information Service (IS)                                                     | S5    | Yes              |

| Type | Number | Title                                                                                                                                                                                                                                         | Group | For publication? |
|------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|------------------|
| TS   | 32.673 | Telecommunication management; Configuration Management (CM); State Management Integration Reference Point (IRP); Common Object Request Broker Architecture (CORBA) Solution Set (SS)                                                          | S5    | Yes              |
| TS   | 32.675 | Telecommunication management; Configuration Management (CM); State Management Integration Reference Point (IRP); Bulk CM eXtensible Markup Language (XML) file format definition                                                              | S5    | Yes              |
| TS   | 32.690 | Telecommunication management; Inventory Management (IM); Requirements                                                                                                                                                                         | S5    | Yes              |
| TS   | 32.691 | Telecommunication management; Inventory Management (IM) network resources Integration Reference Point (IRP); Requirements                                                                                                                     | S5    | Yes              |
| TS   | 32.692 | Telecommunication management; Inventory Management (IM) network resources Integration Reference Point (IRP); Network Resource Model (NRM)                                                                                                     | S5    | Yes              |
| TS   | 32.695 | Telecommunication management; Inventory Management (IM) network resources Integration Reference Point (IRP); Bulk Configuration Management (CM) eXtensible Markup Language (XML) file format definition                                       | S5    | Yes              |
| TS   | 32.711 | Telecommunication management; Configuration Management (CM); Transport Network (TN) interface Network Resource Model (NRM) Integration Reference Point (IRP); Requirements                                                                    | S5    | Yes              |
| TS   | 32.712 | Telecommunication management; Configuration Management (CM); Transport Network (TN) interface Network Resource Model (NRM) Integration Reference Point (IRP); Information Service (IS)                                                        | S5    | Yes              |
| TS   | 32.713 | Telecommunication management; Configuration Management (CM); Transport Network (TN) Network Resource Model (NRM) Integration Reference Point (IRP); Common Object Request Broker Architecture (CORBA) Solution Set (SS)                       | S5    | Yes              |
| TS   | 32.715 | Telecommunication management; Configuration Management (CM) Transport Network (TN); Network Resource Model (NRM) Integration Reference Point (IRP); Bulk CM eXtensible Markup Language (XML) file format definition                           | S5    | Yes              |
| TS   | 32.721 | Telecommunication management; Configuration Management (CM); Repeater network resources Integration Reference Point (IRP); Requirements                                                                                                       | S5    | Yes              |
| TS   | 32.722 | Telecommunication management; Configuration Management (CM); Repeater network resources Integration Reference Point (IRP); information Service (IS)                                                                                           | S5    | Yes              |
| TS   | 32.723 | Telecommunication management; Configuration Management (CM); Repeater network resources Integration Reference Point (IRP); Common Object Request Broker Architecture (CORBA) Solution Set (SS)                                                | S5    | Yes              |
| TS   | 32.725 | Telecommunication management; Configuration Management (CM); Repeater network resources Integration Reference Point (IRP); Bulk CM eXtensible Markup Language (XML) file format definition                                                    | S5    | Yes              |
| TS   | 32.731 | Telecommunication management; IP Multimedia Subsystem (IMS) Network Resource Model (NRM) Integration Reference Point (IRP); Requirements                                                                                                      | S5    | Yes              |
| TS   | 32.732 | Telecommunication management; IP Multimedia Subsystem (IMS) Network Resource Model (NRM) Integration Reference Point (IRP); Information Service (IS)                                                                                          | S5    | Yes              |
| TS   | 32.733 | Telecommunication management; IP Multimedia Subsystem (IMS) Network Resource Model (NRM) Integration Reference Point (IRP); Common Object Request Broker Architecture (CORBA) Solution Set (SS)                                               | S5    | Yes              |
| TS   | 32.735 | Telecommunication management; IP Multimedia Subsystem (IMS) Network Resource Model (NRM) Integration Reference Point (IRP); Bulk CM eXtensible Markup Language (XML) file format definition                                                   | S5    | Yes              |
| TS   | 32.741 | Telecommunication management; Configuration Management (CM); Signalling Transport Network (STN) interface Network Resource Model (NRM) Integration Reference Point (IRP); Requirements                                                        | S5    | Yes              |
| TS   | 32.742 | Telecommunication management; Configuration Management (CM); Signalling Transport Network (STN) interface Network Resource Model (NRM) Integration Reference Point (IRP); Information Service (IS)                                            | S5    | Yes              |
| TS   | 32.743 | Telecommunication management; Configuration Management (CM); Signalling Transport Network (STN) interface Network Resource Model (NRM) Integration Reference Point (IRP); Common Object Request Broker Architecture (CORBA) Solution Set (SS) | S5    | Yes              |

| Type | Number | Title                                                                                                                                                                                                                                     | Group | For publication? |
|------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|------------------|
| TS   | 32.745 | Telecommunication management; Configuration Management (CM); Signalling Transport Network (STN) interface Network Resource Model (NRM) Integration Reference Point (IRP); Bulk CM eXtensible Markup Language (XML) file format definition | S5    | Yes              |
| TS   | 32.751 | Telecommunication management; Evolved Packet Core (EPC) Network Resource Model (NRM) Integration Reference Point (IRP); Requirements                                                                                                      | S5    | Yes              |
| TS   | 32.752 | Telecommunication management; Evolved Packet Core (EPC) Network Resource Model (NRM) Integration Reference Point (IRP); Information Service (IS)                                                                                          | S5    | Yes              |
| TS   | 32.753 | Telecommunication management; Evolved Packet Core (EPC) Network Resource Model (NRM) Integration Reference Point (IRP); Common Object Request Broker Architecture (CORBA) Solution Set (SS)                                               | S5    | Yes              |
| TS   | 32.755 | Telecommunication management; Evolved Packet Core (EPC) Network Resource Model (NRM) Integration Reference Point (IRP); eXtensible Markup Language (XML) definitions                                                                      | S5    | Yes              |
| TS   | 32.761 | Telecommunication management; Evolved Universal Terrestrial Radio Access Network (E-UTRAN) Network Resource Model (NRM) Integration Reference Point (IRP); Requirements                                                                   | S5    | Yes              |
| TS   | 32.762 | Telecommunication management; Evolved Universal Terrestrial Radio Access Network (E-UTRAN) Network Resource Model (NRM) Integration Reference Point (IRP); Information Service (IS)                                                       | S5    | Yes              |
| TS   | 32.763 | Telecommunication management; Evolved Universal Terrestrial Radio Access Network (E-UTRAN) Network Resource Model (NRM) Integration Reference Point (IRP); Common Object Request Broker Architecture (CORBA) Solution Set (SS)            | S5    | Yes              |
| TS   | 32.765 | Telecommunication management; Evolved Universal Terrestrial Radio Access Network (E-UTRAN) Network Resource Model (NRM) Integration Reference Point (IRP); eXtensible Markup Language (XML) definitions                                   | S5    | Yes              |
| TS   | 33.102 | 3G security; Security architecture                                                                                                                                                                                                        | S3    | Yes              |
| TS   | 33.105 | 3G Security; Cryptographic algorithm requirements                                                                                                                                                                                         | S3    | Yes              |
| TS   | 33.106 | 3G security; Lawful interception requirements                                                                                                                                                                                             | S3    | Yes              |
| TS   | 33.107 | 3G security; Lawful interception architecture and functions                                                                                                                                                                               | S3    | Yes              |
| TS   | 33.108 | 3G security; Handover interface for Lawful Interception (LI)                                                                                                                                                                              | S3    | Yes              |
| TS   | 33.110 | Key establishment between a Universal Integrated Circuit Card (UICC) and a terminal                                                                                                                                                       | S3    | Yes              |
| TS   | 33.141 | Presence service; Security                                                                                                                                                                                                                | S3    | Yes              |
| TS   | 33.203 | 3G security; Access security for IP-based services                                                                                                                                                                                        | S3    | Yes              |
| TS   | 33.204 | 3G Security; Network Domain Security (NDS); Transaction Capabilities Application Part (TCAP) user security                                                                                                                                | S3    | Yes              |
| TS   | 33.210 | 3G security; Network Domain Security (NDS); IP network layer security                                                                                                                                                                     | S3    | Yes              |
| TS   | 33.220 | Generic Authentication Architecture (GAA); Generic Bootstrapping Architecture (GBA)                                                                                                                                                       | S3    | Yes              |
| TS   | 33.221 | Generic Authentication Architecture (GAA); Support for subscriber certificates                                                                                                                                                            | S3    | Yes              |
| TS   | 33.222 | Generic Authentication Architecture (GAA); Access to network application functions using Hypertext Transfer Protocol over Transport Layer Security (HTTPS)                                                                                | S3    | Yes              |
| TS   | 33.223 | Generic Authentication Architecture (GAA); Generic Bootstrapping Architecture (GBA) Push function                                                                                                                                         | S3    | Yes              |
| TS   | 33.224 | Generic Authentication Architecture (GAA); Generic Bootstrapping Architecture (GBA) push layer                                                                                                                                            | S3    | Yes              |
| TS   | 33.234 | 3G security; Wireless Local Area Network (WLAN) interworking security                                                                                                                                                                     | S3    | Yes              |
| TS   | 33.246 | 3G Security; Security of Multimedia Broadcast/Multicast Service (MBMS)                                                                                                                                                                    | S3    | Yes              |
| TS   | 33.259 | Key establishment between a UICC hosting device and a remote device                                                                                                                                                                       | S3    | Yes              |
| TS   | 33.310 | Network Domain Security (NDS); Authentication Framework (AF)                                                                                                                                                                              | S3    | Yes              |

| Type | Number   | Title                                                                                                                                                                                                                                                      | Group | For publication? |
|------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|------------------|
| TS   | 33.401   | 3GPP System Architecture Evolution (SAE); Security architecture                                                                                                                                                                                            | S3    | Yes              |
| TS   | 33.402   | 3GPP System Architecture Evolution (SAE); Security aspects of non-3GPP accesses                                                                                                                                                                            | S3    | Yes              |
| TR   | 33.812   | Feasibility study on the security aspects of remote provisioning and change of subscription for Machine to Machine (M2M) equipment                                                                                                                         | S3    | No               |
| TR   | 33.821   | Rationale and track of security decisions in Long Term Evolution (LTE) RAN / 3GPP System Architecture Evolution (SAE)                                                                                                                                      | S3    | No               |
| TR   | 33.828   | IP Multimedia Subsystem (IMS) media plane security                                                                                                                                                                                                         | S3    | No               |
| TR   | 33.905   | Recommendations for Trusted Open Platforms                                                                                                                                                                                                                 | S3    | Yes              |
| TR   | 33.919   | 3G Security; Generic Authentication Architecture (GAA); System description                                                                                                                                                                                 | S3    | Yes              |
| TR   | 33.937   | Study of mechanisms for Protection against Unsolicited Communication for IMS (PUCI)                                                                                                                                                                        | S3    | Yes              |
| TR   | 33.980   | Liberty Alliance and 3GPP security interworking; Interworking of Liberty Alliance Identity Federation Framework (ID-FF), Identity Web Services Framework (ID-WSF) and Generic Authentication Architecture (GAA)                                            | S3    | Yes              |
| TS   | 34.108   | Common test environments for User Equipment (UE); Conformance testing                                                                                                                                                                                      | R5    | Yes              |
| TS   | 34.114   | User Equipment (UE) / Mobile Station (MS) Over The Air (OTA) antenna performance; Conformance testing                                                                                                                                                      | R5    | Yes              |
| TS   | 34.123-1 | User Equipment (UE) conformance specification; Part 1: Protocol conformance specification                                                                                                                                                                  | R5    | Yes              |
| TS   | 34.123-2 | User Equipment (UE) conformance specification; Part 2: Implementation conformance statement (ICS) proforma specification                                                                                                                                   | R5    | Yes              |
| TS   | 34.123-3 | User Equipment (UE) conformance specification; Part 3: Abstract test suite (ATS)                                                                                                                                                                           | R5    | Yes              |
| TS   | 34.124   | Electromagnetic compatibility (EMC) requirements for mobile terminals and ancillary equipment                                                                                                                                                              | R4    | Yes              |
| TS   | 34.131   | Test Specification for C-language binding to (Universal) Subscriber Interface Module ((U)SIM) Application Programming Interface (API)                                                                                                                      | C6    | Yes              |
| TS   | 34.171   | Terminal conformance specification; Assisted Global Positioning System (A-GPS); Frequency Division Duplex (FDD)                                                                                                                                            | R5    | Yes              |
| TS   | 34.229-1 | Internet Protocol (IP) multimedia call control protocol based on Session Initiation Protocol (SIP) and Session Description Protocol (SDP); User Equipment (UE) conformance specification; Part 1: Protocol conformance specification                       | R5    | Yes              |
| TS   | 34.229-2 | Internet Protocol (IP) multimedia call control protocol based on Session Initiation Protocol (SIP) and Session Description Protocol (SDP); User Equipment (UE) conformance specification; Part 2: Implementation Conformance Statement (ICS) specification | R5    | Yes              |
| TS   | 34.229-3 | Internet Protocol (IP) multimedia call control protocol based on Session Initiation Protocol (SIP) and Session Description Protocol (SDP); User Equipment (UE) conformance specification; Part 3: Abstract test suite (ATS)                                | R5    | Yes              |
| TR   | 34.926   | Electromagnetic compatibility (EMC); Table of international requirements for mobile terminals and ancillary equipment                                                                                                                                      | R4    | Yes              |
| TS   | 35.201   | 3G Security; Specification of the 3GPP confidentiality and integrity algorithms; Document 1: f8 and f9 specification                                                                                                                                       | S3    | Yes              |
| TS   | 35.202   | 3G Security; Specification of the 3GPP confidentiality and integrity algorithms; Document 2: Kasumi specification                                                                                                                                          | S3    | Yes              |
| TS   | 35.203   | 3G Security; Specification of the 3GPP confidentiality and integrity algorithms; Document 3: Implementors' test data                                                                                                                                       | S3    | Yes              |
| TS   | 35.204   | 3G Security; Specification of the 3GPP confidentiality and integrity algorithms; Document 4: Design conformance test data                                                                                                                                  | S3    | Yes              |
| TS   | 35.205   | 3G Security; Specification of the MILENAGE algorithm set: An example algorithm set for the 3GPP authentication and key generation functions f1, f1*, f2, f3, f4, f5 and f5*; Document 1: General                                                           | S3    | Yes              |

| Type | Number | Title                                                                                                                                                                                                                                 | Group | For publication? |
|------|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|------------------|
| TS   | 35.206 | 3G Security; Specification of the MILENAGE algorithm set: An example algorithm set for the 3GPP authentication and key generation functions f1, f1*, f2, f3, f4, f5 and f5*; Document 2: Algorithm specification                      | S3    | Yes              |
| TS   | 35.207 | 3G Security; Specification of the MILENAGE algorithm set: An example algorithm set for the 3GPP authentication and key generation functions f1, f1*, f2, f3, f4, f5 and f5*; Document 3: Implementors' test data                      | S3    | Yes              |
| TS   | 35.208 | 3G Security; Specification of the MILENAGE algorithm set: An example algorithm set for the 3GPP authentication and key generation functions f1, f1*, f2, f3, f4, f5 and f5*; Document 4: Design conformance test data                 | S3    | Yes              |
| TS   | 35.215 | Specification of the 3GPP Confidentiality and Integrity Algorithms UEA2 & UIA2; Document 1: UEA2 and UIA2 specifications                                                                                                              | S3    | Yes              |
| TS   | 35.216 | Specification of the 3GPP Confidentiality and Integrity Algorithms UEA2 & UIA2; Document 2: SNOW 3G specification                                                                                                                     | S3    | Yes              |
| TS   | 35.217 | Specification of the 3GPP Confidentiality and Integrity Algorithms UEA2 & UIA2; Document 3: Implementors' test data                                                                                                                   | S3    | Yes              |
| TS   | 35.218 | Specification of the 3GPP Confidentiality and Integrity Algorithms UEA2 & UIA2; Document 4: Design conformance test data                                                                                                              | S3    | Yes              |
| TR   | 35.909 | 3G Security; Specification of the MILENAGE algorithm set: an example algorithm set for the 3GPP authentication and key generation functions f1, f1*, f2, f3, f4, f5 and f5*; Document 5: Summary and results of design and evaluation | S3    | Yes              |
| TR   | 35.919 | Specification of the 3GPP Confidentiality and Integrity Algorithms UEA2 & UIA2; Document 5: Design and evaluation report                                                                                                              | S3    | Yes              |
| TS   | 36.101 | Evolved Universal Terrestrial Radio Access (E-UTRA); User Equipment (UE) radio transmission and reception                                                                                                                             | R4    | Yes              |
| TS   | 36.104 | Evolved Universal Terrestrial Radio Access (E-UTRA); Base Station (BS) radio transmission and reception                                                                                                                               | R4    | Yes              |
| TS   | 36.106 | Evolved Universal Terrestrial Radio Access (E-UTRA); FDD repeater radio transmission and reception                                                                                                                                    | R4    | Yes              |
| TS   | 36.113 | Evolved Universal Terrestrial Radio Access (E-UTRA); Base Station (BS) and repeater ElectroMagnetic Compatibility (EMC)                                                                                                               | R4    | Yes              |
| TS   | 36.124 | Evolved Universal Terrestrial Radio Access (E-UTRA); Electromagnetic compatibility (EMC) requirements for mobile terminals and ancillary equipment                                                                                    | R4    | Yes              |
| TS   | 36.133 | Evolved Universal Terrestrial Radio Access (E-UTRA); Requirements for support of radio resource management                                                                                                                            | R4    | Yes              |
| TS   | 36.141 | Evolved Universal Terrestrial Radio Access (E-UTRA); Base Station (BS) conformance testing                                                                                                                                            | R4    | Yes              |
| TS   | 36.143 | Evolved Universal Terrestrial Radio Access (E-UTRA); FDD repeater conformance testing                                                                                                                                                 | R4    | Yes              |
| TS   | 36.171 | Evolved Universal Terrestrial Radio Access (E-UTRA); Requirements for Support of Assisted Global Navigation Satellite System (A-GNSS)                                                                                                 | R4    | Yes              |
| TS   | 36.201 | Evolved Universal Terrestrial Radio Access (E-UTRA); LTE physical layer; General description                                                                                                                                          | R1    | Yes              |
| TS   | 36.211 | Evolved Universal Terrestrial Radio Access (E-UTRA); Physical channels and modulation                                                                                                                                                 | R1    | Yes              |
| TS   | 36.212 | Evolved Universal Terrestrial Radio Access (E-UTRA); Multiplexing and channel coding                                                                                                                                                  | R1    | Yes              |
| TS   | 36.213 | Evolved Universal Terrestrial Radio Access (E-UTRA); Physical layer procedures                                                                                                                                                        | R1    | Yes              |
| TS   | 36.214 | Evolved Universal Terrestrial Radio Access (E-UTRA); Physical layer; Measurements                                                                                                                                                     | R1    | Yes              |
| TS   | 36.300 | Evolved Universal Terrestrial Radio Access (E-UTRA) and Evolved Universal Terrestrial Radio Access Network (E-UTRAN); Overall description; Stage 2                                                                                    | R2    | Yes              |
| TS   | 36.302 | Evolved Universal Terrestrial Radio Access (E-UTRA); Services provided by the physical layer                                                                                                                                          | R2    | Yes              |
| TS   | 36.304 | Evolved Universal Terrestrial Radio Access (E-UTRA); User Equipment (UE) procedures in idle mode                                                                                                                                      | R2    | Yes              |

| Type | Number | Title                                                                                                                                                                               | Group | For publication? |
|------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|------------------|
| TS   | 36.305 | Evolved Universal Terrestrial Radio Access Network (E-UTRAN); Stage 2 functional specification of User Equipment (UE) positioning in E-UTRAN                                        | R2    | Yes              |
| TS   | 36.306 | Evolved Universal Terrestrial Radio Access (E-UTRA); User Equipment (UE) radio access capabilities                                                                                  | R2    | Yes              |
| TS   | 36.307 | Evolved Universal Terrestrial Radio Access (E-UTRA); Requirements on User Equipments (UEs) supporting a release-independent frequency band                                          | R4    | Yes              |
| TS   | 36.314 | Evolved Universal Terrestrial Radio Access (E-UTRA); Layer 2 - Measurements                                                                                                         | R2    | Yes              |
| TS   | 36.321 | Evolved Universal Terrestrial Radio Access (E-UTRA); Medium Access Control (MAC) protocol specification                                                                             | R2    | Yes              |
| TS   | 36.322 | Evolved Universal Terrestrial Radio Access (E-UTRA); Radio Link Control (RLC) protocol specification                                                                                | R2    | Yes              |
| TS   | 36.323 | Evolved Universal Terrestrial Radio Access (E-UTRA); Packet Data Convergence Protocol (PDCP) specification                                                                          | R2    | Yes              |
| TS   | 36.331 | Evolved Universal Terrestrial Radio Access (E-UTRA); Radio Resource Control (RRC); Protocol specification                                                                           | R2    | Yes              |
| TS   | 36.355 | Evolved Universal Terrestrial Radio Access (E-UTRA); LTE Positioning Protocol (LPP)                                                                                                 | R2    | Yes              |
| TS   | 36.401 | Evolved Universal Terrestrial Radio Access Network (E-UTRAN); Architecture description                                                                                              | R3    | Yes              |
| TS   | 36.410 | Evolved Universal Terrestrial Radio Access Network (E-UTRAN); S1 general aspects and principles                                                                                     | R3    | Yes              |
| TS   | 36.411 | Evolved Universal Terrestrial Radio Access Network (E-UTRAN); S1 layer 1                                                                                                            | R3    | Yes              |
| TS   | 36.412 | Evolved Universal Terrestrial Radio Access Network (E-UTRAN); S1 signalling transport                                                                                               | R3    | Yes              |
| TS   | 36.413 | Evolved Universal Terrestrial Radio Access Network (E-UTRAN); S1 Application Protocol (S1AP)                                                                                        | R3    | Yes              |
| TS   | 36.414 | Evolved Universal Terrestrial Radio Access Network (E-UTRAN); S1 data transport                                                                                                     | R3    | Yes              |
| TS   | 36.420 | Evolved Universal Terrestrial Radio Access Network (E-UTRAN); X2 general aspects and principles                                                                                     | R3    | Yes              |
| TS   | 36.421 | Evolved Universal Terrestrial Radio Access Network (E-UTRAN); X2 layer 1                                                                                                            | R3    | Yes              |
| TS   | 36.422 | Evolved Universal Terrestrial Radio Access Network (E-UTRAN); X2 signalling transport                                                                                               | R3    | Yes              |
| TS   | 36.423 | Evolved Universal Terrestrial Radio Access Network (E-UTRAN); X2 Application Protocol (X2AP)                                                                                        | R3    | Yes              |
| TS   | 36.424 | Evolved Universal Terrestrial Radio Access Network (E-UTRAN); X2 data transport                                                                                                     | R3    | Yes              |
| TS   | 36.440 | Evolved Universal Terrestrial Radio Access Network (E-UTRAN); General aspects and principles for interfaces supporting Multimedia Broadcast Multicast Service (MBMS) within E-UTRAN | R3    | Yes              |
| TS   | 36.441 | Evolved Universal Terrestrial Radio Access Network (E-UTRAN); Layer 1 for interfaces supporting Multimedia Broadcast Multicast Service (MBMS) within E-UTRAN                        | R3    | Yes              |
| TS   | 36.442 | Evolved Universal Terrestrial Radio Access Network (E-UTRAN); Signalling Transport for interfaces supporting Multimedia Broadcast Multicast Service (MBMS) within E-UTRAN           | R3    | Yes              |
| TS   | 36.443 | Evolved Universal Terrestrial Radio Access Network (E-UTRAN); M2 Application Protocol (M2AP)                                                                                        | R3    | Yes              |
| TS   | 36.444 | Evolved Universal Terrestrial Radio Access Network (E-UTRAN); M3 Application Protocol (M3AP)                                                                                        | R3    | Yes              |
| TS   | 36.445 | Evolved Universal Terrestrial Radio Access Network (E-UTRAN); M1 data transport                                                                                                     | R3    | Yes              |
| TS   | 36.455 | Evolved Universal Terrestrial Radio Access (E-UTRA); LTE Positioning Protocol A (LPPa)                                                                                              | R3    | Yes              |

| Type | Number   | Title                                                                                                                                                                                                       | Group | For publication? |
|------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|------------------|
| TS   | 36.508   | Evolved Universal Terrestrial Radio Access (E-UTRA) and Evolved Packet Core (EPC); Common test environments for User Equipment (UE) conformance testing                                                     | R5    | Yes              |
| TS   | 36.509   | Evolved Universal Terrestrial Radio Access (E-UTRA) and Evolved Packet Core (EPC); Special conformance testing functions for User Equipment (UE)                                                            | R5    | Yes              |
| TS   | 36.521-1 | Evolved Universal Terrestrial Radio Access (E-UTRA); User Equipment (UE) conformance specification; Radio transmission and reception; Part 1: Conformance testing                                           | R5    | Yes              |
| TS   | 36.521-2 | Evolved Universal Terrestrial Radio Access (E-UTRA); User Equipment (UE) conformance specification; Radio transmission and reception; Part 2: Implementation Conformance Statement (ICS)                    | R5    | Yes              |
| TS   | 36.521-3 | Evolved Universal Terrestrial Radio Access (E-UTRA); User Equipment (UE) conformance specification; Radio transmission and reception; Part 3: Radio Resource Management (RRM) conformance testing           | R5    | Yes              |
| TS   | 36.523-1 | Evolved Universal Terrestrial Radio Access (E-UTRA) and Evolved Packet Core (EPC); User Equipment (UE) conformance specification; Part 1: Protocol conformance specification                                | R5    | Yes              |
| TS   | 36.523-2 | Evolved Universal Terrestrial Radio Access (E-UTRA) and Evolved Packet Core (EPC); User Equipment (UE) conformance specification; Part 2: Implementation Conformance Statement (ICS) proforma specification | R5    | Yes              |
| TS   | 36.523-3 | Evolved Universal Terrestrial Radio Access (E-UTRA) and Evolved Packet Core (EPC); User Equipment (UE) conformance specification; Part 3: Test suites                                                       | R5    | Yes              |
| TR   | 36.800   | Universal Terrestrial Radio Access (UTRA) and Evolved Universal Terrestrial Radio Access (E-UTRA); Extended UMTS / LTE 800 Work Item Technical Report                                                       | R4    | No               |
| TR   | 36.805   | Evolved Universal Terrestrial Radio Access (E-UTRA); Study on minimization of drive-tests in next generation networks                                                                                       | R2    | No               |
| TR   | 36.806   | Evolved Universal Terrestrial Radio Access (E-UTRA); Relay architectures for E-UTRA (LTE-Advanced)                                                                                                          | R2    | No               |
| TR   | 36.810   | Universal Terrestrial Radio Access (UTRA) and Evolved Universal Terrestrial Radio Access (E-UTRA); UMTS / LTE in 800 MHz for Europe                                                                         | R4    | No               |
| TR   | 36.814   | Evolved Universal Terrestrial Radio Access (E-UTRA); Further advancements for E-UTRA physical layer aspects                                                                                                 | R1    | No               |
| TR   | 36.815   | Further Advancements for E-UTRA; LTE-Advanced feasibility studies in RAN WG4                                                                                                                                | R4    | No               |
| TR   | 36.902   | Evolved Universal Terrestrial Radio Access Network (E-UTRAN); Self-configuring and self-optimizing network (SON) use cases and solutions                                                                    | R3    | Yes              |
| TR   | 36.903   | Evolved Universal Terrestrial Radio Access (E-UTRA) and Evolved Universal Terrestrial Radio Access Network (E-UTRAN); Derivation of test tolerances for Radio Resource Management (RRM) conformance tests   | R5    | Yes              |
| TR   | 36.921   | Evolved Universal Terrestrial Radio Access (E-UTRA); FDD Home eNode B (HeNB) Radio Frequency (RF) requirements analysis                                                                                     | R4    | Yes              |
| TR   | 36.922   | Evolved Universal Terrestrial Radio Access (E-UTRA); TDD Home eNode B (HeNB) Radio Frequency (RF) requirements analysis                                                                                     | R4    | Yes              |
| TR   | 36.931   | Evolved Universal Terrestrial Radio Access (E-UTRA); Radio Frequency (RF) requirements for LTE Pico Node B                                                                                                  | R4    | Yes              |
| TR   | 36.938   | Evolved Universal Terrestrial Radio Access Network (E-UTRAN); Improved network controlled mobility between E-UTRAN and 3GPP2/mobile WiMAX radio technologies                                                | R2    | Yes              |
| TR   | 36.942   | Evolved Universal Terrestrial Radio Access (E-UTRA); Radio Frequency (RF) system scenarios                                                                                                                  | R4    | Yes              |
| TS   | 37.104   | E-UTRA, UTRA and GSM/EDGE; Multi-Standard Radio (MSR) Base Station (BS) radio transmission and reception                                                                                                    | R4    | Yes              |
| TS   | 37.113   | E-UTRA, UTRA and GSM/EDGE; Multi-Standard Radio (MSR) Base Station (BS) Electromagnetic Compatibility (EMC)                                                                                                 | R4    | Yes              |
| TS   | 37.141   | E-UTRA, UTRA and GSM/EDGE; Multi-Standard Radio (MSR) Base Station (BS) conformance testing                                                                                                                 | R4    | Yes              |

| Type | Number   | Title                                                                                                                                                                                                                   | Group | For publication? |
|------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|------------------|
| TS   | 37.571-1 | Universal Terrestrial Radio Access (UTRA) and Evolved UTRA (E-UTRA) and Evolved Packet Core (EPC); User Equipment (UE) conformance specification for UE positioning; Part 1: Conformance test specification             | R5    | Yes              |
| TS   | 37.571-2 | Universal Terrestrial Radio Access (UTRA) and Evolved UTRA (E-UTRA) and Evolved Packet Core (EPC); User Equipment (UE) conformance specification for UE positioning; Part 2: Protocol conformance                       | R5    | Yes              |
| TS   | 37.571-3 | Universal Terrestrial Radio Access (UTRA) and Evolved UTRA (E-UTRA) and Evolved Packet Core (EPC); User Equipment (UE) conformance specification for UE positioning; Part 3: Implementation Conformance Statement (ICS) | R5    | Yes              |
| TS   | 37.571-4 | Universal Terrestrial Radio Access (UTRA) and Evolved UTRA (E-UTRA) and Evolved Packet Core (EPC); User Equipment (UE) conformance specification for UE positioning; Part 4: Test suites                                | R5    | Yes              |
| TS   | 37.571-5 | Universal Terrestrial Radio Access (UTRA) and Evolved UTRA (E-UTRA) and Evolved Packet Core (EPC); User Equipment (UE) conformance specification for UE positioning; Part 5: Test scenarios and assistance data         | R5    | Yes              |
| TR   | 37.900   | Radio Frequency (RF) requirements for Multicarrier and Multiple Radio Access Technology (Multi-RAT) Base Station (BS)                                                                                                   | R4    | Yes              |

Table is based on query " 2003-09-03\_LTE\_specs\_list\_rel-x\_21-201" in the [3GPP Specifications Status database](#).

# Annex A (informative): Change history

| Change history |                |                        |    |     |                                                                                                                      |       |       |
|----------------|----------------|------------------------|----|-----|----------------------------------------------------------------------------------------------------------------------|-------|-------|
| Date           | TSG #          | TSG Doc.               | CR | Rev | Subject/Comment                                                                                                      | Old   | New   |
| 2008-03        |                |                        |    |     | First draft based on SA1 request to SP-38, refined at SP-39. Spec list based on Specification Manager's whim.        |       | 0.0.0 |
| 2008-05        |                |                        |    |     | Rapporteur's revision                                                                                                | 0.0.0 | 0.1.0 |
| 2008-12        | SP-42          | SP-080723              |    |     | Rapporteur's revision prior to upgrading of specs to Rel-8 following Release freeze.                                 | 0.1.0 | 0.2.0 |
| 2009-01        |                |                        |    |     | Further rapporteur revision in the light of feedback                                                                 | 0.2.0 | 0.3.0 |
| 2009-03        | CP-43<br>RP-43 | CP-080927<br>RP-081048 |    |     | Submission for review                                                                                                | 0.3.0 | 1.0.0 |
| 2009-03        | SP-43          | SP-090034              |    |     | Clean up of §3. To SA for information.                                                                               | 1.0.0 | 1.0.1 |
| 2009-03        | SP-43          | SP-090224              |    |     | Major revision following clarification of scope, restricting the TS to a list of normative elements specific to EPS. | 1.0.1 | 2.0.0 |
| 2009-03        | SP-43          |                        |    |     | Approved                                                                                                             | 2.0.0 | 8.0.0 |
| 2009-06        | SP-45          | SP-090495              | 1  | 2   | Update list of Specs                                                                                                 | 8.0.0 |       |
|                |                |                        | 2  | 2   | Clarification of scope                                                                                               |       | 8.1.0 |
| 2009-12        | SP-46          | SP-090695              | 3  | 1   | Correction to list of specifications                                                                                 | 8.1.0 | 8.2.0 |
| 2010-03        | SP-47          | SP-100012              | 4  | -   | Update list of specs                                                                                                 | 8.2.0 | 8.3.0 |
| 2010-03        | SP-47          | SP-100012              | 5  | -   | Update list of specs                                                                                                 | 8.3.0 | 9.0.0 |
| 2011-03        | SP-51          |                        |    |     | Correction of Release 8 to Release 9 in Scope clause                                                                 | 9.0.0 | 9.0.1 |
| 2011-06        | SP-52          | SP-110298              | 7  | -   | Correction to list of specifications                                                                                 | 9.0.1 | 9.1.0 |
| 2012-03        | SP-55          | SP-120114              | 10 | 1   | Changes to list of Specs: LTE systems                                                                                | 9.1.0 | 9.2.0 |


<!-- ===== SOURCE FILE: raw__3_.md ===== -->



# Keywords UMTS, LTE, Packet Mode, Architecture, IP, IMS 3GPP TS 21.202 V9.3.0 (2012-03)

*Technical Specification*

## <sup>3GPP</sup> **3rd Generation Partnership Project;** ~~Postal address~~ **Technical Specification Group Services and System Aspects;** **Technical Specifications and Technical Reports relating to the** ~~2GPP support office address~~ **Common IP Multimedia Subsystem (IMS)**

![LTE logo](64662465bba247703fdec49c8f3309f9_img.jpg)

LTE logo

650 Route des Lucioles - Sophia Antipolis  
Valbonne - FRANCE  
Tel.: +33 4 92 94 42 00 Fax: +33 4 93 65 47 16

Internet  
<http://www.3gpp.org>

![3GPP logo](0538daaa5583c23e17db3a12f2281a55_img.jpg)

3GPP logo

# **Copyright Notification**

No part may be reproduced except as authorized by written permission.  
The copyright and the foregoing restriction extend to reproduction in all media.

© 2012, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TTA, TTC).  
All rights reserved.

UMTS™ is a Trade Mark of ETSI registered for the benefit of its members

3GPP™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners

LTE™ is a Trade Mark of ETSI currently being registered for the benefit of its Members and of the 3GPP Organizational Partners

GSM® and the GSM logo are registered and owned by the GSM Association.  
The present document has been developed within the 3rd Generation Partnership Project (3GPP™) and may be further elaborated for the purposes of 3GPP.

The present document has not been subject to any approval process by the 3GPP Organizational Partners and shall not be implemented.

This Specification is provided for future development work within 3GPP only. The Organizational Partners accept no liability for any use of this Specification.

Specifications and reports for implementation of the 3GPP™ system should be obtained via the 3GPP Organizational Partners' Publications Offices.

# --- Contents

|                                                                                     |           |
|-------------------------------------------------------------------------------------|-----------|
| Foreword .....                                                                      | 4         |
| 1 Scope.....                                                                        | 5         |
| 2 References.....                                                                   | 5         |
| 3 Definitions, symbols and abbreviations .....                                      | 5         |
| 3.1 Definitions.....                                                                | 5         |
| 3.2 Symbols.....                                                                    | 5         |
| 3.3 Abbreviations .....                                                             | 5         |
| 4 General.....                                                                      | 5         |
| 5 Specifications and Reports.....                                                   | 6         |
| <b>Annex A (informative): (void).....</b>                                           | <b>9</b>  |
| <b>Annex M (informative): IMS related Specifications and Reports in 3GPP2 .....</b> | <b>10</b> |
| <b>Annex C (informative): Change history.....</b>                                   | <b>12</b> |

# --- Foreword

This Technical Specification has been produced by the 3<sup>rd</sup> Generation Partnership Project (3GPP).

The contents of the present document are subject to continuing work within the TSG and may change following formal TSG approval. Should the TSG modify the contents of the present document, it will be re-released by the TSG with an identifying change of release date and an increase in version number as follows:

Version x.y.z

where:

- x the first digit:
  - 1 presented to TSG for information;
  - 2 presented to TSG for approval;
  - 3 or greater indicates TSG approved document under change control.
- y the second digit is incremented for all changes of substance, i.e. technical enhancements, corrections, updates, etc.
- z the third digit is incremented when editorial only changes have been incorporated in the document.

# --- 1 Scope

The present document identifies the 3GPP Technical Specifications and Technical Reports specifically relating to the Common IP Multimedia Subsystem (IMS) maintained by 3GPP. Standards organizations adopting the Common IP Multimedia Subsystem (IMS) might not need to use all listed specifications.

# --- 2 References

The following documents contain provisions which, through reference in this text, constitute provisions of the present document.

- References are either specific (identified by date of publication, edition number, version number, etc.) or non-specific.
- For a specific reference, subsequent revisions do not apply.
- For a non-specific reference, the latest version applies. In the case of a reference to a 3GPP document (including a GSM document), a non-specific reference implicitly refers to the latest version of that document *in the same Release as the present document*.

[1] 3GPP TR 21.905: "Vocabulary for 3GPP Specifications".

[2] 3GPP TR 21.900: "Technical specification group working methods"

# --- 3 Definitions, symbols and abbreviations

## 3.1 Definitions

For the purposes of the present document, the terms and definitions given in TR 21.905 [1] apply.

## 3.2 Symbols

(None)

## 3.3 Abbreviations

For the purposes of the present document, the abbreviations given in TR 21.905 [1] and the following apply. An abbreviation defined in the present document takes precedence over the definition of the same abbreviation, if any, in TR 21.905 [1].

|        |                                                                                        |
|--------|----------------------------------------------------------------------------------------|
| NGN    | Next Generation Network                                                                |
| R1     | Release 1                                                                              |
| R2     | Release 2                                                                              |
| TISPAN | Telecommunications and Internet converged Services and Protocols for Advanced Networks |

# --- 4 General

The numbering scheme for specifications is described in 3GPP TR 21.900 [2].

# 5 Specifications and Reports

NOTE 1: The "for publication?" column of the table below indicates whether or not the documents are intended for adoption by the partner Standards Development Organizations as their own publications. Those marked "no" are internal working documents of the 3GPP TSGs.

NOTE 2: "Type" indicates Technical Specification (TS) or Technical Report (TR).

The table below contains all Common IMS specs pertaining to Release 9.

| Type | Number | Title                                                                                                                                | Group | For publication? |
|------|--------|--------------------------------------------------------------------------------------------------------------------------------------|-------|------------------|
| TS   | 21.111 | USIM and IC card requirements                                                                                                        | C6    | Yes              |
| TR   | 21.905 | Vocabulary for 3GPP Specifications                                                                                                   | SP    | Yes              |
| TS   | 22.030 | Man-Machine Interface (MMI) of the User Equipment (UE)                                                                               | S1    | Yes              |
| TS   | 22.041 | Operator Determined Barring (ODB)                                                                                                    | S1    | Yes              |
| TS   | 22.071 | Location Services (LCS); Service description; Stage 1                                                                                | S1    | Yes              |
| TS   | 22.101 | Service aspects; Service principles                                                                                                  | S1    | Yes              |
| TS   | 22.105 | Services and service capabilities                                                                                                    | S1    | Yes              |
| TS   | 22.115 | Service aspects; Charging and billing                                                                                                | S1    | Yes              |
| TS   | 22.127 | Service requirement for the Open Services Access (OSA); Stage 1                                                                      | S1    | Yes              |
| TS   | 22.140 | Multimedia Messaging Service (MMS); Stage 1                                                                                          | S1    | Yes              |
| TS   | 22.141 | Presence service; Stage 1                                                                                                            | S1    | Yes              |
| TS   | 22.153 | Multimedia priority service                                                                                                          | S1    | Yes              |
| TS   | 22.173 | IP Multimedia Core Network Subsystem (IMS) Multimedia Telephony Service and supplementary services; Stage 1                          | S1    | Yes              |
| TS   | 22.174 | Push Service; Service aspects; Stage 1                                                                                               | S1    | Yes              |
| TS   | 22.182 | Customized Alerting Tones (CAT) requirements; Stage 1                                                                                | S1    | Yes              |
| TS   | 22.183 | Customized Ringing Signal (CRS) requirements; Stage 1                                                                                | S1    | Yes              |
| TS   | 22.228 | Service requirements for the Internet Protocol (IP) multimedia core network subsystem (IMS); Stage 1                                 | S1    | Yes              |
| TS   | 22.250 | IP Multimedia Subsystem (IMS) Group Management; Stage 1                                                                              | S1    | Yes              |
| TS   | 22.279 | Combined Circuit Switched (CS) and IP Multimedia Subsystem (IMS) sessions; Stage 1                                                   | S1    | Yes              |
| TS   | 22.340 | IP Multimedia Subsystem (IMS) messaging; Stage 1                                                                                     | S1    | Yes              |
| TR   | 22.979 | Feasibility study on combined Circuit Switched (CS) calls and IP Multimedia Subsystem (IMS) sessions                                 | S1    | Yes              |
| TS   | 23.141 | Presence service; Architecture and functional description                                                                            | S2    | Yes              |
| TS   | 23.167 | IP Multimedia Subsystem (IMS) emergency sessions                                                                                     | S2    | Yes              |
| TS   | 23.204 | Support of Short Message Service (SMS) over generic 3GPP Internet Protocol (IP) access; Stage 2                                      | S2    | Yes              |
| TS   | 23.218 | IP Multimedia (IM) session handling; IM call model; Stage 2                                                                          | C1    | Yes              |
| TS   | 23.228 | IP Multimedia Subsystem (IMS); Stage 2                                                                                               | S2    | Yes              |
| TS   | 23.333 | Multimedia Resource Function Controller (MRFC) - Multimedia Resource Function Processor (MRFP) Mp interface: Procedures descriptions | C4    | Yes              |
| TS   | 23.334 | IP Multimedia Subsystem (IMS) Application Level Gateway (IMS-ALG) – IMS Access Gateway (IMS-AGW) interface: Procedures descriptions  | C4    | Yes              |
| TS   | 24.141 | Presence service using the IP Multimedia (IM) Core Network (CN) subsystem; Stage 3                                                   | C1    | Yes              |
| TS   | 24.147 | Conferencing using the IP Multimedia (IM) Core Network (CN) subsystem; Stage 3                                                       | C1    | Yes              |

| Type | Number | Title                                                                                                                                                                                   | Group | For publication? |
|------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|------------------|
| TS   | 24.173 | IMS Multimedia telephony communication service and supplementary services; Stage 3                                                                                                      | C1    | Yes              |
| TS   | 24.182 | IP Multimedia Subsystem (IMS) Customized Alerting Tones (CAT); Protocol specification                                                                                                   | C1    | Yes              |
| TS   | 24.229 | IP multimedia call control protocol based on Session Initiation Protocol (SIP) and Session Description Protocol (SDP); Stage 3                                                          | C1    | Yes              |
| TS   | 24.238 | Session Initiation Protocol (SIP) based user configuration; Stage 3                                                                                                                     | C1    | Yes              |
| TS   | 24.239 | Flexible Alerting (FA) using IP Multimedia (IM) Core Network (CN) subsystem; Protocol specification                                                                                     | C1    | Yes              |
| TS   | 24.247 | Messaging service using the IP Multimedia (IM) Core Network (CN) subsystem; Stage 3                                                                                                     | C1    | Yes              |
| TS   | 24.341 | Support of SMS over IP networks; Stage 3                                                                                                                                                | C1    | Yes              |
| TS   | 24.604 | Communication Diversion (CDIV) using IP Multimedia (IM) Core Network (CN) subsystem; Protocol specification                                                                             | C1    | Yes              |
| TS   | 24.605 | Conference (CONF) using IP Multimedia (IM) Core Network (CN) subsystem; Protocol specification                                                                                          | C1    | Yes              |
| TS   | 24.606 | Message Waiting Indication (MWI) using IP Multimedia (IM) Core Network (CN) subsystem; Protocol specification                                                                           | C1    | Yes              |
| TS   | 24.607 | Originating Identification Presentation (OIP) and Originating Identification Restriction (OIR) using IP Multimedia (IM) Core Network (CN) subsystem; Protocol specification             | C1    | Yes              |
| TS   | 24.608 | Terminating Identification Presentation (TIP) and Terminating Identification Restriction (TIR) using IP Multimedia (IM) Core Network (CN) subsystem; Protocol specification             | C1    | Yes              |
| TS   | 24.610 | Communication HOLD (HOLD) using IP Multimedia (IM) Core Network (CN) subsystem; Protocol specification                                                                                  | C1    | Yes              |
| TS   | 24.611 | Anonymous Communication Rejection (ACR) and Communication Barring (CB) using IP Multimedia (IM) Core Network (CN) subsystem; Protocol specification                                     | C1    | Yes              |
| TS   | 24.615 | Communication Waiting (CW) using IP Multimedia (IM) Core Network (CN) subsystem; Protocol Specification                                                                                 | C1    | Yes              |
| TS   | 24.616 | Malicious Communication Identification (MCID) using IP Multimedia (IM) Core Network (CN) subsystem; Protocol specification                                                              | C1    | Yes              |
| TS   | 24.628 | Common Basic Communication procedures using IP Multimedia (IM) Core Network (CN) subsystem; Protocol specification                                                                      | C1    | Yes              |
| TS   | 24.629 | Explicit Communication Transfer (ECT) using IP Multimedia (IM) Core Network (CN) subsystem; Protocol specification                                                                      | C1    | Yes              |
| TS   | 24.642 | Completion of Communications to Busy Subscriber (CCBS) and Completion of Communications by No Reply (CCNR) using IP Multimedia (IM) Core Network (CN) subsystem; Protocol specification | C1    | Yes              |
| TS   | 24.647 | Advice Of Charge (AOC) using IP Multimedia (IM) Core Network (CN) subsystem                                                                                                             | C1    | Yes              |
| TS   | 24.654 | Closed User Group (CUG) using IP Multimedia (IM) Core Network (CN) subsystem, Protocol Specification                                                                                    | C1    | Yes              |
| TR   | 24.930 | Signalling flows for the session setup in the IP Multimedia core network Subsystem (IMS) based on Session Initiation Protocol (SIP) and Session Description Protocol (SDP); Stage 3     | C1    | Yes              |
| TS   | 29.162 | Interworking between the IM CN subsystem and IP networks                                                                                                                                | C3    | Yes              |
| TS   | 29.163 | Interworking between the IP Multimedia (IM) Core Network (CN) subsystem and Circuit Switched (CS) networks                                                                              | C3    | Yes              |
| TS   | 29.165 | Inter-IMS Network to Network Interface (NNI)                                                                                                                                            | C3    | Yes              |
| TS   | 29.212 | Policy and Charging Control (PCC) over Gx/Sd reference point                                                                                                                            | C3    | Yes              |
| TS   | 29.213 | Policy and charging control signalling flows and Quality of Service (QoS) parameter mapping                                                                                             | C3    | Yes              |
| TS   | 29.214 | Policy and charging control over Rx reference point                                                                                                                                     | C3    | Yes              |

| Type | Number | Title                                                                                                                           | Group | For publication? |
|------|--------|---------------------------------------------------------------------------------------------------------------------------------|-------|------------------|
| TS   | 29.215 | Policy and Charging Control (PCC) over S9 reference point; Stage 3                                                              | C3    | Yes              |
| TS   | 29.228 | IP Multimedia (IM) Subsystem Cx and Dx Interfaces; Signalling flows and message contents                                        | C4    | Yes              |
| TS   | 29.229 | Cx and Dx interfaces based on the Diameter protocol; Protocol details                                                           | C4    | Yes              |
| TS   | 29.232 | Media Gateway Controller (MGC) - Media Gateway (MGW) interface; Stage 3                                                         | C4    | Yes              |
| TS   | 29.238 | Interconnection Border Control Functions (IBCF) - Transition Gateway (TrGW) interface, Ix interface; Stage 3                    | C4    | Yes              |
| TS   | 29.292 | Interworking between the IP Multimedia (IM) Core Network (CN) subsystem (IMS) and MSC Server for IMS Centralized Services (ICS) | C3    | Yes              |
| TS   | 29.311 | Service level interworking for Messaging Services                                                                               | C3    | Yes              |
| TS   | 29.328 | IP Multimedia (IM) Subsystem Sh interface; Signalling flows and message contents                                                | C4    | Yes              |
| TS   | 29.329 | Sh interface based on the Diameter protocol; Protocol details                                                                   | C4    | Yes              |
| TS   | 29.333 | Multimedia Resource Function Controller (MRFC) - Multimedia Resource Function Processor (MRFP) Mp interface; Stage 3            | C4    | Yes              |
| TS   | 29.334 | IMS Application Level Gateway (IMS-ALG) - IMS Access Gateway (IMS-AGW); Iq Interface; Stage 3                                   | C4    | Yes              |
| TS   | 29.658 | SIP Transfer of IP Multimedia Service Tariff Information; Protocol specification                                                | C3    | Yes              |
| TS   | 31.101 | UICC-terminal interface; Physical and logical characteristics                                                                   | C6    | Yes              |
| TS   | 31.103 | Characteristics of the IP Multimedia Services Identity Module (ISIM) application                                                | C6    | Yes              |
| TS   | 31.115 | Remote APDU Structure for (U)SIM Toolkit applications                                                                           | C6    | Yes              |
| TS   | 31.116 | Remote APDU Structure for (U)SIM Toolkit applications                                                                           | C6    | Yes              |
| TS   | 31.133 | IP Multimedia Services Identity Module (ISIM) Application Programming Interface (API); ISIM API for Java Card™                  | C6    | Yes              |
| TS   | 32.240 | Telecommunication management; Charging management; Charging architecture and principles                                         | S5    | Yes              |
| TS   | 32.260 | Telecommunication management; Charging management; IP Multimedia Subsystem (IMS) charging                                       | S5    | Yes              |
| TS   | 32.299 | Telecommunication management; Charging management; Diameter charging applications                                               | S5    | Yes              |
| TR   | 32.824 | Telecommunication management; Service Oriented Architecture (SOA) Integration Reference Point (IRP) study                       | S5    | No               |
| TS   | 33.141 | Presence service; Security                                                                                                      | S3    | Yes              |
| TS   | 33.203 | 3G security; Access security for IP-based services                                                                              | S3    | Yes              |
| TS   | 33.210 | 3G security; Network Domain Security (NDS); IP network layer security                                                           | S3    | Yes              |

Tables are based on query " 2003-09-03\_CmnIMS\_specs\_list\_rel-x \_\_21-202" in the [3GPP Specifications Status database](#).

---

Annex A (informative):  
(void)

## Annex M (informative): IMS related Specifications and Reports in 3GPP2

The table below shows the 3GPP2 publications relating to core functions of the IP Multimedia Subsystem (IMS) used by the 3GPP2. Also shown in the table is the mapping between the replaced 3GPP2 MMD specifications and the corresponding 3GPP IMS specifications which replace them and the final revision of the document that was published by 3GPP2.

| 3GPP2 Document Number and Revision | 3GPP2 Document Title                                                                 | 3GPP Rel-8 TS/TR                    | 3GPP WG        |
|------------------------------------|--------------------------------------------------------------------------------------|-------------------------------------|----------------|
| X.S0013-000-B v1.0                 | Overview                                                                             | TS 23.002                           | S2             |
| X.S0013-002-B v1.0                 | IP Multimedia Subsystem – Stage 2                                                    | TS 23.228<br>TS 23.228<br>TS 23.002 | S2<br>S2       |
| X.S0013-003-B v1.0                 | IP Multimedia Session Handling; IP Multimedia Call Model – Stage 2                   | TS 23.218                           | C1             |
| X.S0013-004-B v1.0                 | IP Multimedia Call Control Protocol Based on SIP and SDP - Stage 3                   | TS 24.229                           | C1             |
| X.S0013-005-B v1.0                 | IP Multimedia Subsystem Cx Interface Signaling flows and Message Contents            | TS 29.228                           | C4             |
| X.S0013-006-B v1.0                 | Cx Interface Based on the Diameter Protocol; Protocol Details                        | TS 29.229                           | C4             |
| X.S0013-007-A v1.0                 | IP Multimedia Subsystem - Charging Architecture                                      | TS 32.240<br>TS 32.260              | S5<br>S5       |
| X.S0013-008-A v1.0                 | IP Multimedia Subsystem - Offline Accounting Information Flows and Protocol          | TS 32.260<br>TS 32.299              | S5<br>S5       |
| X.S0013-009-0 v1.0                 | IMS/MMD Call Flow Examples                                                           | TR 24.930                           | C1             |
| X.S0013-010-B v1.0                 | IP Multimedia Subsystem Sh interface; Signaling flows and message contents – Stage 2 | TS 29.328                           | C4             |
| X.S0013-011-B v1.0                 | Sh Interface based on Diameter Protocols Protocol Details – Stage 3                  | TS 29.329                           | C4             |
| X.S0013-012-0 v1.0                 | Service Based Bearer Control – Stage 2                                               | TS 23.203                           | S2             |
| X.S0013-013-0 v1.0                 | Service Based Bearer Control – Tx Interface Stage 3                                  | TS 29.213<br>TS 29.214              | C3<br>C3       |
| X.S0013-014-0 v1.0                 | Service Based Bearer Control – Ty Interface Stage 3                                  | TS 29.212<br>TS 29.215              | C3<br>C3       |
| X.S0013-016-0 v1.0                 | Messaging Service Using the IP Multimedia Subsystem                                  | TS 24.247                           | C1             |
| X.S0027-000-A v1.0                 | Presence Overview                                                                    | No 3GPP equivalent                  |                |
| X.S0027-001-0 v1.0                 | Presence Service: Architecture and Functional Description                            | TS 23.141                           | S2             |
| X.S0027-002-0 v1.0                 | Presence Security                                                                    | TS 33.141                           | S3             |
| X.S0027-003-0 v1.0                 | Presence Stage 3                                                                     | TS 24.141                           | C1             |
| X.S0027-004-0 v1.0                 | Network Presence                                                                     | No 3GPP equivalent                  |                |
| X.S0029-0 v1.0                     | Conferencing Using the IP Multimedia (IM) Core Network (CN) Subsystem                | TS 24.147                           | C1             |
| X.S0049-0 v1.0                     | All-IP Network Emergency Call Support                                                | TS 23.167<br>TS 24.229              | S2<br>C1       |
| X.S0055-0 v1.0                     | MMD Supplementary Services                                                           | TS 24.173<br>TS 24.182<br>TS 24.238 | C1<br>C1<br>C1 |

|                |                                                                |                    |    |
|----------------|----------------------------------------------------------------|--------------------|----|
|                |                                                                | TS 24.239          | C1 |
|                |                                                                | TS 24.604          | C1 |
|                |                                                                | TS 24.605          | C1 |
|                |                                                                | TS 24.606          | C1 |
|                |                                                                | TS 24.607          | C1 |
|                |                                                                | TS 24.608          | C1 |
|                |                                                                | TS 24.610          | C1 |
|                |                                                                | TS 24.611          | C1 |
|                |                                                                | TS 24.615          | C1 |
|                |                                                                | TS 24.628          | C1 |
|                |                                                                | TS 24.629          | C1 |
| S.S0086-B v2.0 | IMS Security Framework                                         | TS 33.203          | S3 |
|                |                                                                | TS 33.210          | S3 |
| S.R0058        | IP Multimedia Domain – System Requirements                     | TS 22.228          | S1 |
| S.R0062        | Presence for Wireless Systems – Stage 1 Requirements           | TS 22.141          | S1 |
| S.R0125        | VoIP Supplementary Services Feature Description                | TS 22.173          | S1 |
| X.R0052-0      | All-IP System – MMD Roaming Technical Report                   | No 3GPP equivalent |    |
| X.S0042        | Voice Call Continuity between IMS and Circuit Switched Systems | TS 23.206          | S2 |
|                |                                                                | TS 24.206          | C1 |
| C.S0069        | ISIM Application on UICC for cdma2000 Spread Spectrum Systems  | TS 31.103          | C6 |

## Annex C (informative): Change history

| Change history |       |           |    |     |                                                                                                                                                                                          |       |       |
|----------------|-------|-----------|----|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|-------|
| Date           | TSG # | TSG Doc.  | CR | Rev | Subject/Comment                                                                                                                                                                          | Old   | New   |
| 2008-05        |       |           |    |     | First draft based on SA1 request to SP-38, refined at SP-39. Spec list based on Specification Manager's whim.                                                                            |       | 0.0.0 |
| 2008-12        |       |           |    |     | Update based on continuing evolution of Release 8 specs                                                                                                                                  | 0.0.0 | 0.1.0 |
| 2008-12        | SP-42 | SP-080724 |    |     | Incorporation of comments from TSG CT: removal of §5.1 (substituted by two examples in annex A); indication in list of specs of those which do not progress beyond NGN R2 applicability. | 0.1.0 | 0.2.0 |
| 2009-01        |       |           |    |     | Update to specs list table resulting from further feedback; Correction to URL of TISPAN spec mapping following revamp of 3GPP web site                                                   | 0.2.0 | 0.3.0 |
| 2009-03        | CP-43 | CP-090103 |    |     | Presentation for information                                                                                                                                                             | 0.3.0 | 1.0.0 |
| 2009-03        | SP-43 | SP-090035 |    |     | Presentation to TSG for approval                                                                                                                                                         | 1.0.0 | 1.1.0 |
| 2009-03        | SP-43 |           |    |     | Approved                                                                                                                                                                                 | 1.1.0 | 8.0.0 |
| 2009-05        | SP-44 | SP-090463 | 2  | 2   | Annex mapping 3GPP2 specs to 3GPP common IMS specs                                                                                                                                       | 8.0.0 |       |
|                |       | SP-090464 | 3  |     | Revise scope                                                                                                                                                                             |       | 8.1.0 |
| 2009-06        | SP-46 | SP-090695 | 4  | 1   | Correction to list of specifications                                                                                                                                                     | 8.1.0 | 8.2.0 |
| 2010-03        | SP-47 | SP-100012 | 5  |     | Update list of specs                                                                                                                                                                     | 8.2.0 | 8.3.0 |
|                |       |           | 6  |     | Update list of specs                                                                                                                                                                     | 8.3.0 |       |
|                |       |           | 7  |     | Removal of information only relevant for earlier Release                                                                                                                                 |       | 9.0.0 |
| 2010-12        | SP-50 | SP-100871 | 8  | 1   | Clarification of scope to indicate use of complete set of TSs/TRs is not obligatory in all IMS implementations                                                                           | 9.0.0 | 9.1.0 |
| 2011-06        | SP-52 | SP-110298 | 10 |     | Correction to list of specifications                                                                                                                                                     | 9.1.0 | 9.2.0 |
| 2012-03        | SP-55 | SP-120114 | 13 | 1   | Changes to list of Specs: common IMS                                                                                                                                                     | 9.2.0 | 9.3.0 |

Error! No

12

Error! No text of specified style in

Error! No

12

Error! No text of specified style in

Error! No

1

Error! No text of specified style in

**3GPP**

**3GPP**

**3GPP**


<!-- ===== SOURCE FILE: raw__4_.md ===== -->



# 3rd Generation Partnership Project; Technical Specification Group Services and System Aspects; **3GPP TR 21.801** (2010-09) **Specification drafting rules** *Technical Report* **(Release 9)** ---

![LTE logo](935eed7aa61f7777f62cfc032e11bee9_img.jpg)

---

The LTE logo features the lowercase letters 'lte' in a bold, sans-serif font. Above the 'l' and 't' are three red curved lines representing signal waves. A small 'TM' trademark symbol is located to the right of the 'e'.

LTE logo

![3GPP logo](30a26f2d17ca95672702bf50fb4f0242_img.jpg)

The 3GPP logo consists of the letters '3GPP' in a stylized, bold, black font. The '3' is slightly larger and positioned to the left. Below the 'P' is a small red signal wave icon. A small 'TM' trademark symbol is located to the right of the 'P'.

3GPP logo

The present document has been developed within the 3<sup>rd</sup> Generation Partnership Project (3GPP<sup>TM</sup>) and may be further elaborated for the purposes of 3GPP.

The present document has not been subject to any approval process by the 3GPP Organizational Partners and shall not be implemented.

This Specification is provided for future development work within 3GPP only. The Organizational Partners accept no liability for any use of this Specification.

Specifications and reports for implementation of the 3GPP<sup>TM</sup> system should be obtained via the 3GPP Organizational Partners' Publications Offices.

Keywords  
GSM, UMTS, LTE, methodology

## **3GPP**

Postal address

---

3GPP support office address

---

650 Route des Lucioles - Sophia Antipolis  
Valbonne - FRANCE  
Tel.: +33 4 92 94 42 00 Fax: +33 4 93 65 47 16

Internet

---

<http://www.3gpp.org>

## **Copyright Notification**

No part may be reproduced except as authorized by written permission.  
The copyright and the foregoing restriction extend to reproduction in all media.

© 2010, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TTA, TTC).  
All rights reserved.

UMTS™ is a Trade Mark of ETSI registered for the benefit of its members  
3GPP™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners  
LTE™ is a Trade Mark of ETSI currently being registered for the benefit of its Members and of the 3GPP Organizational Partners  
GSM® and the GSM logo are registered and owned by the GSM Association

## --- Contents

|                                            |   |
|--------------------------------------------|---|
| Foreword .....                             | 3 |
| 1 Scope.....                               | 4 |
| 2 References.....                          | 4 |
| 3 (Void).....                              | 4 |
| 4 Drafting rules for Release 9 .....       | 4 |
| Annex K (informative): Change history..... | 5 |

---

# Foreword

This Technical Report has been produced by the 3<sup>rd</sup> Generation Partnership Project (3GPP) Secretariat on behalf of the 3GPP Technical Specification Groups (TSGs).

The contents of the present document are subject to continuing work within the TSG and may change following formal TSG approval. Should the TSG modify the contents of the present document, it will be re-released by the TSG with an identifying change of release date and an increase in version number as follows:

Version x.y.z

where:

- x the first digit:
  - 1 presented to TSG for information;
  - 2 presented to TSG for approval;
  - 3 or greater indicates TSG approved document under change control.
- y the second digit is incremented for all changes of substance, i.e. technical enhancements, corrections, updates, etc.
- z the third digit is incremented when editorial only changes have been incorporated in the document.

The present document is based ISO/IEC Directives. Most clauses of the ISO/IEC document have been retained, while some clauses have been modified or deleted. Additional material has been inserted.

Items concerning word-processor specific layout and formatting matters when using the Microsoft Word for Windows® based skeleton documents and templates are shown with shaded background. Boiler plate text (i.e. text which shall be directly used in 3GPP specifications) is represented by *italic* characters.

# --- 1 Scope

The present document specifies rules for the structure and drafting of documents intended to become a 3GPP Technical Specification or Technical Report. These rules are intended to ensure that such documents are drafted in as uniform a manner as is practicable, irrespective of the technical content.

The present document is based on the ISO/IEC Directives, Part 3, but is a self-contained document that will be maintained as such.

These drafting rules complement the 3GPP Working Procedures.

# --- 2 References

The following documents contain provisions which, through reference in this text, constitute provisions of the present document.

- References are either specific (identified by date of publication, edition number, version number, etc.) or non-specific.
- For a specific reference, subsequent revisions do not apply.
- For a non-specific reference, the latest version applies. In the case of a reference to a 3GPP document (including a GSM document), a non-specific reference implicitly refers to the latest version of that document *in the same Release as the present document*.

- [1] Void
- [2] Void
- [3] Void
- [4] 3GPP TR 21.801 Release 10: "Specification drafting rules".

# --- 3 (Void)

# 4 Drafting rules for Release 9

The drafting rules for Release 9 3GPP Technical Specifications and Technical Reports are identical to the rules for the next higher Release of TR 21.801 [4].

## Annex K (informative): Change history

| Change history |           |         |       |         |             |                                                                                 |
|----------------|-----------|---------|-------|---------|-------------|---------------------------------------------------------------------------------|
| TSG SA #       | TDoc      | Version | CR    | <Phase> | New Version | Subject/Comment                                                                 |
| 05-2000        |           |         | -     |         | 0.0.0       | First draft, internal to MCC.                                                   |
| 06-2000        |           | 0.0.0   | -     |         | 1.0.0       | Editorial clean up                                                              |
| SP-08          | SP-000278 | 1.0.0   | -     |         | 1.0.1       | Presentation to SA#8                                                            |
| SP-08          |           | 1.0.1   |       | Rel-4   | 4.0.0       | Approved (Rel-4)                                                                |
| SP-11          | SP-010193 | 4.0.0   | 001   | Rel-4   | 4.1.0       | Automatic numbering of references                                               |
| SP-11          | SP-010213 | 4.0.0   | 002r1 | Rel-4   | 4.1.0       | Clarification on use of automatically numbered figures, tables, etc.            |
| SP-13          | SP-010482 | 4.1.0   | 003   | Rel-4   | 4.2.0       | Corrections of invalid clause reference                                         |
| SP-15          | SP-020105 | 4.2.0   | 004   | Rel-4   | 4.3.0       | Correction of invalid table number, annex H.                                    |
| SP-16          |           | 4.3.0   |       | Rel-5   | 5.0.0       | Upgrade to Rel-5.                                                               |
|                |           | 5.0.0   |       | Rel-5   | 5.0.1       | 2002-07-19: Correct cover page.                                                 |
|                |           | 5.0.1   |       | Rel-5   | 5.0.2       | 2003-05-15: Correct cover page.                                                 |
| SP-23          |           | 5.0.2   |       | Rel-6   | 6.0.0       | Upgrade without change to Release 6                                             |
| SP-28          | SP-050401 | 6.0.0   | 009   | Rel-7   | 7.0.0       | The use of 'void'                                                               |
| SP-29          | SP-050535 | 7.0.0   | 013   | Rel-7   |             | Introduction of MS Visio                                                        |
|                |           |         | 014r1 |         | 7.1.0       | Specification of versions of permitted software packages                        |
| SP-30          | SP-050689 | 7.1.0   | 015   | Rel-7   | 7.2.0       | Inclusion of version identity for Visio                                         |
| SP-34          | SP-060914 | 7.2.0   | 017   | Rel-7   |             | Alignment of section 6.6.4.2 and annex I in respect of figure format.           |
|                |           |         |       |         | 7.3.0       |                                                                                 |
| SP-37          | SP-070527 | 7.3.0   | 018   | Rel-8   |             | Upgrade to Rel-8, allowing for more recent versions of application file formats |
|                |           |         |       |         | 8.0.0       |                                                                                 |
| SP-39          | SP-080078 | 8.0.0   | 020   | Rel-8   |             | Correction of illegal text                                                      |
|                |           |         | 021   |         | 8.1.0       | Elimination of IPR provisions                                                   |
| SP-46          |           | 8.1.0   |       | Rel-9   | 9.0.0       | Upgrade to Rel-9, no technical change                                           |
| SP-49          | SP-100655 | 9.0.0   | 027r1 | Rel-9   |             | Eliminate contents of Rel-9 and substitute with pointer to Rel-10               |
|                |           |         |       |         | 9.1.0       |                                                                                 |


<!-- ===== SOURCE FILE: raw__5_.md ===== -->



Keywords  
GSM, UMTS, LTE, methodology

# 3GPP TR 21.900 V9.1.0 (2011-06)

*Technical Report*

**3GPP**

Postal address

## **3rd Generation Partnership Project; Technical Specification Group Services and System Aspects; ~~Technical Specification Group working methods~~**

3GPP support office address

0550 Route des Lucioles - Sophia Antipolis

Valbonne - FRANCE

Tel.: +33 4 92 94 42 00 Fax: +33 4 93 65 47 16

**(Release 9)**  
**3GPP™**

Internet

<http://www.3gpp.org>

![LTE logo](8740e63f5546e4004e600f24d883acba_img.jpg)

The LTE logo features the lowercase letters 'lte' in a bold, sans-serif font. Above the 'l' and 't' are three red curved lines representing signal waves. A small 'TM' trademark symbol is located to the right of the 'e'.

LTE logo

The present document has been developed within the 3<sup>rd</sup> Generation Partnership Project (3GPP™) and may be further elaborated for the purposes of 3GPP.

The present document has not been subject to any approval process by the 3GPP Organisational Partners and shall not be implemented.  
This Specification is provided for future development work within 3GPP only. The Organisational Partners accept no liability for any use of this Specification.  
Specifications and reports for implementation of the 3GPP™ system should be obtained via the 3GPP Organisational Partners' Publications Offices.

## ***Copyright Notification***

No part may be reproduced except as authorized by written permission.  
The copyright and the foregoing restriction extend to reproduction in all media.

© 2011, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TTA, TTC).  
All rights reserved.

UMTSTM is a Trade Mark of ETSI registered for the benefit of its members  
3GPP™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners  
LTE™ is a Trade Mark of ETSI currently being registered for the benefit of its Members and of the 3GPP Organizational Partners  
GSM® and the GSM logo are registered and owned by the GSM Association

# Contents

|                              |   |
|------------------------------|---|
| Foreword .....               | 4 |
| Introduction .....           | 4 |
| 1 Scope.....                 | 5 |
| 1A References.....           | 5 |
| Annex A: Change history..... | 6 |

# --- Foreword

This Technical Specification has been produced by the 3<sup>rd</sup> Generation Partnership Project (3GPP).

The contents of the present document are subject to continuing work within the TSG and may change following formal TSG approval. Should the TSG modify the contents of the present document, it will be re-released by the TSG with an identifying change of release date and an increase in version number as follows:

Version x.y.z

where:

- x the first digit:
  - 1 presented to TSG for information;
  - 2 presented to TSG for approval;
  - 3 or greater indicates TSG approved document under change control.
- y the second digit is incremented for all changes of substance, i.e. technical enhancements, corrections, updates, etc.
- z the third digit is incremented when editorial only changes have been incorporated in the document.

# --- Introduction

In order to ensure correctness and consistency of the specifications (i.e., technical specifications and technical reports) under responsibility of the Technical Specification Groups (TSG) of the 3<sup>rd</sup> Generation Partnership Project (3GPP), clear, manageable and efficient mechanisms are necessary to handle version control, change control, document updating, distribution and management.

Also, the fact that the specifications are/will be implemented by industry almost in parallel with the writing of them requires strict and fast procedures for handling of changes to the specifications.

It is very important that the changes that are brought into the standard, from the past, at present and in the future, are well documented and controlled, so that technical consistency and backwards tracing are ensured.

The 3GPP TSGs, and their sub-groups together with the Support Team are responsible for the technical content and consistency of the specifications whilst the Support Team alone is responsible for the proper management of the entire documentation, including specifications, meeting documents, administrative information and information exchange with other bodies.

# --- 1 Scope

This document outlines the working methods to be used by the 3GPP Technical Specification Groups and their Working Groups and their Sub-Groups, and by the 3GPP Support Team in relation to document management.

The provisions for this Release are identical with those for the latest Release of TR 21.900 [1].

# --- 1A References

The following documents contain provisions which, through reference in this text, constitute provisions of the present document.

- References are either specific (identified by date of publication, edition number, version number, etc.) or non-specific.
- For a specific reference, subsequent revisions do not apply.
- For a non-specific reference, the latest version applies. In the case of a reference to a 3GPP document (including a GSM document), a non-specific reference implicitly refers to the latest version of that document *in the same Release as the present document*.

[1] 3GPP TR 21.900 Release 10: "Technical Specification Group working methods".

# Annex A: Change history

| Change history |         |           |           |             |                                                                                                                                                                                                            |
|----------------|---------|-----------|-----------|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TSG SA#        | Version | CR        | Tdoc SA   | New Version | Subject/Comment                                                                                                                                                                                            |
| SP-04          | 3.0.0   | 001       | SP-99288  | 3.1.0       | Alignment with TSG SA decisions made at TSG#3. Deletion of Strategic/non strategic CR references. Change of PT to Support Team, editorial corrections.                                                     |
|                |         | 002       | SP-99289  |             | Harmonisation of the use of software for 3GPP documents in order to minimise the errors due to software conversion problems and to allow efficient interchange of electronic files for electronic working. |
| SP-05          | 3.1.0   | 003       | SP-99428  | 3.2.0       | Addition of new text related to electronic working practices.                                                                                                                                              |
| SP-08          | 3.2.0   | 005       | SP-000279 | 3.3.0       | Clarification and editorial corrections to provisions covering the management of specifications and Work Items.                                                                                            |
| SP-09          | 3.3.0   | 007 r1    | SP-000402 | 3.4.0       | Role of rapporteur for both Specifications and Work Items.                                                                                                                                                 |
|                |         | 008 r2    | SP-000492 |             | Clarification of CR categories.                                                                                                                                                                            |
|                |         | 010       | SP-000461 |             | Clarification of CR categories for a frozen 3GPP release.                                                                                                                                                  |
|                |         | editorial |           |             | Change of "Release 2000" into "Release 4", addition of "Release 5".                                                                                                                                        |
| SP-10          | 3.4.0   | 011 r1    | SP-000693 | 3.5.0       | Release numbers appearing in CR cover sheets                                                                                                                                                               |
|                | 3.4.0   | 012 r1    | SP-000693 |             | Clarification of the "freezing" of specifications                                                                                                                                                          |
|                | 3.4.0   | 013 r2    | SP-000693 |             | Release mechanisms                                                                                                                                                                                         |
| SP-11          | 3.5.0   | 014 r1    | SP-010178 | 3.6.0       | Inclusion of GSM spec numbering scheme                                                                                                                                                                     |
|                | 3.6.0   | -         | -         | 4.0.0       | Upgrade to Rel-4.                                                                                                                                                                                          |
| SP-16          | 4.0.0   | -         | -         | 5.0.0       | Upgrade to Rel-5.                                                                                                                                                                                          |
| 2002-09-17     | 5.0.0   | -         | -         | 5.0.1       | Editorial correction to front cover (change title to read Release 5 instead of Release 4)                                                                                                                  |
| SP-21          | 5.0.1   | 015       | SP-030499 | 6.0.0       | Addition of stage 1-2-3 specification structure description                                                                                                                                                |
| SP-22          | 6.0.0   | 019       | SP-030575 | 6.1.0       | Corrects references                                                                                                                                                                                        |
| SP-23          | 6.1.0   | -         | -         | 6.1.1       | Corrects Release shown on cover page                                                                                                                                                                       |
| SP-24          | 6.1.1   | 020       | SP-040310 | 6.2.0       | Release planning: target date setting                                                                                                                                                                      |
|                |         | -         | -         |             | Editorial: Correction of second clause 6.0.2 to 6.0.3.                                                                                                                                                     |
| SP-25          | 6.2.0   | 021 r3    | SP-040705 | 6.3.0       | Introduction of "Early Implementation" process                                                                                                                                                             |
|                |         | 024       | SP-040706 |             | Improved tracking of Work Item status                                                                                                                                                                      |
| SP-26          | 6.3.0   | 025       | SP-040824 | 7.0.0       | Editorial clarification of version numbering system, upgrade to Rel-7                                                                                                                                      |
| SP-28          | 7.0.0   |           |           | 7.0.1       | Editorial corrections to harmonize use of capitalization plus a typographical error                                                                                                                        |
| SP-29          | 7.0.1   | 028       | SP-050537 | 7.1.0       | Introduction of the concept of "study item"                                                                                                                                                                |
| SP-32          | 7.1.0   | 029       | SP-060403 | 7.2.0       | Inclusion of "study item" in definition of "work item"                                                                                                                                                     |
|                |         | 030       |           |             | Change "short" to "long" WG abbreviations                                                                                                                                                                  |
|                |         | 031 r1    |           |             | Correct references to obsolete TSG.                                                                                                                                                                        |
|                |         | 032       |           |             | Registration of code points with external bodies                                                                                                                                                           |
| SP-37          | 7.2.0   | 034 r2    | SP-070703 | 8.0.0       | Alignment of working methods with alignment CR practice agreed in TSG SA #36                                                                                                                               |
| SP-38          | 8.0.0   | 035       | SP-070900 | 8.1.0       | Addition of 36.-series to Specs series table                                                                                                                                                               |
|                | 8.1.0   |           |           | 8.1.1       | Correct typo in previous entry in history table                                                                                                                                                            |
| SP-39          | 8.1.1   | 036 r2    | SP-080079 | 8.2.0       | Clarification of version nomenclature                                                                                                                                                                      |
| SP-42          | 8.2.0   | 037 r3    | SP-080897 | 8.3.0       | Determination of freeze dates for stages of a Release. (Correction recommended by OP ad hoc group on improvements.)                                                                                        |
|                |         | 038 r1    | SP-080721 |             | Cross-TSG work coordination. (Correction recommended by OP ad hoc group on improvements.)                                                                                                                  |
|                |         | 039 r2    |           |             | Introduction of concept of "exception sheets" for late-running work items                                                                                                                                  |
| SP-46          | 8.3.0   |           |           | 9.0.0       | Upgrade without technical change to Rel-9                                                                                                                                                                  |
| SP-52          | 9.0.0   | 0044      | SP-110297 | 9.1.0       | Eliminate contents of Rel-9 and substitute with pointer to Rel-10                                                                                                                                          |




<!-- ===== SOURCE FILE: raw__6_.md ===== -->



# 3rd Generation Partnership Project; **3GPP TR 21.902** Technical Specification Group Services and System Aspects (2009-12) **Evolution of 3GPP system;** *Technical Report* **(Release 9)** ---

![3GPP logo with TM symbol](935eed7aa61f7777f62cfc032e11bee9_img.jpg)

The 3GPP logo, featuring the letters '3GPP' in a stylized, bold font. The '3' is black, 'G' is black, 'P' is black, and 'P' is black. There is a small red signal icon below the 'G'. A 'TM' symbol is located to the top right of the 'P'.

3GPP logo with TM symbol

The present document has been developed within the 3<sup>rd</sup> Generation Partnership Project (3GPP™) and may be further elaborated for the purposes of 3GPP.

The present document has not been subject to any approval process by the 3GPP Organizational Partners and shall not be implemented.

This Specification is provided for future development work within 3GPP only. The Organizational Partners accept no liability for any use of this Specification.

Specifications and reports for implementation of the 3GPP™ system should be obtained via the 3GPP Organizational Partners' Publications Offices.

Keywords  
3GPP, Evolution

## **3GPP**

Postal address

---

3GPP support office address

---

650 Route des Lucioles - Sophia Antipolis  
Valbonne - FRANCE  
Tel.: +33 4 92 94 42 00 Fax: +33 4 93 65 47 16

Internet

---

<http://www.3gpp.org>

## ***Copyright Notification***

No part may be reproduced except as authorized by written permission.  
The copyright and the foregoing restriction extend to reproduction in all media.

© 2009, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TTA, TTC).  
All rights reserved.

UMTS™ is a Trade Mark of ETSI registered for the benefit of its members  
3GPP™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners  
LTE™ is a Trade Mark of ETSI currently being registered for the benefit of its Members and of the 3GPP Organizational Partners  
GSM® and the GSM logo are registered and owned by the GSM Association

# --- Contents

|                                                            |    |
|------------------------------------------------------------|----|
| Foreword .....                                             | 4  |
| Introduction .....                                         | 4  |
| 1 Scope.....                                               | 5  |
| 2 References.....                                          | 5  |
| 3 Definitions and abbreviations .....                      | 5  |
| 3.1 Definitions.....                                       | 5  |
| 3.2 Abbreviations .....                                    | 5  |
| 4 The current scope of 3GPP and its Releases.....          | 6  |
| 4.1 3GPP Releases.....                                     | 6  |
| 4.1.1 3GPP Release 1999 .....                              | 7  |
| 4.1.2 3GPP Release 4 .....                                 | 7  |
| 4.1.3 3GPP Release 5 .....                                 | 7  |
| 4.1.4 3GPP Releases 6.....                                 | 7  |
| 4.1.5 Future 3GPP Releases .....                           | 7  |
| 4.2 Interactions with other industry fora .....            | 7  |
| 4.2.1 Internet Engineering Task Force (IETF) .....         | 7  |
| 4.2.2 Open Mobile Alliance (OMA) .....                     | 8  |
| 5 Focus areas and Stakeholder expectations .....           | 9  |
| 6 Technology Evolution.....                                | 10 |
| 6.1 Statements and Assumptions.....                        | 10 |
| 6.2 3G Enhancements (short to medium term evolution) ..... | 10 |
| 6.2.1 Radio access network technology .....                | 10 |
| 6.2.2 Core Network .....                                   | 11 |
| 6.2.3 Service Provision.....                               | 11 |
| 6.2.4 Operations Support Systems.....                      | 12 |
| 6.2.5 User Equipment .....                                 | 12 |
| 6.2.6 Smartcards .....                                     | 13 |
| 6.2.7 Security .....                                       | 13 |
| 6.3 3G Long Term Evolution .....                           | 13 |
| 6.3.1 Radio access network technology .....                | 13 |
| 6.3.2 Core network .....                                   | 14 |
| 6.3.3 Smart Cards .....                                    | 14 |
| 6.3.4 Architecture Evolution .....                         | 14 |
| 7 Other influences .....                                   | 15 |
| 7.1 Regulatory issues.....                                 | 15 |
| 7.2 Spectrum.....                                          | 15 |
| Annex A: Change history.....                               | 16 |

# --- Foreword

This Technical Report has been produced by the 3<sup>rd</sup> Generation Partnership Project (3GPP).

The contents of the present document are subject to continuing work within the TSG and may change following formal TSG approval. Should the TSG modify the contents of the present document, it will be re-released by the TSG with an identifying change of release date and an increase in version number as follows:

Version x.y.z

where:

- x the first digit:
  - 1 presented to TSG for information;
  - 2 presented to TSG for approval;
  - 3 or greater indicates TSG approved document under change control.
- y the second digit is incremented for all changes of substance, i.e. technical enhancements, corrections, updates, etc.
- z the third digit is incremented when editorial only changes have been incorporated in the document.

# --- Introduction

At a time when the first release of the 3GPP 3G standard has stabilised, and the first 3GPP compliant networks are going live, the ITU is already working towards elaborating a framework for the future development of IMT-2000 and systems beyond IMT-2000. In addition, a number of research initiatives worldwide are investigating technologies and techniques that might fall within that framework. It is therefore timely, that 3GPP look at how its systems will evolve in the future to meet the requirements of the user and the industry, and to make use of emerging technologies.

# --- 1 Scope

The present document describes a long term, high level roadmap, intended to guide the future work of 3GPP. It is focussed on items pertinent to the evolution of 3GPP specifications, and identifies concepts and trends to be considered by 3GPP when defining future work items. It does not contain details of proposed technologies, rather it contains pointers to direct the activities of the appropriate TSGs in elaborating future releases of the 3GPP standard. As a result, not all of the topics covered herein are within the remit of 3GPP to discuss, and description of such items will not be extensively developed. E.g. Spectrum is an ITU-R/WRC issue and therefore outside the scope of 3GPP. The document is designed to be a "living document" and will be updated accordingly over its lifetime in order to reflect future developments and innovations.

# --- 2 References

The following documents contain provisions which, through reference in this text, constitute provisions of the present document.

- References are either specific (identified by date of publication, edition number, version number, etc.) or non-specific.
- For a specific reference, subsequent revisions do not apply.
- For a non-specific reference, the latest version applies. In the case of a reference to a 3GPP document (including a GSM document), a non-specific reference implicitly refers to the latest version of that document *in the same Release as the present document*.

[1] 3GPP TR 21.905: "Vocabulary for 3GPP Specifications".

# --- 3 Definitions and abbreviations

## 3.1 Definitions

For the purposes of the present document, the terms and definitions given in [1] apply.

## 3.2 Abbreviations

For the purposes of the present document, the following abbreviations apply:

|     |                                     |
|-----|-------------------------------------|
| LIF | Location Interoperability Forum     |
| WAP | Wireless Application Protocol       |
| WRC | World Radiocommunication Conference |

# --- 4 The current scope of 3GPP and its Releases

## 4.1 3GPP Releases

The current scope of 3<sup>rd</sup> Generation Partnership Project (3GPP) is to produce globally applicable Technical Specifications (TSs) and Technical Reports (TRs) for:

- a 3<sup>rd</sup> Generation Mobile System based on evolved GSM core networks and the radio access technologies that they support (i.e., Universal Terrestrial Radio Access (UTRA) both Frequency Division Duplex (FDD) and Time Duplex (TDD) modes); and
- the Global System for Mobile communication (GSM) including evolved radio access technologies (e.g. General Packet Radio Service (GPRS) and Enhanced Data rates for GSM Evolution (EDGE)).

In addition, 3GPP shall consider the long term evolution of its systems.

The 3<sup>rd</sup> Generation Mobile System and the Global System for Mobile communication (GSM) and their capabilities are developed in a phased approach. In the following the content of the 3GPP Releases is briefly outlined.

![Figure 1: 3GPP Releases for enhancements/improvements of the 3GPP Mobile Network. A graph showing Functionality on the Y-axis and Time on the X-axis. The graph shows a solid line representing the initial release, followed by a dashed line representing subsequent releases. Four releases are marked: Release 1999, Release 4, Release 5, and Release n. The X-axis has markers for 1999-12, 2001-03, and 2002-03/06.](ac99eff233b8fe51d30f499e7413c345_img.jpg)

The figure is a line graph illustrating the progression of 3GPP releases over time. The vertical axis is labeled 'Functionality' and the horizontal axis is labeled 'Time'. A solid line starts at the origin and rises linearly. Four rectangular boxes, each containing a release name, are positioned below the line, with a downward-pointing arrow from each box to the line. The releases are 'Release 1999', 'Release 4', 'Release 5', and 'Release n'. The 'Release 1999' box is at the lowest point on the line, followed by 'Release 4', then 'Release 5', and finally 'Release n' at the highest point. The line becomes dashed after 'Release 5', indicating future releases. The X-axis has tick marks and labels for '1999-12', '2001-03', and '2002-03/06'.

Figure 1: 3GPP Releases for enhancements/improvements of the 3GPP Mobile Network. A graph showing Functionality on the Y-axis and Time on the X-axis. The graph shows a solid line representing the initial release, followed by a dashed line representing subsequent releases. Four releases are marked: Release 1999, Release 4, Release 5, and Release n. The X-axis has markers for 1999-12, 2001-03, and 2002-03/06.

**Figure 1: 3GPP Releases for enhancements/improvements of the 3GPP Mobile Network**

### 4.1.1 3GPP Release 1999

3GPP Release 1999 is the first release from 3GPP and covers specifications for a complete mobile system. 3GPP Release 1999 contains, but is not limited to, UTRA FDD and 3.84 Mcps TDD modes, UTRAN Iu, Iub and Iur interfaces, GSM based evolved core network, USIM, AMR speech codec, Multimedia Messaging Service (MMS), Location Services (LCS), a broad range of supplementary services, Customized Applications for Mobile network Enhanced Logic (CAMEL); Open Service Access (OSA) and telecommunication management.

The 3GPP Release 1999 was functionally frozen in December 1999.

### 4.1.2 3GPP Release 4

3GPP Release 4 is a further enhancement of 3GPP Release 1999.

3GPP Release 4 contains, but is not limited to, UTRA FDD repeater function, low chip rate TDD option, 700 MHz support for GERAN, e2e transparent packet streaming service, Tandem Free Operation, Transcoder Free Operation, IP transport of CN protocols, bearer independent CS core network, CAMEL enhancements and OSA enhancements.

The 3GPP Release 4 was functionally frozen in March 2001.

### 4.1.3 3GPP Release 5

3GPP Release 5 is a further enhancement of the previous releases.

3GPP Release 5 contains, but is not limited to, the initial phase of the IP Multimedia Subsystem (IMS), High Speed Downlink Packet Access (HSDPA), UMTS in 1800/1900 MHz bands (release independent), Wideband AMR, IP transport in the UTRAN, Iu for GERAN, Gb over IP, CAMEL enhancements, OSA enhancement, Global Text Telephony (this is a Release independent Feature, not a Rel-5 Feature), Location Services enhancements, UTRAN sharing in connected mode and security enhancements.

The 3GPP Release 5 was functionally frozen in March 2002 and the remaining part in June 2002.

### 4.1.4 3GPP Releases 6

Work is currently ongoing for 3GPP Release 6. It is planned that 3GPP Release 6 will contain, but will not be limited to: Multimedia Broadcast/Multicast Service (MBMS), Network Sharing, Priority Service, Wireless LAN/UMTS Interworking, IMS Phase 2, Push Services and Presence.

### 4.1.5 Future 3GPP Releases

The present document addresses the evolutionary aspects of subsequent 3GPP Releases.

## 4.2 Interactions with other industry fora

### 4.2.1 Internet Engineering Task Force (IETF)

As a result of the introduction of the IP Multimedia CN Subsystem, the dependence on IETF RFCs has significantly increased, with 3GPP defining requirements that impact the IETF work. The relationship with IETF is moving away from one where 3GPP simply adopts the protocols as applicable (as was the case in Release 1999 and Rel-4), with 3GPP actively participating in the develop of the protocols for Release 5 and in the case of Release 6 defining the system requirements, from which the protocol requirements can be determined and passed to IETF to provide the solution. To coordinate that work, 3GPP has put in place the following:

- an IETF Liaison Rapporteur to work with the officials of IETF;
- tracks the dependencies on work in IETF through the 3GPP Work Plan;
- provides 3GPP requirements drafts into IETF through contributions from individuals.

### 4.2.2 Open Mobile Alliance (OMA)

OMA is a new industry forum, which is working on service enablers for mobile systems. The working relationship between 3GPP and OMA is still being developed. Currently, 3GPP is dependent upon work within OMA that was formerly being done with fora such as WAP and LIF. In this case, the requirements have been defined by 3GPP and the protocols are being defined by OMA e.g. for LCS and MMS.

In the future there is the possibility that OMA will be defining service enablers that 3GPP will need to:

- provide interworking to;
- provide network capabilities to support the service.

# 5 Focus areas and Stakeholder expectations

A number of drivers have been identified for the evolution of the 3GPP system. These drivers can be categorised as expectations coming from a number of different "Stakeholders", in that each Stakeholder has its own expectations of what evolution will deliver. Table 1 gives a summary of the stakeholders and their expectations. They have been grouped under focus areas. Some drivers appear under more than one focus area. It is recognised that new services/functions shall provide new streams of revenue.

**Table 1: Mapping of Stakeholder expectations to Focus Areas**

| Focus Area                                                                                                                                                             | End User Expectations                                                                                                                                                                                                                     | Network Operators Expectations                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Manufacturer/Application Developer Expectations                                                                                                                                                                                                                           |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Ubiquitous access for a core set of services, delivering IP based services at moderate data rates (hundreds of kb/s) over the widest possible proportion of the world. | Ubiquitous mobile access<br>Appropriate quality at reasonable cost (including terminal cost)<br>Easily understandable user interface.                                                                                                     | Reduced cost of terminals and network equipment based on global economies of scale.<br>Need to reduce cost of network ownership and ongoing operations.<br>QoS and Security management.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Access to a global market                                                                                                                                                                                                                                                 |
| Flexibility in services provision; including charging, ease of use.                                                                                                    | Easy access to applications and services<br>Inter-Operability of services between diverse systems independent of access technology<br>Easily understandable user interface<br>Large choice of terminals<br>Enhanced service capabilities. | Ability to provide differentiated services;<br>Flexible charging;<br>Ad hoc networking integration shall allow the full operator control of all the nodes involved<br>Mobile nodes should request and obtain operator's authorisation for every service requiring the usage of radio or network resources.                                                                                                                                                                                                                                                                                                                                                                                                        |                                                                                                                                                                                                                                                                           |
| Cost containment; relates to cost savings as seen by each stakeholder.                                                                                                 | Appropriate quality at reasonable cost<br>Long equipment and battery life.<br><br>User friendly charging capabilities.                                                                                                                    | Optimisation of resources (spectrum and equipment).<br>Flexibility in the network configuration;<br>Access type selection optimising service delivery;<br>Reduced cost of terminals and network equipment based on global economies of scale.<br>Need to reduce cost of network ownership and ongoing operations.<br>Maximized usage and sharing capabilities between 3GPP systems and systems beyond 3G (sharing of terminal, USIM, network elements, radio sites).<br>Limit number of options in order to ease deployment and network configuration for multi-vendor infrastructure, handsets and roaming. Need a standardized set of OAM&P (Operations, Administration, Management & Provisioning) interfaces. | Reduced cost of terminals and network equipment based on global economies of scale.<br>Access to a global market.<br>Open physical and logical interfaces between modular and integrated subsystems.<br>Programmable platforms that enable fast and low cost development. |
| Security related issues of services; including all aspects related to the protection of information, fraud prevention etc.                                             | Availability of a trusted environment (Security of identity, personal data and "conversations").                                                                                                                                          | Single authentication (independent of the access network).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |                                                                                                                                                                                                                                                                           |
| Performance.                                                                                                                                                           | Enhanced service capabilities<br>Improved system performance in terms of responsiveness and reduced delay in sending/receiving data.                                                                                                      | Optimisation of resources (spectrum and equipment).<br>Trusted environment based on USIM/UICC.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                           |

# --- 6 Technology Evolution

## 6.1 Statements and Assumptions

A number of basic assumptions are made for this high level roadmap as follows:

- future is evolution not revolution;
- where possible, existing techniques/technologies should be re-used (potentially through co-operation with external fora);
- requirements setting should be improved, e.g. by including commercial considerations;
- three horizontal layers are applied in 3GPP architecture definition: access/connectivity layer, service enablers layer, and applications/services layer;
- the 3GPP architecture separates user, control and management related information flows into their own planes;
- the description of the 3GPP System Future Evolution is split in two parts:
  - 3G Enhancements (short to medium term evolution);
  - 3G Long Term Evolution;
- different domains and layers of the system may evolve at different paces, partly due to the pace of technical development within the domain, and partly due to regulatory windows of opportunity, such as, WRC-07. This means that specification work on Short/medium and long term capabilities will overlap. As a general rule, the borderline between short/medium term and long-term evolution is in approximately 4-5 years time (around 2007-2008), for the availability of the specifications. Hence, some of the long term specifications may be available close to this borderline and before all the specifications for the short/medium term are complete.

In considering the future evolution of the 3GPP system it is further recommended that:

- the layered architecture model allows rapid development of new applications and services, but allows also the integration of new radio and network technologies on the access/connectivity layer;
- decoupling between horizontal layers is adopted as a design principle;
- access technology specificities are considered and taken into account when justified by application and system performance gains;
- 3GPP should also in the future define clear interfaces between different subsystems of the 3GPP system to facilitate development of each subsystem according to its evolution phase;
- mechanisms to manage the provision of third-party services over decoupled networks are introduced.

## 6.2 3G Enhancements (short to medium term evolution)

The Short/Medium Term phase of the evolution is marked by the fact that the requirements for many of the changes are known today. Hence, it is easier to be more specific on what enhancements may be made to the 3GPP system.

### 6.2.1 Radio access network technology

Short to medium term evolution of 3G radio access should aim for improved radio performance, support for better UE performance, and optimisation of radio access network architecture. Improvements to radio performance include:

- higher spectral efficiency;
- improved coverage;
- radio protocol optimisation for shorter radio access latencies (both call set up and round-trip-time).

Further improvements of RAN performance (radio performance, RAN architecture) spectral contribute to lower costs of service delivery. For best effort type of traffic at least two times the cellular throughput of HSDPA (Rel-5) should be achieved. Important techniques to be considered are e.g. multi-antenna both in Node B and UE (multi-streaming and diversity) and efficient utilisation of multicast/broadcast solutions. In addition for better user experience higher bit rates in the order several hundreds of kbps for dozens of users per cell should be possible in wide area deployments.

Radio protocol optimisation should take into account the overall end-to-end performance requirements as seen by the end-user. Of particular importance is the delay contribution of radio access for delay/response sensitive services like interactive gaming.

Techniques that enhance the UE performance especially in terms of power consumption should be targeted for. This may involve e.g. higher peak data (in the order of 20-30 Mbps) rates.

Joint utilisation of 3G cellular and alternative access technologies (e.g. WLAN) creates a multi-radio concept which potentially can improve the user experience e.g. in terms of increased capacity and very fast local access. Radio access solutions that enable low cost/power efficient multi-radio implementations and improved overall performance (data rate, spectral efficiency, capacity, delay) should be studied.

Radio access network architecture should be further optimised especially for packet data communication. This would improve the efficiency of the network and also lower the involved implementation costs.

### 6.2.2 Core Network

The following enhancements to the 3GPP core network system are considered to be realisable in the short to medium term:

- a Harmonized IMS between 3GPP and 3GPP2:
  - a Harmonized IMS is highly desirable for operators to provide the opportunity of service transparency, seamless roaming and common application across all evolving IMT-2000 systems;
  - a single IMS reference model should be adopted and consistent terminology used to describe common IMS functional entities;
  - 3GPP and 3GPP2 should work to ensure interoperability between the 3GPP IMS terminals and 3GPP2 MMD terminals (a 3GPP IMS terminal can set up a session with a 3GPP2 MMD terminal and vice-versa);
  - application level intersystem IMS roaming should be supported. A 3GPP IMS terminal supporting the visited network's access network, IP transport technology and IMS discovery mechanisms, should be able to roam into a 3GPP2 network and use the capabilities of visited P-CSCF to access home IMS and vice-versa);
- service expandability and application service support;
- security support;
- further optimisation, especially for packet data communication, of the core and radio access network architectures to improve the efficiency of the network and also lower the involved implementation costs.

In addition, it is expected that short to medium term enhancements will improve system flexibility, scalability, interoperability and robustness.

### 6.2.3 Service Provision

A number of short to medium term enhancements have been identified from the service provision perspective. These include:

- the establishment of flexible charging capabilities;
- access to a very large market through a high similarity of application programming interfaces;
- fast, open service creation, validation and provisioning;
- enhanced QoS and security management;
- Service Portability – Global Roaming;

- the ability to monitor and measure Service Level Agreements on End to End Basis;
- the ability to adapt content to user requirements depending on terminal, location and user preferences;
- automatic service adaptation as a function of available data rate and type of terminal;
- the definition of enhanced APIs:
  - generic APIs which allow application creation. The APIs should include interface with underlying QoS capabilities;
  - a simple IMS interface towards external networks;
  - APIs for Application delivery;
- Seamless Service Provision & Service Interworking:
  - from the user access perspective;
  - across different environments;
- Service harmonization( or interoperability):
  - as varieties of application services are expected to explode every year, seamless application interoperability will be the key factors to satisfy users. It is undoubted that service interoperability can be fully supported on the common service platform but, 3GPP and other external bodies have their own services which already almost completed their technical works;
  - 3GPP should focus on developing common service platform and providing service interoperability for the work already being done, such as MMS service between 3GPP and 3GPP2.

### 6.2.4 Operations Support Systems

The following enhancements to Operation Support Systems are considered to be realisable in the short to medium term:

- improved OAM&P (Operations, Administration, Maintenance, & Provisioning) and customer care possibilities;
- the definition of a standardized set of OAM&P interfaces to simplify operations and optimise costs;
- the exploitation of inherent network functions such as security, authentication, charging, etc.
- the inclusion of requirements from new functions.

In addition, it is expected that short to medium term enhancements will result in improved charging, security and testing.

### 6.2.5 User Equipment

The following are seen as enhancements from the User Equipment perspective, that will appear in the short to medium term:

- more easily understandable user interfaces;
- increased equipment and battery life;
- increased standby and activity times;
- larger choice of terminal models and terminal types;
- support of secure download of applications to the UE.

### 6.2.6 Smartcards

In the short to medium term it is expected that enhancements will appear that enable:

- support of secure download of UICC applications;

- establishment of the UICC as a cornerstone for all kind of trusted relationships (e.g. via powerful crypto processors);
  - support of the UICC as secure token for e.g. keys generation, rights management, e-signature, biometric identification, etc.
- advanced high-speed communication protocols for the terminal  $\leftrightarrow$  UICC interface;
- support of the UICC as a secure repository of personal data, due to the increasing size of the available memory on the UICC (from Megabytes and above);
- support of the enhanced set of USAT commands to increase the interaction with the terminal and different applications on the same UICC.

### 6.2.7 Security

In the short to medium term advances in security are expected that will:

- enable re-use of 3G based USIM/UICC centric identification and authentication for roaming between 3GPP and non-3GPP based networks by providing adequate means to non 3GPP networks to make use of 3GPP Security mechanisms;
- establishment of the USIM/UICC centric 3GPP security mechanisms as a cornerstone for all kind of trusted relationships;
- introduce the necessary state of the art protection mechanism needed to cope with the increased threats due to overall IP-based network and terminal connectivity.

## 6.3 3G Long Term Evolution

The Long Term Evolution is somewhat blurry and is marked by *visions* of what the future wireless networks should evolve into. The 3GPP Long Term vision is still a little hazy, as are other visions, and will gradually come into focus through a careful study of market trends, understanding of future user requirements and the availability of new network and wireless access technologies. Thus, only the outline of the proposed 3GPP Long Term evolution is presented.

### 6.3.1 Radio access network technology

In long term, the performance improvements (spectral efficiency, higher bit rates, shorter delays) of 3GPP radio access should be continued. Long term target peak data rates are:

- up to 100 Mbps in full mobility, wide area deployments;
- up to 1 Gbps in low mobility, local area deployments.

The long term spectral efficiency targets are (for best effort packet communication):

- in a single (isolated) cell, up to 5-10 bps/Hz;
- in a multi-cellular case, up to 2-3 bps/Hz.

Reaching the peak data rate targets may take place by gradual evolution of existing 3GPP (UTRAN) and alternate access means (e.g. WLAN), but also new access techniques should be considered according to the availability of additional or re-allocated spectrum, as defined by WRC.

### 6.3.2 Core network

The following reflect a vision of longer evolution of the 3GPP core network system:

- a seamless integrated network comprising a variety of networking access systems connected to a common IP based network supported by a centralised mobility manager;
- a broadband and multiple bearer service capability;
- interworking between 3GPP Mobile Network and other Networks:

- a similarity of services and applications across the different systems is beneficial to users, and this has stimulated the current trend towards convergence. In the future operators may complement their cellular networks with a mix of technologies that could incorporate WLAN, digital broadcast, satellite and other access systems. This will require the seamless interaction of these systems in order for the user to be able to receive a variety of content via a variety of delivery mechanisms depending upon the particular terminal capabilities, location and user profile;
- different radio access systems will be connected via flexible core networks. In this way, an individual user can be connected via a variety of different access systems to the networks and services he desires;
- 3GPP should focus on the interworking between 3GPP Mobile Networks and other Networks considering mobility, high security (identification, authentication, ciphering, lawful interception), charging and QoS management;
- examples of other networks may include ad hoc networks, home networks, device networks and sensor networks etc.
- ad hoc networking approach:
  - as a means of increasing overall flexibility of their network, 3GPP operators may want their 3GPP networks to interwork with ad hoc networks;
  - depending on the progress and deployment of ad hoc networks, the 3GPP organisation should pursue interworking between 3GPP networks and ad hoc networks using the approach taken to develop interworking between 3GPP networks and WLANs (i.e. consideration needs to be taken for management of identification, authentication, security, charging, network resources (e.g. QoS), regulatory aspects, etc.);
  - one of the potential benefits of the Ad Hoc Networking approach is e.g. self-configuration, self-balancing and self-healing capabilities which may have applicability to 3GPP networks;
  - ad-hoc networking research and development is currently quite active though there is not now a clear consensus on definition, scope, or architecture principles.

NOTE: The role of ad-hoc networks and their implications needs to be defined.

### 6.3.3 Smart Cards

In the longer term Smart Cards will be available that support data streaming enabling services based on the ciphering / deciphering of encrypted data using a new enhanced interface protocol.

### 6.3.4 Architecture Evolution

In the long term evolution of 3G network architecture intrinsic resilience shall be a guiding principle.

The evolution goals shall be:

- achieve a lower cost of ownership by providing "Carrier Grade Reliability" without requiring the use of high reliability platforms;
- provide a fault tolerant network by means of the 3GPP defined architecture;
- provide enhanced scalability of network nodes by means of the 3GPP defined architecture.

NOTE: This does not preclude the further future use of high reliability platforms.

# --- 7 Other influences

## 7.1 Regulatory issues

Following established 3GPP practice, regional regulatory requirements that affect the work of 3GPP shall be taken into account. The assessment of each of these requirements as being optional or mandatory needs to be carried out case by case. Requirements relevant to one region should not unduly affect the implementation in other regions.

## 7.2 Spectrum

Spectrum is an ITU-R/WRC issue and outside the scope of 3GPP. However, 3GPP should consider technologies that make new and innovative use of spectrum, whilst future standards should include provision for equipment to be able to operate in all frequency bands over a global harmonized frequency range.

# --- Annex A: Change history

| Change history |       |           |    |     |                                       |       |       |
|----------------|-------|-----------|----|-----|---------------------------------------|-------|-------|
| Date           | TSG # | TSG Doc.  | CR | Rev | Subject/Comment                       | Old   | New   |
| 2003-09        | SP-21 | SP-030518 | -  | -   | Approved at TSG SA meeting #21        | 2.0.0 | 6.0.0 |
| 2007-06        | SP-36 |           |    |     | Upgrade to Rel-7, no technical change | 6.0.0 | 7.0.0 |
| 2008-12        | SP-42 |           |    |     | Upgrade to Rel-8, no technical change | 7.0.0 | 8.0.0 |
| 2009-12        | SP-46 |           |    |     | Upgrade to Rel-9, no technical change | 8.0.0 | 9.0.0 |


<!-- ===== SOURCE FILE: raw__7_.md ===== -->



# **3rd Generation Partnership Project; Technical Specification Group Services and System Aspects; 3GPP TR 21.905 (2009.12) Vocabulary for 3GPP Specifications *Technical Report* (Release 9)** ---

![LTE logo](935eed7aa61f7777f62cfc032e11bee9_img.jpg)

The LTE logo features the lowercase letters "lte" in a bold, sans-serif font. Above the "l" and "t" are three red curved lines representing signal waves. A small "TM" trademark symbol is located to the right of the "e".

LTE logo

![3GPP logo](30a26f2d17ca95672702bf50fb4f0242_img.jpg)

The 3GPP logo consists of the letters "3GPP" in a stylized, bold, black font. The "3" and "G" are connected at the top. Below the "P" is a red signal wave icon. A small "TM" trademark symbol is located to the upper right of the "P".

3GPP logo

The present document has been developed within the 3<sup>rd</sup> Generation Partnership Project (3GPP<sup>TM</sup>) and may be further elaborated for the purposes of 3GPP.

The present document has not been subject to any approval process by the 3GPP Organisational Partners and shall not be implemented.  
This Specification is provided for future development work within 3GPP only. The Organisational Partners accept no liability for any use of this Specification.  
Specifications and reports for implementation of the 3GPP<sup>TM</sup> system should be obtained via the 3GPP Organisational Partners' Publications Offices.

## Keywords

---

GSM, UMTS, LTE, Vocabulary

## **3GPP**

### Postal address

### --- 3GPP support office address

---

650 Route des Lucioles - Sophia Antipolis  
Valbonne - FRANCE  
Tel.: +33 4 92 94 42 00 Fax: +33 4 93 65 47 16

## Internet

---

<http://www.3gpp.org>

## ***Copyright Notification***

No part may be reproduced except as authorized by written permission.  
The copyright and the foregoing restriction extend to reproduction in all media.

© 2009, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TTA, TTC).  
All rights reserved.

UMTSTM is a Trade Mark of ETSI registered for the benefit of its members  
3GPP™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners  
LTE™ is a Trade Mark of ETSI currently being registered for the benefit of its Members and of the 3GPP Organizational Partners  
GSM® and the GSM logo are registered and owned by the GSM Association

## Contents

---

|                              |    |
|------------------------------|----|
| Foreword .....               | 5  |
| 1 Scope.....                 | 5  |
| 2 References.....            | 5  |
| 3 Terms and definitions..... | 6  |
| 0-9.....                     | 6  |
| A.....                       | 6  |
| B.....                       | 7  |
| C.....                       | 8  |
| D.....                       | 10 |
| E.....                       | 11 |
| F.....                       | 12 |
| G.....                       | 12 |
| H.....                       | 13 |
| I.....                       | 13 |
| J.....                       | 15 |
| K.....                       | 15 |
| L.....                       | 15 |
| M.....                       | 16 |
| N.....                       | 18 |
| O.....                       | 19 |
| P.....                       | 19 |
| Q.....                       | 21 |
| R.....                       | 21 |
| S.....                       | 24 |
| T.....                       | 27 |
| U.....                       | 28 |
| V.....                       | 30 |
| W.....                       | 30 |
| X.....                       | 30 |
| Y.....                       | 30 |
| Z.....                       | 30 |
| 4 Abbreviations .....        | 30 |
| 0-9.....                     | 30 |
| A.....                       | 31 |
| B.....                       | 32 |
| C.....                       | 33 |
| D.....                       | 35 |
| E.....                       | 36 |
| F.....                       | 37 |
| G.....                       | 37 |
| H.....                       | 38 |
| I.....                       | 38 |
| J.....                       | 40 |
| K.....                       | 40 |
| L.....                       | 40 |
| M.....                       | 41 |
| N.....                       | 42 |
| O.....                       | 43 |
| P.....                       | 44 |
| Q.....                       | 45 |
| R.....                       | 46 |
| S.....                       | 47 |
| T.....                       | 49 |
| U.....                       | 50 |
| V.....                       | 51 |
| W.....                       | 51 |

X.....52  
Y.....52  
Z.....52  
5 Equations.....53  
Annex A (informative): Change history.....55

## --- Foreword

This Technical Specification has been produced by the 3<sup>rd</sup> Generation Partnership Project (3GPP).

The contents of the present document are subject to continuing work within the TSG and may change following formal TSG approval. Should the TSG modify the contents of the present document, it will be re-released by the TSG with an identifying change of release date and an increase in version number as follows:

Version x.y.z

where:

- x the first digit:
  - 1 presented to TSG for information;
  - 2 presented to TSG for approval;
  - 3 or greater indicates TSG approved document under change control.
- y the second digit is incremented for all changes of substance, i.e. technical enhancements, corrections, updates, etc.
- z the third digit is incremented when editorial only changes have been incorporated in the document.

# --- 1 Scope

The purpose of this report is to identify specialist technical terms used within the 3GPP project for the purposes of specifying service requirements. The motivations for this are:

- To ensure that editors use terminology that is consistent across specifications.
- To provide a reader with convenient reference for technical terms that are used across multiple documents.
- To prevent inconsistent use of terminology across documents.

This document is a collection of terms, definitions and abbreviations related to the baseline documents defining 3GPP objectives and systems framework. This document provides a tool for further work on 3GPP technical documentation and facilitates their understanding.

The terms, definitions and abbreviations as given in this document are either imported from existing documentation (ETSI, ITU or elsewhere) or newly created by 3GPP experts whenever the need for precise vocabulary was identified.

# --- 2 References

The following documents contain provisions which, through reference in this text, constitute provisions of the present document.

- References are either specific (identified by date of publication, edition number, version number, etc.) or non-specific.
- For a specific reference, subsequent revisions do not apply.
- For a non-specific reference, the latest version applies. In the case of a reference to a 3GPP document (including a GSM document), a non-specific reference implicitly refers to the latest version of that document *in the same Release as the present document*.

- [1] Void
- [2] 3GPP TS 25.990: "Technical Specification Group (TSG) RAN; Vocabulary ".
- [3] "The Path towards UMTS - Technologies for the Information Society" – Report #2, UMTS Forum.

- [4] 3GPP TS 23.122: "Non-Access-Stratum (NAS) functions related to Mobile Station (MS) in idle mode".
- [5] ETSI TR 180 000: "NGN terminology".

# --- 3 Terms and definitions

## 0-9

**1.8V technology Smart Card:** A Smart Card operating at  $1.8\text{V} \pm 10\%$  and  $3\text{V} \pm 10\%$ .

**1.8V technology Terminal:** A terminal operating the Smart Card - Terminal interface at  $1.8\text{V} \pm 10\%$  and  $3\text{V} \pm 10\%$ .

**3GPP Generic User Profile (GUP):** The 3GPP Generic User Profile is the collection of user related data which affects the way in which an individual user experiences services and which may be accessed in a standardised manner.

**3GPP system:** the telecommunication system standardised by the 3GPP consisting of a core network and a radio access network that may be either GERAN or UTRAN, or both.

**3GPP System core network:** refers in this specification to an evolved GSM core network infrastructure.

**3GPP System coverage:** see coverage area.

**3GPP System IC Card:** An IC card (or 'smartcard') of defined electromechanical specification which contains at least one USIM.

**3GPP System mobile termination:** part of the 3GPP System Mobile Station which provides functions specific to the management of the radio interface (Um).

**3GPP-WLAN Interworking:** Used to generically refer to interworking between the 3GPP system and the WLAN family of standards.

**3V technology Smart Card:** A Smart Card operating at  $3\text{V} \pm 10\%$  and  $5\text{V} \pm 10\%$ .

**3V technology Terminal:** A terminal operating the Smart Card - Terminal interface at  $3\text{V} \pm 10\%$  and  $5\text{V} \pm 10\%$ .

### A

**A/Gb mode:** mode of operation of the MS when connected to the Core Network via GERAN and the A and/or Gb interfaces.

**Acceptable Cell:** A cell that the UE may camp on to make emergency calls. It must satisfy certain conditions.

**Access conditions:** A set of security attributes associated with a file.

**Access delay:** The value of elapsed time between an access request and a successful access (source: ITU-T X.140).

**Access Stratum SDU (Service Data Unit):** Unit of data transferred over the access stratum SAP (Service Access Point) in the Core Network or in the User Equipment.

**Access protocol:** A defined set of procedures that is adopted at an interface at a specified reference point between a user and a network to enable the user to employ the services and/or facilities of that network (source: ITU-T I.112).

**Accounting:** The process of apportioning charges between the Home Environment, Serving Network and User.

**Accuracy:** A performance criterion that describes the degree of correctness with which a function is performed. (The function may or may not be performed with the desired speed.) (source: ITU-T I.350).

**Active communication:** a UE is in active communication when it has a CS connection established. For PS active communication is defined by the existence of one or more Activated PDP contexts. Either one or both of the mentioned active communications may occur in the UE.

**Active Set:** Set of radio links simultaneously involved in a specific communication service between an UE and a UTRAN.

**Adjacent Channel Leakage power Ratio (ACLR):** The ratio of the average power centered on the assigned channel frequency to the average power centered on an adjacent channel frequency. In both cases the average power is measured with a filter that has Root Raised Cosine (RRC) filter response with roll-off  $\alpha = 0.22$  and a bandwidth equal to the chip rate.

**Air Interface User Rate:** The user rate between Mobile Termination and IWF. For T services it is the maximum possible AIUR not including padding. For NT services it is the maximum possible AIUR.

**ALCAP:** Generic name for the transport signalling protocols used to set-up and tear-down transport bearers.

**Allowable PLMN:** A PLMN which is not in the list of forbidden PLMN in the UE.

**Allowed CSG list:** A list stored in the UE under both user and operator control, containing the CSG identities and associated PLMN identities of the CSGs to which the subscriber belongs.

**Applet:** A small program that is intended not to be run on its own, but rather to be embedded inside another application

**Application:** an application is a service enabler deployed by service providers, manufacturers or users. Individual applications will often be enablers for a wide range of services. (UMTS Forum report #2) [3]

**Applications / Clients:** These are services, which are designed using service capability features.

**Application Dedicated File (ADF):** an application DF is the entry point to an application on the UICC.

**Application Interface:** Standardised Interface used by application/clients to access service capability features.

**Application protocol:** The set of procedures required by the application.

**ASCI** Generic name to identify the services VGCS, VBS and eMLPP.

**Authentication:** A property by which the correct identity of an entity or party is established with a required assurance. The party being authenticated could be a user, subscriber, home environment or serving network.

**Available PLMN:** A PLMN where the UE has found a cell that satisfies certain conditions.

**Average power:** The thermal power as measured through a root raised cosine filter with roll-off  $\alpha = 0.22$  and a bandwidth equal to the chip rate of the radio access mode. The period of measurement shall be one power control group (timeslot) unless otherwise stated.

### B

**Base Station:** A base station is a network element in radio access network responsible for radio transmission and reception in one or more cells to or from the user equipment. A base station can have an integrated antenna or be connected to an antenna by feeder cables. In UTRAN it terminates the Iub interface towards the RNC. In GERAN it terminates the Abis interface towards the BSC.

**Baseline capabilities:** Capabilities that are required for a service-less UE to operate within a network. The baseline capabilities for a UE include the capabilities to search for, synchronise with and register (with authentication) to a network. The negotiation of the UE and the network capabilities, as well as the maintenance and termination of the registration are also part of the required baseline capabilities.

**Base Station Controller:** This equipment in the BSS is in charge of controlling the use and the integrity of the radio resources.

**Base Station Subsystem:** Either a full network or only the access part of a GERAN offering the allocation, release and management of specific radio resources to establish means of connection between an MS and the GERAN. A Base Station Subsystem is responsible for the resources and transmission/reception in a set of cells.

**Baseline Implementation Capabilities:** Set of Implementation capabilities, in each technical domain, required to enable a UE to support the required Baseline capabilities.

**Basic OR Basic Optimal Routeing**

**Basic telecommunication service:** This term is used as a common reference to both bearer services and teleservices.

**Bearer:** A information transmission path of defined capacity, delay and bit error rate, etc.

**Bearer capability:** A transmission function which the UE requests to the network.

**Bearer independent protocol:** (UICC) Mechanism by which the ME provides the (U)SIM applications on the UICC with access to the data bearers supported by the ME and the network.

**Bearer service:** A type of telecommunication service that provides the capability of transmission of signals between access points.

**Best effort QoS:** The lowest of all QoS traffic classes. If the guaranteed QoS cannot be delivered, the bearer network delivers the QoS which can also be called best effort QoS.

**Best effort service:** A service model which provides minimal performance guarantees, allowing an unspecified variance in the measured performance criteria.

**Billing:** A function whereby CDRs generated by the charging function are transformed into bills requiring payment.

**Broadcast:** A value of the service attribute "communication configuration", which denotes unidirectional distribution to all users (source: ITU-T I.113).

**Byte code:** (UICC) A hardware machine independent representation of a primitive computer operation that serves as an instruction to a software program called an interpreter or a virtual machine that simulates the hypothetical computer's central processing unit. code generated by a Java compiler and executed by the Java interpreter.

### C

**Cable, Connector, and Combiner Losses (Transmitter) (dB):** The combined losses of all transmission system components between the transmitter output and the antenna input (all losses in positive dB values).

**Cable, Connector, and Splitter Losses (Receiver) (dB):** The combined losses of all transmission system components between the receiving antenna output and the receiver input.

**CAC (Connection Admission Control):** A set of measures taken by the network to balance between the QoS requirements of new connections request and the current network utilisation without affecting the grade of service of existing/already established connections.

**Call:** a logical association between several users (this could be connection oriented or connection less).

**Charging Data Record (CDR):** A formatted collection of information about a chargeable event (e.g. time of call set-up, duration of the call, amount of data transferred, etc) for use in billing and accounting. For each party to be charged for parts of or all charges of a chargeable event a separate CDR shall be generated, i.e more than one CDR may be generated for a single chargeable event, e.g. because of its long duration, or because more than one charged party is to be charged.

**Camped on a cell:** The UE is in idle mode and has completed the cell selection/reselection process and has chosen a cell. The UE monitors system information and (in most cases) paging information. Note that the services may be limited, and that the PLMN may not be aware of the existence of the UE within the chosen cell.

**Capability Class:** A piece of information which indicates general 3GPP System mobile station characteristics (e.g. supported radio interfaces,...) for the interest of the network.

**Card session:** A link between the card and the external world starting with the ATR and ending with a subsequent reset or a deactivation of the card.

**CBS DRX cycle:** The time interval between successive readings of BMC messages.

**Cell:** Radio network object that can be uniquely identified by a User Equipment from a (cell) identification that is broadcasted over a geographical area from one UTRAN Access Point. A Cell is either FDD or TDD mode.

**Cell Radio Network Temporary Identifier (C-RNTI):** The C-RNTI is a UE identifier allocated by a controlling RNC and it is unique within one cell controlled by the allocating CRNC. C-RNTI can be reallocated when a UE accesses a new cell with the cell update procedure.

**Cellular Text telephone Modem (CTM):** A modulation and coding method intended for transmission of text in voice channels for the application of real time text conversation.

**Chargeable Event:** An activity utilising telecommunications network infrastructure and related services for user to user

communication (e.g. a single call, a data communication session or a short message), or for user to network communication (e.g. service profile administration), or for inter-network communication (e.g. transferring calls, signalling, or short messages), or for mobility (e.g. roaming or inter-system handover), which the network operator wants to charge for. The cost of a chargeable event may cover the cost of sending, transporting, delivery and storage. The cost of call related signalling may also be included.

**Charged Party:** A user involved in a chargeable event who has to pay parts or the whole charges of the chargeable event, or a third party paying the charges caused by one or all users involved in the chargeable event, or a network operator.

**Charging:** A function whereby information related to a chargeable event is formatted and transferred in order to make it possible to determine usage for which the charged party may be billed.

**Cipher key:** A code used in conjunction with a security algorithm to encode and decode user and/or signalling data.

**Closed group:** A group with a pre-defined set of members. Only defined members may participate in a closed group.

**Closed Subscriber Group (CSG):** A Closed Subscriber Group identifies subscribers of an operator who are permitted to access one or more cells of the PLMN but which have restricted access (CSG cells).

**Coded Composite Transport Channel:** A data stream resulting from encoding and multiplexing of one or several transport channels.

**Common Channel:** A Channel not dedicated to a specific UE.

**Confidentiality:** The avoidance of disclosure of information without the permission of its owner.

**Connected Mode:** Connected mode is the state of User Equipment switched on and an RRC connection established.

**Connection:** A communication channel between two or more end-points (e.g. terminal, server etc.).

**Connection mode:** The type of association between two points as required by the bearer service for the transfer of information. A bearer service is either connection-oriented or connectionless. In a connection oriented mode, a logical association called *connection* needs to be established between the source and the destination entities before information can be exchanged between them. Connection oriented bearer services lifetime is the period of time between the establishment and the release of the connection. In a connectionless mode, no connection is established beforehand between the source and the destination entities; the source and destination network addresses need to be specified in each message. Transferred information cannot be guaranteed of ordered delivery. Connectionless bearer services lifetime is reduced to the transport of one message.

**Connectionless (for a bearer service):** In a connectionless bearer, no connection is established beforehand between the source and the destination entities ; the source and destination network addresses need to be specified in each message. Transferred information cannot be guaranteed of ordered delivery. Connectionless bearer services lifetime is reduced to the transport of one message.

**Connectionless service:** A service which allows the transfer of information among service users without the need for end-to-end call establishment procedures (source: ITU-T I.113).

**Control channel:** A logical channel that carries system control information.

**Controlling RNC:** A role an RNC can take with respect to a specific set of UTRAN access points. There is only one Controlling RNC for any UTRAN access point. The Controlling RNC has the overall control of the logical resources of its UTRAN access point's.

**Conversational service:** An interactive service which provides for bi-directional communication by means of real-time (no store-and-forward) end-to-end information transfer from user to user (source: ITU-T I.113).

**Core network:** An architectural term relating to the part of 3GPP System which is independent of the connection technology of the terminal (eg radio, wired).

**Core Network Operator:** Operator that offers core network services.

**Corporate code:** Code which when combined with the network and SP codes refers to a unique Corporate. The code is provided in the GID2 file on the (U)SIM (see Annex A.1.) and is correspondingly stored on the ME.

**Corporate code group** combination of the Corporate code and the associated SP and network codes.

**Corporate personalisation:** Allows a corporate customer to personalise MEs that he provides for his employees or customers use so that they can only be used with the company's own (U)SIMs.

**Coverage area (of a mobile cellular system):** An area where mobile cellular services are provided by that mobile cellular system to the level required of that system.

**Coverage area:** Area over which a 3GPP System service is provided with the service probability above a certain threshold.

**CSG cell:** A cell, part of the PLMN, broadcasting a specific CSG Identity. A CSG cell is accessible by the members of the closed subscribers group for that CSG Identity. All the CSG cells sharing the same identity are identifiable as a single group.

**CSG Identity (CSGID):** An identity broadcast by a CSG cell or cells and used by the UE to facilitate access for authorised members of the associated Closed Subscriber Group.

**CSG Indicator:** An indication transmitted on the broadcast channel of the CSG cell that allows the UE to identify such as CSG cell.

**CSG manager:** A CSG manager can, under the operator's supervision, add, remove and view the list of CSG members.

**Current directory:** The latest MF or DF selected on the UICC.

**Current EF:** The latest EF selected.

**Current serving cell:** This is the cell on which the MS is camped.

### D

**Data field:** Obsolete term for Elementary File.

**Data Object:** Information coded as TLV objects, i.e. consisting of a Tag, a Length and a Value part.

**Dedicated Channel:** A channel dedicated to a specific UE.

**De-personalisation:** Is the process of deactivating the personalisation so that the ME ceases to carry out the verification checks.

**Dedicated File (DF):** A file containing access conditions and, optionally, Elementary Files (EFs) or other Dedicated Files (DFs).

**Delivered QoS:** Actual QoS parameter values with which the content was delivered over the lifetime of a QoS session.

**Demand service:** A type of telecommunication service in which the communication path is established almost immediately, in response to a user request effected by means of user-network signalling (source: ITU-T I.112).

**Dependability:** A performance criterion that describes the degree of certainty (or surety) with which a function is performed regardless of speed or accuracy, but within a given observational interval (source: ITU-T I.350).

**Destination user:** Entity to which calls to the General Packet Radio Service (GPRS) are directed.

**Directory:** General term for the MF or a DF on the UICC.

**Directory Number:** A string consisting of one or more of the characters from the set {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, \*, #, a, b, c} associated with a nature of address indicator and number plan indicator. When using the public MMI for the control of supplementary services however, \* and # cannot be part of any SC or SI field.

NOTE 1: No such restriction on the SC and SI fields exists when using other (e.g. menu-driven) MMI for the control of supplementary services.

NOTE 2: When using the public MMI, certain limitations on the use of one and two digit directory numbers may apply. The use of other MMI can remove these restrictions.

NOTE 3: This definition is not intended to require the support of all these characters in the MMI itself.

**Distribution service:** Service characterised by the unidirectional flow of information from a given point in the network to other (multiple) locations (source: ITU-T I.113).

**Domain:** The highest-level group of physical entities. Reference points are defined between domains.

**Domain Specific Access Control:** Access control functionality for access barring in either domain (i.e. CS domain or PS domain).

**Donor network:** The subscription network from which a number is ported in the porting process. This may or may not be the number range owner network.

**Downlink:** Unidirectional radio link for the transmission of signals from a UTRAN access point to a UE. Also in general the direction from Network to UE.

**Drift RNS:** The role an RNS can take with respect to a specific connection between a UE and UTRAN. An RNS that supports the Serving RNS with radio resources when the connection between the UTRAN and the User Equipment need to use cell(s) controlled by this RNS is referred to as Drift RNS.

### E

**Element Manager:** Provides a package of end-user functions for management of a set of closely related types of network elements. These functions can be divided into two main categories.

**Element Management Functions:** Set of functions for management of network elements on an individual basis. These are basically the same functions as supported by the corresponding local terminals.

**Elementary File (EF):** A file containing access conditions and data and no other files on the UICC.

**End-User:** An End-User is an entity (typically a user), associated with one or multiple subscriptions through identities (e.g. IMSIs, MSISDNs, IMPIs, IMPUs and application-specific identities). In the 3GPP system an End-User is characterised by an End-User Identity.

**End-User Identity (EUI):** An End-User Identity is an identity that uniquely characterises an End-User in the 3GPP system. An End-User Identity is mainly intended for administration purposes of the operator.

**Enterprise Systems:** Information Systems that are used in the telecommunication organisation but are not directly or essentially related to the telecommunications aspects (Call Centre's, Fraud Detection and Prevention Systems, Invoicing etc).

**Equivalent HPLMN:** Any of the PLMN entries contained in the Equivalent HPLMN list.

**Equivalent HPLMN list:** To allow provision for multiple HPLMN codes, PLMN codes that are present within this list shall replace the HPLMN code derived from the IMSI for PLMN selection purposes. This list is stored on the USIM and is known as the EHPLMN list. The EHPLMN list may also contain the HPLMN code derived from the IMSI. If the HPLMN code derived from the IMSI is not present in the EHPLMN list then it shall be treated as a Visited PLMN for PLMN selection purposes.

**Essential UE Requirement (Conditional):** Requirement which has to be implemented under certain Service conditions. e.g. AMR codec in UE which supports speech service

**Essential UE Requirement (Unconditional):** Requirement which has to be implemented in any 3G UE in order to exist in and communicate with 3G network (e.g. Chiprate of 3.84Mcps).

**Evolved Packet Core:** Is a framework for an evolution or migration of the 3GPP system to a higher-data-rate, lower-latency, packet-optimized system that supports, multiple RATs.

**Evolved Packet System:** Is an evolution of the 3G UMTS characterized by higher-data-rate, lower-latency, packet-optimized system that supports multiple RATs. The Evolved Packet System comprises the Evolved Packet Core together with the evolved radio access network (E-UTRA and E-UTRAN).

**Evolved UTRA:** Evolved UTRA is an evolution of the 3G UMTS radio-access technology towards a high-data-rate, low-latency and packet-optimized radio-access technology.

**Evolved UTRAN:** Evolved UTRAN is an evolution of the 3G UMTS radio-access network towards a high-data-rate, low-latency and packet-optimized radio-access network.

**Explicit Diversity Gain (dB):** The effective gain achieved using diversity techniques.

**Extra SDU delivery probability:** The ratio of total (unrequested) extra service data units (SDUs) to total service data units received by a destination user in a specified sample (source: ITU-T X.140).

NOTE: the term "user information unit" has been replaced by the term "service data unit".

### F

**File:** A named and hierarchically-classified data set on the UICC.

**File identifier (FID):** The 2-byte name of a file or a directory on the UICC.

**Fixed Network User Rate:** The user rate between IWF and the fixed network.

**FC (Flow Control):** A set of mechanisms used to prevent the network from becoming overloaded by regulating the input rate transmissions.

**Flexible Layer One (FLO):** GERAN feature that allows the channel coding of the layer one to be configured at call setup.

**Fixed Mobile Convergence (FMC):** In a given network configuration, the capabilities that provide service and application to the end-user irrespective of the fixed or mobile access technologies and independent of user's location. In the NGN environment, it means to provide NGN services to end-users regardless of the access technology.

**Framework:** A framework defines a set of Application Programming Interface (API) classes for developing applications and for providing system services to those applications.

**Functional group:** A set of functions that may be performed by a single equipment (source: ITU-T I.112).

### G

**Geographical routing:** The conversion of the PDU's geographical area definition, which specifies the area in which the PDU will be broadcast, into an equivalent radio coverage map.

**GERAN Radio Network Temporary Identifier (G-RNTI):** G-RNTI is an MS identifier which is allocated by the Serving BSC and is unique within this SBSC. It is allocated for all MSs having an RRC connection. The G-RNTI is always reallocated when the Serving BSC for the RRC connection is changed and deallocated when the RRC connection is released. The G-RNTI is also used at RLC/MAC during contention resolution.

**GPRS MS:** An MS capable of GPRS services is a GPRS MS.

**Group:** A set of members allowed to participate in the group call service. The group is defined by a set of rules that identifies a collection of members implicitly or explicitly. These rules may associate members for the purpose of participating in a group call, or may associate members who do not participate in data transfer but do participate in management, security, control, or accounting for the group.

**Group call:** The relationship that exists between the members of a group for the purpose of transferring data. More than one group call may exist in a group. A group call establishes an active group.

**Group call initiator:** A member (or third party) authorised to initiate a group call. More than one member may initiate group calls.

**Group call participant:** A member of a group participating in a particular group call at a given time.

**Group call server:** A logical entity that provides the group call service to the members.

**Group call service:** A PTM service in which a relationship exists between participants of the group, and in which a single data unit transmitted by a source participant is received by multiple destination participants; it is a one-in, many-out service.

**Group controller:** The member (or third party) responsible for the group creation and membership control.

**GSM/EDGE Radio Access Network:** GERAN is a conceptual term identifying that part of the network which consists of BSCs and BTSs between A/Gb or Iu and Um interfaces.

**GSM BSS:** refers in this specification to the GSM/GPRS access network.

**GSM core network:** refers in this specification to the GSM NSS and GPRS backbone infrastructure.

**GSM coverage:** an area where mobile cellular services are provided in accordance with GSM standards

**GSM session:** That part of the card session dedicated to the GSM operation.

**Guaranteed service:** A service model which provides highly reliable performance, with little or no variance in the measured performance criteria.

### H

**Handoff Gain/Loss (dB):** This is the gain/loss factor (+ or -) brought by handoff to maintain specified reliability at the cell boundary.

**Handover:** The transfer of a user's connection from one radio channel to another (can be the same or different cell).

**Handover:** The process in which the radio access network changes the radio transmitters or radio access mode or radio system used to provide the bearer services, while maintaining a defined bearer service QoS.

**Hard Handover:** Hard handover is a category of handover procedures where all the old radio links in the UE are abandoned before the new radio links are established.

**HE-VASP:** Home Environment Value Added Service Provider. This is a VASP that has an agreement with the Home Environment to provide services. The Home Environment provides services to the user in a managed way, possibly by collaborating with HE-VASPs, but this is transparent to the user. The same service could be provided by more than one HE-VASP and each HE-VASP can provide more than one service.

**Home Environment:** responsible for overall provision and control of the Personal Service Environment of its subscribers.

**HNB Name:** The HNB Name is a broadcast string in free text format that provides a human readable name for the Home NodeB/eNodeB.

**Home PLMN:** This is a PLMN where the MCC and MNC of the PLMN identity match the MCC and MNC of the IMSI. Matching criteria are defined in TS 23.122.

### I

**IC Card:** A card holding an Integrated Circuit containing subscriber, end user, authentication and/or application data for one or more applications.

**IC card SIM:** Obsolete term for ID-1 SIM.

**ICS proforma:** A document, in the form of a questionnaire, which when completed for an implementation or system becomes an ICS.

**ID-000 SIM:** A UICC having the form on an ID-000 card (see ISO 7816-1 [24]) that contains a SIM application.

**ID-1 SIM:** A UICC having the format of an ID-1 card (see ISO 7816-1 [24]) that contains a SIM.

**Idle mode:** The state of UE switched on but which does not have any established RRC connection.

**Implementation capability:** A capability that relates to a particular technical domain. Examples: a spreading factor of 128 (in the domain of the physical layer); the A5 algorithm; a 64 bit key length (in the domain of security); a power output of 21 dBm (in the domain of transmitter performance); support of AMR Codec (in the domain of the Codec); support of CHV1 (in the domain of the USIM).

**Implementation Conformance Statement (ICS):** A statement made by the supplier of an implementation or system claimed to conform to a given specification, stating which capabilities have been implemented. The ICS can take several forms: protocol ICS, profile ICS, profile specific ICS, information object ICS, etc.

**Information Data Rate:** Rate of the user information, which must be transmitted over the Air Interface. For example, output rate of the voice codec.

**Initial paging information:** This information indicates if the UE needs to continue to read more paging information and eventually receive a page message.

**Initial paging occasion:** The paging occasion the UE uses as starting point for its paging DRX cycle.

**Integrity:** (in the context of security) The avoidance of unauthorised modification of information.

**Inter-cell handover:** A handover between different cells. An inter-cell handover requires network connections to be altered.

**Inter PLMN handover:** Handover between different PLMNs, ie having different MCC-MNC.

**Inter system handover:** Handover between networks using different radiosystems , e.g. UMTS – GSM.

**Interactive service:** A service which provides the means for bi-directional exchange of information between users. Interactive services are divided into three classes of services: conversational services, messaging services and retrieval services (source: ITU-T I.113).

**Interface:** The common boundary between two associated systems (source: ITU-T I.112).

**International Mobile Station Equipment Identity (IMEI):** An "International Mobile Station Equipment Identity" is a unique number which shall be allocated to each individual mobile station equipment in the PLMN and shall be unconditionally implemented by the MS manufacturer.

**International mobile user number (IMUN):** The International Mobile User Number is a diallable number allocated to a 3GPP System user.

**Interference Signal Code Power (ISCP):** Given only interference power is received, the average power of the received signal after despreading and combining.

**Interpreter:** A software program that simulates a hypothetical computer by performing the operations defined by the instructions of this computer.(see also 'byte code' and 'virtual machine').

**Interworking WLAN (I-WLAN):** A WLAN that interworks with a 3GPP system.

**Intra-cell handover:** A handover within one sector or between different sectors of the same cell. An intra-cell handover does not require network connections to be altered.

**Intra PLMN handover:** Handover within the same network, ie having the same MCC-MNC regardless of radio access system.

Note: this includes the case of UMTS  $\leftrightarrow$  GSM handover where MCC-MNC are the same in both cases.

**IP-Connectivity Access Network (IP-CAN):** The collection of network entities and interfaces that provides the underlying IP transport connectivity between the UE and the IMS entities. An example of an "IP-Connectivity Access Network" is GPRS.

**IP-Connectivity Access Network bearer (IP-CAN bearer):** The data communications bearer provided by the IP-Connectivity Access Network. When using GPRS, the IP-Connectivity Access Network bearers are provided by PDP Contexts.

**IRP Information Model:** An IRP Information Model consists of an IRP Information Service and a Network Resource Model (see below for definitions of IRP Information Service and Network Resource Model).

**IRP Information Service:** An IRP Information Service describes the information flow and support objects for a certain functional area, e.g. the alarm information service in the fault management area. As an example of support objects, for the Alarm IRP there is the alarm record and alarm list.

**IRP Solution Set:** An IRP Solution Set is a mapping of the IRP Information Service to one of several technologies (CORBA/IDL, SNMP/SMI, CMIP/GDMO, etc.). An IRP Information Service can be mapped to several different IRP Solution Sets. Different technology selections may be done for different IRPs.

**Inter System Change:** a change of radio access between different radio access technologies such as GSM and UMTS.

**IMS Credentials (IMC):** A set of IMS security data and functions for IMS access by a terminal that does not support any 3GPP access technology.. The IMC is not including an ISIM or a USIM. The IMC is not used if ISIM or USIM is

present..

**IMS Multimedia Telephony:** A service that allows multimedia conversational communications between two or more users. It provides real time bidirectional conversational transfer of media, e.g. speech, video, text or other types of data. The IMS multimedia telephony service includes Supplementary Services and takes account of regulatory requirements.

**IMS SIM (ISIM):** An application residing on the UICC that provides access to IP Multimedia Services.

**Iu:** Interconnection point between an RNC or a BSC and a 3G Core Network. It is also considered as a reference point.

**Iu-flex:** Routing functionality for intra domain connection of RAN nodes to multiple CN nodes.

**Iu mode:** mode of operation of the MS when connected to the Core Network via GERAN or UTRAN and the Iu interface.

**Iub:** Interface between an RNC and a Node B.

**Iur:** A logical interface between two RNC. Whilst logically representing a point to point link between RNC, the physical realisation may not be a point to point link.

### J

<void>

### K

**Key pair:** Key pairs are matching private and public keys. If a block of data is encrypted using the private key, the public key from the pair can be used to decrypt it. The private key is never divulged to any other party, but the public key is available, e.g. in a certificate.

### L

**Local Service:** Services, which are provided by current roamed to network that are not HE services. The same service can be provided by a network as a local service to inbound roamers and as a HE service to the subscribers of this network.

**Localised Service Area (LSA):** A LSA is an operator-defined group of cells, for which specific access conditions apply. This may correspond to an area in which the Core Network offers specific services. A LSA may be defined within a PLMN or globally. Therefore, a LSA may offer a non-contiguous radio coverage.

**Location Registration (LR):** The UE registers its presence in a registration area, for instance regularly or when entering a new registration area.

**Logical Channel:** A logical channel is an information stream dedicated to the transfer of a specific type of information over the radio interface. Logical Channels are provided on top of the MAC layer.

**Logical Channel (UICC):** A command/response communication context multiplexed on the physical channel between the ME and the UICC.

**Logical Model:** A Logical Model defines an abstract view of a network or network element by means of information objects representing network element, aggregations of network elements, the topological relationship between the elements, endpoints of connections (termination points), and transport entities (such as connections) that transport information between two or more termination points.

The information objects defined in the Logical Model are used, among others, by connection management functions. In this way a physical implementation independent management is achieved.

**Logical O&M:** Logical O&M is the signalling associated with the control of logical resources (channels, cells,) owned by the RNC but physically implemented in the Node B. The RNC controls these logical resources. A number of O&M procedures physically implemented in Node B impact on the logical resources and therefore require an information exchange between RNC and Node B. All messages needed to support this information exchange are classified as Logical O&M forming an integral part of NBAP.

**LSA exclusive access cell:** A UE may only camp on this cell if the cell belongs to the LSAs to which the user has subscribed. Nevertheless, if no other cells are available, the UE of non-LSA users may originate emergency calls from

this cell.

**LSA only access:** When LSA only access applies to the user, the UE can only access cells that belong to the LSAs to which the user has subscribed. Outside the coverage area of the subscribed LSAs, the UE may camp on other cells and limited services apply.

**LSA preferential access cell:** A LSA preferential access cell is a cell which is part of the LSA. UEs of users that have subscribed to a LSA of a LSA-preferential-access cell have higher priority to resources than non-LSA users in the same cell.

### M

**Macro cells:** "Macro cells" are outdoor cells with a large cell radius.

**Macro diversity handover:** "Macro diversity" is a operation state in which a User Equipment simultaneously has radio links with two or more UTRAN access points for the sole aim of improving quality of the radio connection or providing seamless.

**Management Infrastructure:** The collection of systems (computers and telecommunications) a 3GPP System Organisation has in order to manage a 3GPP System.

**Mandatory UE Requirement:** Regulatory requirement which is applicable to 3G UEs. It is determined by each country/region and beyond the scope of 3GPP specification (e.g. spurious emission in UK).

**Master File (MF):** The root directory of the file system hierarchy on the UICC.

**Maximum output Power:** For UE, this is a measure of the maximum power supported by the UE (i.e. the actual power as would be measured assuming no measurement error) (TS 25.101). For FDD BS, the mean power level per carrier of the base station measured at the antenna connector in a specified reference condition (TS 25.104). For TDD BS this refers to the measure of power when averaged over the transmit timeslot at the maximum power setting (TS 25.105).

**Maximum possible AIUR:** The highest possible AIUR that the multiple TCH/F can provide, e.g. 2 TCH/F using TCH/F9.6 provides a maximum possible AIUR of 19,2 kbit/s.

**Maximum Transmitter Power Per Traffic Channel (dBm):** The maximum power at the transmitter output for a single traffic channel.

**Mean bit rate:** A measure of throughput. The average (mean) bit rate available to the user for the given period of time (source: ITU-T I.210).

**Mean transit delay:** The average transit delay experienced by a (typically) large sample of PDUs within the same service category.

**Medium Access Control:** A sub-layer of radio interface layer 2 providing unacknowledged data transfer service on logical channels and access to transport channels.

**Messaging service:** An interactive service which offers user-to-user communication between individual users via storage units with store-and-forward, mailbox and/or message handling, (e.g., information editing, processing and conversion) functions (source: ITU-T I.113).

**MExE Classmark:** A MExE classmark identifies a category of MExE UE supporting MExE functionality with a minimum level of processing, memory, display, and interactive capabilities. Several MExE classmarks may be defined to differentiate between the functionalities offered by different MExE UEs. A MExE application or applet defined as being of a specific MExE Classmark indicates that it is supportable by a MExE UE of that Classmark.

**MExE executable:** An executable is an applet, application, or executable content, which conforms to the MExE specification and may execute on the ME.

**MExE server:** A node supporting MExE services in the MExE service environment.

**MExE service:** a service enhanced (or made possible) by MExE technology.

**MExE service environment:** Depending on the configuration of the PLMN, the operator may be able to offer support to MExE services in various ways. Examples of possible sources are from traditional GSM nodes, IN nodes, operator-

specific nodes, operator franchised nodes and services provider nodes, together with access to nodes external (i.e. vendor-specific) to the PLMN depending on the nature of the MExE service. These nodes are considered to constitute the MExE service environment. The MExE service environment shall support direct MExE UE to MExE UE interaction of MExE services.

**MExE service provider:** an organisation which delivers MExE services to the subscriber. This is normally the PLMN operator, but could be an organisation with MExE responsibility (which may have been delegated by the PLMN operator).

**MExE SIM:** A (U)SIM application that is capable of storing a security certificate that is accessible using standard mechanisms.

**MExE subscriber:** The owner of a subscription who has entered into an agreement with a MExE service provider for MExE services.

**Micro cells:** "Micro cells" are small cells.

**Minimum transmit power:** The minimum controlled output power of the TDD BS is when the power control setting is set to a minimum value. This is when the power control indicates a minimum transmit output power is required (TS 25.105).

**Mobile Equipment (ME):** The Mobile Equipment is functionally divided into several entities, i.e. one or more Mobile Terminations (MT) and one or more Terminal Equipments (TE).

**Mobile evaluated handover:** Mobile evaluated handover (MEHO) is a type of handover triggered by an evaluation made in the mobile. The mobile evaluates the necessity of handover based on the measured radio environment and based on criteria defined by the network. When the evaluation meets the hand-off criteria the necessary information is sent from the mobile to the network. The network then decides on the necessity of the handover based on the reported evaluation result and other conditions, e.g. uplink radio environment and/or availability of network resources, the network may then execute the handover.

**Mobile Station (MS):** A Mobile Station (MS) corresponds to a User Equipment (UE). See 3GPP TS 24.002.

**Mobile number portability:** The ability for a mobile subscriber to change subscription network within the same country whilst retaining their original MSISDN(s).

**Mobile Termination (MT):** The Mobile Termination is the component of the Mobile Equipment (ME) which supports functions specific to management of the PLMN access interface (3GPP or non-3GPP). The MT is realized as a single functional entity..

**Mobility:** The ability for the user to communicate whilst moving independent of location.

**Mobility Management:** A relation between the mobile station and the UTRAN that is used to set-up, maintain and release the various physical channels.

**Multi mode terminal:** UE that can obtain service from at least one UTRA radio access mode, and one or more different systems such as GSM bands or possibly other radio systems such IMT-2000 family members.

**Multicast service:** A unidirectional PTM service in which a message is transmitted from a single source entity to all subscribers currently located within a geographical area. The message contains a group identifier indicating whether the message is of interest to all subscribers or to only the subset of subscribers belonging to a specific multicast group.

**Multipoint:** A value of the service attribute "communication configuration", which denotes that the communication involves more than two network terminations (source: ITU-T I.113).

**Multimedia service:** Services that handle several types of media such as audio and video in a synchronised way from the user's point of view. A multimedia service may involve multiple parties, multiple connections, and the addition or deletion of resources and users within a single communication session.

### N

**Name:** A name is an alpha numeric label used for identification of end users and may be portable.

**Negotiated QoS:** In response to a QoS request, the network shall negotiate each QoS attribute to a level that is in accordance with the available network resources. After QoS negotiation, the bearer network shall always attempt to provide adequate resources to support all of the negotiated QoS profiles.

**Network code:** MCC and MNC.

**Network code group:** Same as network code.

**Network connection:** An association established by a network layer between two users for the transfer of data, which provides explicit identification of a set of network data transmissions and agreement concerning the services to be provided by the set (source: ITU-T X.213 / ISO-IEC 8348).

**Network Element:** A discrete telecommunications entity which can be managed over a specific interface e.g. the RNC.

**Network Manager:** Provides a package of end-user functions with the responsibility for the management of a network, mainly as supported by the EM(s) but it may also involve direct access to the network elements. All communication with the network is based on open and well standardized interfaces supporting management of multi-vendor and multi-technology network elements.

**Network operator:** See PLMN operator.

**Network personalisation:** Allows the network operator to personalise a ME so that it can only be used with that particular network operator's (U)SIMs.

**Network Resource Model:** A protocol independent model describing managed objects representing network resources, e.g. an RNC or NodeB.

**Network service data unit (NSDU):** A unit of data passed between the user and the GPRS network across a Network Service Access Point (NSAP).

**Network subset code:** digits 6 and 7 of the IMSI.

**Network subset code group:** Combination of a network subset code and the associated network code.

**Network subset personalisation:** A refinement of network personalisation, which allows network operators to limit the usage of a ME to a subset of (U)SIMs

**Network termination:** A functional group on the network side of a user-network interface (source: ITU-T I.112).

**Node B:** A logical node responsible for radio transmission / reception in one or more cells to/from the User Equipment. Terminates the Iub interface towards the RNC.

**Nomadic Operating Mode:** Mode of operation where the terminal is transportable but being operated while stationary and may in addition require user co-operation (e.g. close to open spaces, antenna setup...).

**Nominal Maximum Output Power:** This is the nominal power defined by the UE power class.

**Non-Access Stratum:** Protocols between UE and the core network that are not terminated in the UTRAN.

**Normal GSM operation:** Relating to general, CHV related, GSM security related and subscription related procedures.

**Normal mode of operation:** The mode of operation into which the ME would have gone if it had no personalisation checks to process.

**NTDD:** Narrow TDD – the 1.28 Mcps chip rate UTRA-TDD option

**Number:** A string of decimal digits that uniquely indicates the public network termination point. The number contains the information necessary to route the call to this termination point.

A number can be in a format determined nationally or in an international format. The international format is known as the International Public Telecommunication Number which includes the country code and subsequent digits, but not the international prefix.

**Number portability:** A capability that allows a user to retain the same public telecommunication number when changing from one service provider to another. Additional regulatory constraints may apply in different regions.

**Number range owner network:** The network to which the number range containing the ported number has been

allocated.

### O

**Off-Line charging:** A charging process where charging information does not affect, in real time, the service rendered.

**On-Line Charging:** A charging process where charging information can affect, in real time, the service rendered and therefore directly interacts with the session/service control.

**One Stop Billing:** One bill for all charges incurred using the 3GPP System.

**Open group:** A group that does not have a pre-defined set of members. Any user may participate in an open group.

**Open Service Access:** Concept for introducing a vendor independent means for introduction of new services.

**Operations System:** This abbreviation indicates a generic management system, independent of its location level within the management hierarchy.

**Operator CSG list:** A list stored in the UE under exclusive Operator control, containing the CSG identities and associated PLMN identities of the CSGs to which the subscriber belongs.

**Optional UE Requirement:** Any other requirements than mandatory UE requirement, essential UE requirement (conditional), essential UE requirement (unconditional). It is totally up to individual manufacturer to decide whether it should be implemented or not (e.g. Network initiated MM connection establishment).

**Originating network:** The network where the calling party is located.

**Orthogonal Channel Noise Simulator** a mechanism used to simulate the users or control signals on the other orthogonal channels of a downlink

**OSA Interface:** Standardised Interface used by application/clients to access service capability features.

### P

**Packet:** An information unit identified by a label at layer 3 of the OSI reference model (source: ITU-T I.113). A network protocol data unit (NPDU).

**Packet data protocol (PDP):** Any protocol which transmits data as discrete units known as packets, e.g., IP, or X.25.

**Packet transfer mode:** Also known as packet mode. A transfer mode in which the transmission and switching functions are achieved by packet oriented techniques, so as to dynamically share network transmission and switching resources between a multiplicity of connections (source: ITU-T I.113).

**Padding:** One or more bits appended to a message in order to cause the message to contain the required number of bits or bytes.

**Paging:** The act of seeking a User Equipment.

**Paging DRX cycle:** The individual time interval between monitoring Paging Occasion for a specific UE

**Paging Block Periodicity (PBP):** The period of the occurrence of Paging Blocks. (For FDD, PBP = 1).

**Paging Message Receiving Occasion:** The frame where the UE receives actual paging message.

**Paging occasion:** The frame where the UE monitors in FDD or the paging block, which consists of several frames, for TDD. For Paging Blocks, the value of Paging Occasion is equal to the first frame of the Paging Block.

**Peak bit rate:** A measure of throughput. The maximum bit rate offered to the user for a given time period (to be defined) for the transfer of a bursty signal (source: ITU-T I.210). (The maximum user information transfer rate achievable by a user for a single service data unit transfer.)

**Performance:** The ability to track service and resource usage levels and to provide feedback on the responsiveness and reliability of the network.

**Personal Service Environment:** contains personalised information defining how subscribed services are provided and presented towards the user. Each subscriber of the Home Environment has her own Personal Service Environment. The

Personal Service Environment is defined in terms of one or more User Profiles.

**Personalisation:** The process of storing information in the ME and activating the procedures which verify this information against the corresponding information stored in applications on the (U)SIM whenever the ME is powered up or when a UICC containing network access applications (SIM, USIM, etc.) is inserted, in order to limit the applications with which the ME will operate.

**Personalisation entity:** Network, network subset, SP, Corporate or (U)SIM to which the ME is personalised

**Phonebook:** A dataset of personal or entity attributes. The simplest form is a set of name-subscriber phone number pairs as supported by GSM (U)SIMs.

**Physical channel data stream:** In the uplink, a data stream that is transmitted on one physical channel. In the downlink, a data stream that is transmitted on one physical channel in each cell of the active set.

**Physical Channel:** In FDD mode, a physical channel is defined by code, frequency and, in the uplink, relative phase (I/Q). In TDD mode, a physical channel is defined by code, frequency, and time-slot.

**Pico cells:** "Pico cells" are cells, mainly indoor cells, with a radius typically less than 50 metres.

**PICH Monitoring Occasion:** The time instance where the UE monitors PICH within Paging Occasion.

**Pilot Identity:** A service specific public address used for initial contact, associated with a group of publicly addressable identities (e.g. E.164 numbers or SIP URI).

**PLMN Area:** The PLMN area is the geographical area in which a PLMN provides communication services according to the specifications to mobile users. In the PLMN area, the mobile user can set up calls to a user of a terminating network. The terminating network may be a fixed network, the same PLMN, another PLMN or other types of PLMN. Terminating network users can also set up calls to the PLMN. The PLMN area is allocated to a PLMN. It is determined by the service and network provider in accordance with any provisions laid down under national law. In general the PLMN area is restricted to one country. It can also be determined differently, depending on the different telecommunication services, or type of MS. If there are several PLMNs in one country, their PLMN areas may overlap. In border areas, the PLMN areas of different countries may overlap. Administrations will have to take precautions to ensure that cross border coverage is minimised in adjacent countries unless otherwise agreed.

**PLMN Operator:** Public Land Mobile Network operator. The entity which offers telecommunications services over an air interface..

**Plug-in SIM:** A physical form factor of SIM (see ID-000 SIM).

**point-to-multipoint service:** A service type in which data is sent to "all service subscribers or a pre-defined subset of all subscribers" within an area defined by the Service Requester.

**Point-to-point:** A value of the service attribute "communication configuration", which denotes that the communication involves only two network terminations.

**Point-to-point service:** A service type in which data is sent from a single network termination to another network termination.

**Ported number:** A MSISDN that has undergone the porting process.

**Ported subscriber:** The subscriber of a ported number.

**Porting process:** A description of the transfer of a number between network operators.

**Power control dynamic range:** The difference between the maximum and the minimum total transmit output power for a specified reference condition (TS 25.104).

**Predictive service:** A service model which provides reliable performance, but allowing a specified variance in the measured performance criteria.

**Prepay billing:** Billing arrangement between customer and operator/service provider where the customer deposits an amount of money in advance, which is subsequently used to pay for service usage.

**Postpay billing:** Billing arrangement between customer and operator/service provider where the customer periodically receives a bill for service usage in the past period.

**Proactive SIM:** A SIM, which is capable of issuing commands to the Terminal. Part of SIM Application Toolkit.

**Protocol:** A formal set of procedures that are adopted to ensure communication between two or more functions within the within the same layer of a hierarchy of functions (source: ITU-T I.112).

**Protocol data unit:** In the reference model for OSI, a unit of data specified in an (N)-protocol layer and consisting of (N)-protocol control information and possibly (N)-user data (source: ITU-T X.200 / ISO-IEC 7498-1).

**Public land mobile network:** A telecommunications network providing mobile cellular services.

### Q

**QoS profile:** a QoS profile comprises a number of QoS parameters. A QoS profile is associated with each QoS session. The QoS profile defines the performance expectations placed on the bearer network.

**QoS session:** Lifetime of PDP context. The period between the opening and closing of a network connection whose characteristics are defined by a QoS profile. Multiple QoS sessions may exist, each with a different QoS profile.

**Quality of Service:** The collective effect of service performances which determine the degree of satisfaction of a user of a service. It is characterised by the combined aspects of performance factors applicable to all services, such as;

- service operability performance;
- service accessibility performance;
- service retainability performance;
- service integrity performance; and
- other factors specific to each service.

### R

**Radio access bearer:** The service that the access stratum provides to the non-access stratum for transfer of user data between User Equipment and CN.

**Radio Access Mode:** Mode of the cell, FDD or TDD.

**Radio Access Network Information Management:** Functionality supporting the exchange of information, via the Core Network, between peer application entities located in a GERAN or in a UTRAN access network.

**RAN sharing:** Two or more CN operators share the same RAN, i.e. a RAN node (RNC or BSC) is connected to multiple CN nodes (SGSNs and MSC/VLRs) belonging to different CN operators.

**Radio Access Network Application Part:** Radio Network Signalling over the Iu.

**Radio Access Network Operator:** Operator that offers radio access to one or more core network operators.

**Radio Access Technology:** UTRA, GERAN etc.

**Radio Bearer:** The service provided by the Layer 2 for transfer of user data between User Equipment and UTRAN.

**Radio frame:** A radio frame is a numbered time interval of 10 ms duration used for data transmission on the radio physical channel. A radio frame is divided into 15 time slots of 0.666 ms duration. The unit of data that is mapped to a radio frame (10 ms time interval) may also be referred to as radio frame.

**Radio interface:** The "radio interface" is the tetherless interface between User Equipment and a UTRAN access point. This term encompasses all the functionality required to maintain such interfaces.

**Radio link:** A "radio link" is a logical association between single User Equipment and a single UTRAN access point. Its physical realisation comprises one or more radio bearer transmissions.

**Radio link addition:** The procedure where a new radio link is added to the active set.

**Radio Link Control:** A sublayer of radio interface layer 2 providing transparent, unacknowledged and acknowledged data transfer service.

**Radio link removal:** The procedure where a radio link is removed from the active set.

**Radio Link Set:** A set of one or more Radio Links that has a common generation of Transmit Power Control (TPC) commands in the DL

**Radio Network Controller:** This equipment in the RNS is in charge of controlling the use and the integrity of the radio resources.

**Radio Network Subsystem Application Part:** Radio Network Signalling over the Iur.

**Radio Network Subsystem:** Either a full network or only the access part of a UTRAN offering the allocation and the release of specific radio resources to establish means of connection in between an UE and the UTRAN. A Radio Network Subsystem is responsible for the resources and transmission/reception in a set of cells.

**Radio Network Temporary Identifier:** A Radio Network Temporary Identifier is a generic term of an identifier for a UE when an RRC connection exists. Following types of RNTI are defined: Cell RNTI (C-RNTI), Serving RNC RNTI (S-RNTI), UTRAN RNTI (U-RNTI) and GERAN RNTI (G-RNTI).

**Radio Resource Control:** A sublayer of radio interface Layer 3 existing in the control plane only which provides information transfer service to the non-access stratum. RRC is responsible for controlling the configuration of radio interface Layers 1 and 2.

**Radio system:** the selected 2<sup>nd</sup> or 3<sup>rd</sup> generation radio access technology, eg UTRAN or GERAN.

**Rated Output Power:** For FDD BS, rated output power is the mean power level per carrier that the manufacturer has declared to be available at the antenna connector. For TDD BS rated output power is the mean power level per carrier over an active timeslot that the manufacturer has declared to be available at the antenna connector.

**Real time:** Time, typically in number of seconds, to perform the on-line mechanism used for fraud control and cost control.

**Received Signal Code Power:** Given only signal power is received, the average power of the received signal after despreading and combining.

**Receiver Antenna Gain (dBi):** The maximum gain of the receiver antenna in the horizontal plane (specified as dB relative to an isotropic radiator).

**Receiver Noise Figure (dB):** Receiver noise figure is the noise figure of the receiving system referenced to the receiver input.

**Receiver Sensitivity (dBm):** This is the signal level needed at the receiver input that just satisfies the required  $E_b/(N_0+I_0)$ .

**Recipient network:** The network which receives the number in the porting process. This network becomes the subscription network when the porting process is complete.

**Record:** A string of bytes within an EF handled as a single entity.

**Record number:** The number, which identifies a record within an EF.

**Record pointer:** The pointer, which addresses one record in an EF.

**Reference configuration:** A combination of functional groups and reference points that shows possible network arrangements (source: ITU-T I.112).

**Reference point:** A conceptual point at the conjunction of two non-overlapping functional groups (source: ITU-T I.112).

**Regionally Provided Service:** A service entitlement to only certain geographical part(s) of a PLMN, as controlled by the network operator.

**Registration:** This is the process of camping on a cell of the PLMN and doing any necessary LRs.

**Registered PLMN (RPLMN):** This is the PLMN on which the UE has performed a location registration successfully.

**Registration Area:** A (NAS) registration area is an area in which the UE may roam without a need to perform location registration, which is a NAS procedure.

**Relay:** Terminal devices capable of ODMA relay communications.

**Relay/Seed Gateway:** Relay or Seed that communicates with the UTRAN, in either TDD or FDD mode.

**Relaylink:** Relaylink is a communications link between two ODMA relay nodes.

**Release 99:** A particular version of the 3GPP System standards produced by the 3GPP project. Also: Release 4, Release 5, Release 6 etc..

**Repeater:** A "repeater" is a radio transceiver used to extend the transmission of a base station beyond its normal range.

**Requested QoS:** a QoS profile is requested at the beginning of a QoS session. QoS modification requests are also possible during the lifetime of a QoS session.

**Required Eb/(No+Io) (dB):** The ratio between the received energy per information bit to the total effective noise and interference power density needed to satisfy the quality objectives.

**Residual error rate:** A parameter describing service accuracy. The frequency of lost SDUs, and of corrupted or duplicated network SDUs delivered at the user-network interface.

**Retrieval service:** An interactive service which provides the capability of accessing information stored in data base centres. The information will be sent to the user on demand only. The information is retrieved on an individual basis, i.e., the time at which an information sequence is to start is under the control of the user (source ITU-T I.113).

**Roaming:** The ability for a user to function in a serving network different from the home network. The serving network could be a shared network operated by two or more network operator.

**Root directory:** Obsolete term for Master File.

**Root Relay:** ODMA relay node where communications originate or terminate.

**RRC Connection:** A point-to-point bi-directional connection between RRC peer entities on the UE and the UTRAN sides, respectively. An UE has either zero or one RRC connection.

### S

**SDU error probability:** The ratio of total incorrect service data units (SDUs) to total successfully transferred service data units plus incorrect service data units in a specified sample (source: ITU-T X.140).

NOTE: the source document term "user information unit" has been replaced by the term "service data unit".

**SDU loss probability:** The ratio of total lost service data units (SDUs) to total transmitted service data units in a specified sample (source: ITU-T X.140).

NOTE: the source document term "user information unit" has been replaced by the term "service data unit".

**SDU misdelivery probability:** The ratio of total misdelivered service data units (SDUs) to total service data units transferred between a specified source and destination user in a specified sample (source: ITU-T X.140).

NOTE: the source document term "user information unit" has been replaced by the term "service data unit".

**SDU transfer delay:** The value of elapsed time between the start of transfer and successful transfer of a specified service data unit (SDU) (source: ITU-T X.140).

NOTE: the source document term "user information unit" has been replaced by the term "service data unit".

**SDU transfer rate:** The total number of successfully transferred service data units (SDUs) in a transfer sample divided by the input/output time for that sample. The input/output time is the larger of the input time or the output time for the sample (source: ITU-T X.140).

NOTE: the source document term "user information unit" has been replaced by the term "service data unit".

**Seamless handover:** "Seamless handover" is a handover without perceptible interruption of the radio connection.

**Sector:** A "sector" is a sub-area of a cell. All sectors within one cell are served by the same base station. A radio link within a sector can be identified by a single logical identification belonging to that sector.

**Secured Packet:** The information flow on top of which the level of required security has been applied. An Application Message is transformed with respect to a chosen Transport Layer and chosen level of security into one or more Secured Packets.

**Security:** The ability to prevent fraud as well as the protection of information availability, integrity and confidentiality.

**Seed:** Deployed ODMA relay node with or without a display/keypad.

**Selected PLMN:** This is the PLMN that has been selected by the non-access stratum, either manually or automatically.

**Service:** a component of the portfolio of choices offered by service providers to a user, a functionality offered to a user.

**Service-less UE:** A UE that has only the Baseline capabilities.

**Service Access Point:** A conceptual point where a protocol layer offers access to its services to upper layer.

**Service Area:** The Service Area is defined in the same way as the Service Area according to ITU-T Recommendation Q.1001 [4]. In contrast to the PLMN area it is not based on the coverage of a PLMN. Instead it is based on the area in which a fixed network user can call a mobile user without knowing his location. The Service Area can therefore change when the signalling system is being extended, for example.

**Service attribute:** A specified characteristic of a telecommunication service (source: ITU-T I.112).

NOTE: the value(s) assigned to one or more service attributes may be used to distinguish that telecommunications service from others.

**Service bit rate:** The bit rate that is available to a user for the transfer of user information (source: ITU-T I.113).

**Service Capabilities:** Bearers defined by parameters, and/or mechanisms needed to realise services. These are within networks and under network control.

**Service Capability Feature:** Functionality offered by service capabilities that are accessible via the standardised application interface

**Service Capability Server:** Network functionality providing open interfaces towards the functionality offered by 3GPP System service capabilities.

**Service category or service class:** A service offered to the users described by a set of performance parameters and their specified values, limits or ranges. The set of parameters provides a comprehensive description of the service capability.

**Service Continuity:** The uninterrupted user experience of a service that is using an active communication (e.g. an ongoing voice call) when a UE undergoes a radio access technology change or a CS/PS domain change without, as far as possible, the user noticing the change.

NOTE: In particular Service Continuity encompasses the possibility that after a RAT / domain change the user experience is maintained by a different telecommunication service (e.g. tele- or bearer service) than before the RAT / domain change.

**Service Control:** The ability of the user, home environment or serving environment to determine what a particular service does, for a specific invocation of that service, within the limitations of that service.

**Service Data Unit (SDU):** In the reference model for OSI, an amount of information whose identity is preserved when transferred between peer (N+1)-layer entities and which is not interpreted by the supporting (N)-layer entities (source: ITU-T X.200 / ISO-IEC 7498-1).

**Service delay:** The time elapsed from the invocation of the service request, to the corresponding service request indication at the Service Receiver, indicating the arrival of application data.

**Service Enabler:** a capability which may be used, either by itself or in conjunction with other service enablers, to provide a service to the end user.

**Service Execution Environment:** A platform on which an application or programme is authorised to perform a number of functionalities; examples of service execution environments are the user equipment, integrated circuit card and a network platform or any other server.

**Service Feature:** Functionality that a 3GPP System shall offer to enable provision of services. Services, are made up of

different service features.

**Service Implementation Capabilities:** Set of implementation capabilities, in each technical domain, required to enable a UE to support a set of UE Service Capabilities.

**Service model:** A general characterisation of services based upon a QoS paradigm, without specifying the actual performance targets.

**Service Provider:** A Service Provider is either a network operator or an other entity that provides services to a subscriber (e.g. a MVNO)

**Service receiver:** The entity which receives the service request indication primitive, containing the SDU.

**Service relationship:** The association between two or more entities engaged in the provision of services.

**Service request:** This is defined as being one invocation of the service through a service request primitive.

**Service requester:** The entity which requests the initiation of a GPRS operation, through a service request.

**Service Specific Entities:** Entities dedicated to the provisioning of a given (set of) service(s). The fact that they are implemented or not in a given PLMN should have limited impact on all the other entities of the PLMN.

**Service subscriber:** Entity which subscribes to the General Packet Radio Service (GPRS) service.

**Services (of a mobile cellular system):** The set of functions that the mobile cellular system can make available to the user.

**Serving BSS:** A role a BSS can take with respect to a specific connection between an MS and GERAN. There is one Serving BSS for each MS that has a connection to GERAN. The Serving BSS is in charge of the RRC connection between an MS and the GERAN. The Serving BSS terminates the Iu for this connection.

**Serving Network:** The serving network provides the user with access to the services of home environment.

**Serving RNS:** A role an RNS can take with respect to a specific connection between an UE and UTRAN. There is one Serving RNS for each UE that has a connection to UTRAN. The Serving RNS is in charge of the RRC connection between a UE and the UTRAN. The Serving RNS terminates the Iu for this connection.

**Settlement:** Payment of amounts resulting from the accounting process.

**Shared Channel:** A radio resource (transport channel or physical channel) that can be shared dynamically between several UEs.

**Shared Network:** When two or more network operator sharing network elements.

**Short File Identifier (SFI):** A 5-bit abbreviated name for a file in a directory on the UICC.

**Short time:** Time, typically in number of minutes, to perform the off-line mechanism used for accounting.

**Signalling:** The exchange of information specifically concerned with the establishment and control of connections, and with management, in a telecommunications network (source: ITU-T I.112).

**Signalling connection:** An acknowledged-mode link between the user equipment and the core network to transfer higher layer information between the entities in the non-access stratum.

**Signalling link:** Provides an acknowledged-mode link layer to transfer the UE-UTRAN signalling messages as well as UE - Core Network signalling messages (using the signalling connection).

**SIM application toolkit procedures:** The portion of the communication protocol between the ME and the UICC that enables applications on the UICC to send commands to the ME.

**SIM code:** Code which when combined with the network and NS codes refers to a unique SIM. The code is provided by the digits 8 to 15 of the IMSI

**(U)SIM code group:** Combination of the (U)SIM code and the associated network subset and network codes (it is equivalent to the IMSI).

**(U)SIM personalisation:** Enables a user to personalise a ME so that it may only be used with particular (U)SIM(s).

**Simultaneous use of services:** The concurrent use of a circuit-mode service (voice or data) and packet-mode services (GPRS) by a single mobile station.

**Soft Handover:** Soft handover is a category of handover procedures where the radio links are added and abandoned in such manner that the UE always keeps at least one radio link to the UTRAN.

**SP code:** code which when combined with the network code refers to a unique SP. The code is provided in the GID1 file on the SIM (see Annex A.1.) and is correspondingly stored on the ME.

**SP code group:** Combination of the SP code and the associated network code.

**SP personalisation:** Allows the service provider to personalise a ME so that it can only be used with that particular service provider's (U)SIMs.

**Speed:** A performance criterion that describes the time interval required to perform a function or the rate at which the function is performed. (The function may or may not be performed with the desired accuracy.) (source: ITU-T I.350).

**SRNC Radio Network Temporary Identifier (S-RNTI):** S-RNTI is UE identifier which is allocated by the Serving RNC and unique within this SRNC. It is allocated for all UEs having a RRC connection. S-RNTI is reallocated always when the Serving RNC for the RRC connection is changed and deallocated when the RRC connection is released.

**SRNS Relocation:** The change of Iu instance and transfer of the SRNS role to another RNS.

**Stratum:** Grouping of protocols related to one aspect of the services provided by one or several domains.

**Steering of Roaming:** A technique whereby a roaming UE is encouraged to roam to a preferred VPLMN by the HPLMN.

**Sub Network Management Functions:** Set of functions that are related to a network model for a set of network elements constituting a clearly defined sub-network, which may include relations between the network elements. This model enables additional functions on the sub-network level (typically in the areas of network topology presentation, alarm correlation, service impact analysis and circuit provisioning).

**Subscribed QoS:** The network will not grant a QoS greater than the subscribed. The QoS profile subscription parameters are held in the HLR. An end user may have several QoS subscriptions. For security and the prevention of damage to the network, the end user cannot directly modify the QoS subscription profile data.

**Subscriber:** A Subscriber is an entity (associated with one or more users) that is engaged in a Subscription with a service provider. The subscriber is allowed to subscribe and unsubscribe services, to register a user or a list of users authorised to enjoy these services, and also to set the limits relative to the use that associated users make of these services.

**Subscription:** A subscription describes the commercial relationship between the subscriber and the service provider.

**Subscription Management (SuM):** set of capabilities that allow Operators, Service Providers, and indirectly subscribers, to provision, control, monitor the Subscription Profile.

**Suitable Cell:** This is a cell on which an UE may camp. It must satisfy certain conditions.

**Supplementary service:** A service which modifies or supplements a basic telecommunication service. Consequently, it cannot be offered to a user as a standalone service. It must be offered together with or in association with a basic telecommunication service. The same supplementary service may be common to a number of basic telecommunication services.

**System Area:** The System Area is defined as the group of PLMN areas accessible by MSs. Interworking of several PLMNs and interworking between PLMNs and fixed network(s) permit public land mobile communication services at international level.

### T

**Teleaction service:** A type of telecommunication service that uses short messages, requiring a low transmission rate, between the user and the network (source: ITU-T I.112).

**Telecommunication service:** What is offered by a PLMN operator or service provider to its customers in order to satisfy a specific telecommunication requirement. (source: ITU-T I.112). Telecommunication services are divided into

two broad families: bearer services and teleservices (source: ITU-T I.210).

**Teleservice:** Is a type of telecommunication service that provides the complete capability, including terminal equipment functions, for communication between users according to standardised protocols and transmission capabilities established by agreement between operators.

**Terminal:** A device into which a UICC can be inserted and which is capable of providing access to 3GPP System services to users, either alone or in conjunction with a UICC.

**Terminal Equipment (TE):** Equipment that provides the functions necessary for the operation of the access protocols by the user. A functional group on the user side of a user-network interface (source: ITU-T I.112).

**Test environment:** A "test environment" is the combination of a test propagation environment and a deployment scenario, which together describe the parameters necessary to perform a detailed analysis of a radio transmission technology.

**Text conversation:** Real time transfer of text between users in at least two locations.

**Text Telephony:** An audiovisual conversation service providing bi-directional real time transfer of text and optionally audio between users in two locations. Audio may be transmitted alternating with text or simultaneously with text. (Source ITU-T F.703)

**Throughput:** A parameter describing service speed. The number of data bits successfully transferred in one direction between specified reference points per unit time (source: ITU-T I.113).

**Toolkit applet:** An application on the UICC that generates proactive commands to the ME.

**Total Conversation:** An audiovisual conversation service providing bi-directional symmetric real-time transfer of motion video, text and voice between users in two or more locations. (source ITU-T F.703)

**Total power dynamic range:** The difference between the maximum and the minimum total transmit output power for a specified reference condition (TS25.104).

**Traffic channel:** A "traffic channel" is a logical channel which carries user information.

**Transit delay:** A parameter describing service speed. The time difference between the instant at which the first bit of a protocol data unit (PDU) crosses one designated boundary (reference point), and the instant at which the last bit of the PDU crosses a second designated boundary (source: ITU-T I.113).

**Transmission Time Interval:** Transmission Time Interval is defined as the inter-arrival time of Transport Block Sets, i.e. the time it shall take to transmit a Transport Block Set.

**Transmitter Antenna Gain (dBi):** The maximum gain of the transmitter antenna in the horizontal plane (specified as dB relative to an isotropic radiator).

**Transport Block:** Transport Block is defined as the basic data unit exchanged between L1 and MAC. An equivalent term for Transport Block is "MAC PDU".

**Transport Block Set:** Transport Block Set is defined as a set of Transport Blocks that is exchanged between L1 and MAC at the same time instance using the same transport channel. An equivalent term for Transport Block Set is "MAC PDU Set".

**Transport Block Set Size:** Transport Block Set Size is defined as the number of bits in a Transport Block Set.

**Transport Block Size:** Transport Block Size is defined as the size (number of bits) of a Transport Block.

**Transport channel:** The channels offered by the physical layer to Layer 2 for data transport between peer L1 entities are denoted as Transport Channels. Different types of transport channels are defined by how and with which characteristics data is transferred on the physical layer, e.g. whether using dedicated or common physical channels.

**Transport Format:** A Transport Format is defined as a format offered by L1 to MAC for the delivery of a Transport Block Set during a Transmission Time Interval on a Transport Channel. The Transport Format constitutes of two parts – one dynamic part and one semi-static part.

**Transport Format Combination:** A Transport Format Combination is defined as the combination of currently valid Transport Formats on all Transport Channels of an UE, i.e. containing one Transport Format from each Transport

Channel.

**Transport Format Combination Set:** A Transport Format Combination Set is defined as a set of Transport Format Combinations to be used by an UE.

**Transport Format Combination Indicator (TFCI):** A Transport Format Combination Indicator is a representation of the current Transport Format Combination.

**Transport Format Identification (TFI in UTRAN, TFIN in GERAN):** A label for a specific Transport Format within a Transport Format Set.

**Transport Format Set:** A set of Transport Formats. For example, a variable rate DCH has a Transport Format Set (one Transport Format for each rate), whereas a fixed rate DCH has a single Transport Format.

### U

**UE Service Capabilities:** Capabilities that can be used either singly or in combination to deliver services to the user. The characteristic of UE Service Capabilities is that their logical function can be defined in a way that is independent of the implementation of the 3GPP System (although all UE Service Capabilities are of course constrained by the implementation of the 3GPP System). Examples: a data bearer of 144 kbps; a high quality speech teleservice; an IP teleservice; a capability to forward a speech call.

**UICC:** a physically secure device, an IC card (or 'smart card'), that can be inserted and removed from the terminal. It may contain one or more applications. One of the applications may be a USIM.

**Universal Subscriber Identity Module (USIM):** An application residing on the UICC used for accessing services provided by mobile networks, which the application is able to register on with the appropriate security.

**Universal Terrestrial Radio Access Network (UTRAN):** UTRAN is a conceptual term identifying that part of the network which consists of RNCs and Node Bs between Iu and Uu interfaces.

**Usage Parameter Control (UPC):** Set of actions taken by the network to monitor and control the offered traffic and the validity of the connection with respect to the traffic contract negotiated between the user and the network.

**Uplink:** An "uplink" is a unidirectional radio link for the transmission of signals from a UE to a base station, from a Mobile Station to a mobile base station or from a mobile base station to a base station.

**URA updating:** URA updating is a family of procedures that updates the UTRAN registration area of a UE when a RRC connection exists and the position of the UE is known on URA level in the UTRAN.

**User:** An entity, not part of the 3GPP System, which uses 3GPP System services. Example: a person using a 3GPP System mobile station as a portable telephone.

**User-network interface:** The interface between the terminal equipment and a network termination at which interface the access protocols apply (source: ITU-T I.112).

**User-user protocol:** A protocol that is adopted between two or more users in order to ensure communication between them (source: ITU-T I.112).

**User access or user network access:** The means by which a user is connected to a telecommunication network in order to use the services and/or facilities of that network (source: ITU-T I.112).

**User Equipment (UE):** Allows a user access to network services. For the purpose of 3GPP specifications the interface between the UE and the network is the radio interface. A User Equipment can be subdivided into a number of domains, the domains being separated by reference points. Currently the User Equipment is subdivided into the UICC domain and the ME Domain. The ME Domain can further be subdivided into one or more Mobile Termination (MT) and Terminal Equipment (TE) components showing the connectivity between multiple functional groups.

In the context of Fixed Broadband Access to IMS, TISPAN defines the term UE in ETSI TR180 000 [5].

**User Interface Profile:** Contains information to present the personalised user interface within the capabilities of the terminal and serving network.

**User Services Profile:** Contains identification of subscriber services, their status and reference to service preferences.

**UTRA Radio access mode:** the selected UTRA radio access mode ie UTRA-FDD;UTRA-TDD.

**UTRA-NTDD:** Time Division Duplex UTRA access mode 1.28 Mcps option

**UTRA-TDD:** Time Division Duplex UTRA Radio access mode (Includes UTRA-NTDD and UTRA-WTDD)

**UTRA-WTDD:** Time Division Duplex UTRA access mode 3.84 Mcps option

**UTRAN access point:** A conceptual point within the UTRAN performing radio transmission and reception. A UTRAN access point is associated with one specific cell, i.e. there exists one UTRAN access point for each cell. It is the UTRAN-side end point of a radio link.

**UTRAN Registration Area:** The UTRAN Registration Area is an area covered by a number of cells. The URA is only internally known in the UTRAN.

**UTRAN Radio Network Temporary Identifier:** The U-RNTI is a unique UE identifier that consists of two parts, an SRNC identifier and a C-RNTI. U-RNTI is allocated to an UE having a RRC connection. It identifies the UE within UTRAN and is used as an UE identifier in cell update, URA update, RRC connection reestablishment and (UTRAN originated) paging messages and associated responses on the radio interface.

**User Profile:** Is the set of information necessary to provide a user with a consistent, personalised service environment, irrespective of the user's location or the terminal used (within the limitations of the terminal and the serving network).

**Uu:** The Radio interface between UTRAN and the User Equipment.

### V

**Value Added Service Provider:** Provides services other than basic telecommunications service for which additional charges may be incurred.

**Variable bit rate service:** A type of telecommunication service characterised by a service bit rate specified by statistically expressed parameters which allow the bit rate to vary within defined limits (source: ITU-T I.113).

**Virtual Home Environment:** A concept for personal service environment portability across network boundaries and between terminals.

**Virtual Machine:** A software program that simulates a hypothetical computer central processing unit. The programs executed by a virtual machine are represented as byte codes, which are primitive operations for this hypothetical computer.

**Visited PLMN:** This is a PLMN different from the HPLMN (if the EHPLMN list is not present or is empty) or different from an EHPLMN (if the EHPLMN list is present).

**Visited PLMN of home country:** This is a Visited PLMN where the MCC part of the PLMN identity is the same as the MCC of the IMSI.

### W

**WTDD:** Wide TDD – the 3.84 Mcps chip rate UTRA-TDD option.

**WLAN UE: WLAN User Equipment:** – a UE (equipped with UICC card including (U)SIM) utilized by a subscriber capable of accessing a WLAN network. A WLAN UE may include entities whose configuration, operation and software environment are not under the exclusive control of the 3GPP system operator, such as a laptop computer or PDA with a WLAN card, UICC card reader and suitable software applications.

### X

<void>

### Y

<void>

### Z

<void>

# 4 Abbreviations

## 0-9

|       |                                      |
|-------|--------------------------------------|
| 2G    | 2 <sup>nd</sup> Generation           |
| 3G    | 3 <sup>rd</sup> Generation           |
| 3GPP  | Third Generation Partnership Project |
| 8-PSK | 8-state Phase Shift Keying           |

### A

|        |                                                                                               |
|--------|-----------------------------------------------------------------------------------------------|
| A-SGW  | Access Signalling Gateway                                                                     |
| A3     | Authentication algorithm A3                                                                   |
| A38    | A single algorithm performing the functions of A3 and A8                                      |
| A5/1   | Encryption algorithm A5/1                                                                     |
| A5/2   | Encryption algorithm A5/2                                                                     |
| A5/X   | Encryption algorithm A5/0-7                                                                   |
| A8     | Ciphering key generating algorithm A8                                                         |
| AAL    | ATM Adaptation Layer                                                                          |
| AAL2   | ATM Adaptation Layer type 2                                                                   |
| AAL5   | ATM Adaptation Layer type 5                                                                   |
| AB     | Access Burst                                                                                  |
| AC     | Access Class (C0 to C15)                                                                      |
|        | Access Condition                                                                              |
|        | Application Context                                                                           |
|        | Authentication Centre                                                                         |
| ACC    | Automatic Congestion Control                                                                  |
| ACELP  | Algebraic Code Excited Linear Prediction                                                      |
| ACCH   | Associated Control Channel                                                                    |
| ACIR   | Adjacent Channel Interference Ratio                                                           |
| ACK    | Acknowledgement                                                                               |
| ACL    | APN Control List                                                                              |
| ACLR   | Adjacent Channel Leakage Power Ratio                                                          |
| ACM    | Accumulated Call Meter                                                                        |
|        | Address Complete Message                                                                      |
| ACMmax | ACM (Accumulated Call Meter) maximal value                                                    |
| ACS    | Adjacent Channel Selectivity                                                                  |
| ACU    | Antenna Combining Unit                                                                        |
| ADC    | Administration Centre                                                                         |
|        | Analogue to Digital Converter                                                                 |
| ADCH   | Associated Dedicated CHannel                                                                  |
| ADF    | Application Dedicated File                                                                    |
| ADM    | Access condition to an EF which is under the control of the authority which creates this file |
| ADN    | Abbreviated Dialling Numbers                                                                  |
| ADPCM  | Adaptive Differential Pulse Code Modulation                                                   |
| AE     | Application Entity                                                                            |
| AEC    | Acoustic Echo Control                                                                         |
| AEF    | Additional Elementary Functions                                                               |
| AESA   | ATM End System Address                                                                        |
| AFC    | Automatic Frequency Control                                                                   |
| AGCH   | Access Grant CHannel                                                                          |
| Ai     | Action indicator                                                                              |
| AI     | Acquisition Indicator                                                                         |

|            |                                          |
|------------|------------------------------------------|
| AICH       | Acquisition Indicator Channel            |
| AID        | Application IDentifier                   |
| AIUR       | Air Interface User Rate                  |
| AK         | Anonymity Key                            |
| AKA        | Authentication and Key Agreement         |
| AKI        | Asymmetric Key Index                     |
| ALCAP      | Access Link Control Application Protocol |
| ALSI       | Application Level Subscriber Identity    |
| ALW        | ALWays                                   |
| AM         | Acknowledged Mode                        |
| AMF        | Authentication Management Field          |
| AMR        | Adaptive Multi Rate                      |
| AMR-WB     | Adaptive Multi Rate Wide Band            |
| AN         | Access Network                           |
| ANP        | Access Network Provider                  |
| AoC        | Advice of Charge                         |
| AoCC       | Advice of Charge Charging                |
| AoCI       | Advice of Charge Information             |
| AP         | Access preamble                          |
| APDU       | Application Protocol Data Unit           |
| API        | Application Programming Interface        |
| APN        | Access Point Name                        |
| ARFCN      | Absolute Radio Frequency Channel Number  |
| ARP        | Address Resolution Protocol              |
| ARQ        | Automatic Repeat ReQuest                 |
| ARR        | Access Rule Reference                    |
| AS         | Access Stratum                           |
| ASC        | Access Service Class                     |
| ASCI       | Advanced Speech Call Items               |
| ASE        | Application Service Element              |
| ASN.1      | Abstract Syntax Notation One             |
| AT command | ATtention Command                        |
| ATM        | Asynchronous Transfer Mode               |
| ATR        | Answer To Reset                          |
| ATT (flag) | Attach                                   |
| AU         | Access Unit                              |
| AuC        | Authentication Centre                    |
| AUT(H)     | Authentication                           |
| AUTN       | Authentication token                     |
| AWGN       | Additive White Gaussian Noise            |

### B

|        |                                            |
|--------|--------------------------------------------|
| B-ISDN | Broadband ISDN                             |
| BA     | BCCH Allocation                            |
| BAIC   | Barring of All Incoming Calls              |
| BAOC   | Barring of All Outgoing Calls              |
| BCC    | Base Transceiver Station (BTS) Colour Code |
| BCCH   | Broadcast Control Channel                  |
| BCD    | Binary Coded Decimal                       |
| BCF    | Base station Control Function              |
| BCFE   | Broadcast Control Functional Entity        |
| BCH    | Broadcast Channel                          |
| BCIE   | Bearer Capability Information Element      |
| BDN    | Barred Dialling Number                     |
| BER    | Bit Error Ratio                            |
|        | Basic Encoding Rules (of ASN.1)            |
| BFI    | Bad Frame Indication                       |
| BG     | Border Gateway                             |
| BGT    | Block Guard Time                           |

|            |                                                                                        |
|------------|----------------------------------------------------------------------------------------|
| BI         | all Barring of Incoming call                                                           |
| BIC        | Baseline Implementation Capabilities                                                   |
| BIC-Roam   | Barring of Incoming Calls when Roaming outside the home PLMN country                   |
| BID        | Binding Identity                                                                       |
| BLER       | Block Error Ratio                                                                      |
| Bm         | Full-rate traffic channel                                                              |
| BMC        | Broadcast/Multicast Control                                                            |
| BN         | Bit Number                                                                             |
| BO         | all Barring of Outgoing call                                                           |
| BOC        | Bell Operating Company                                                                 |
| BOIC       | Barring of Outgoing International Calls                                                |
| BOIC-exHC  | Barring of Outgoing International Calls except those directed to the Home PLMN Country |
| BPSK       | Binary Phase Shift Keying                                                              |
| BS         | Base Station                                                                           |
|            | Basic Service (group)                                                                  |
|            | Bearer Service                                                                         |
| BSG        | Basic Service Group                                                                    |
| BSC        | Base Station Controller                                                                |
| BSIC       | Base transceiver Station Identity Code                                                 |
| BSIC-NCELL | BSIC of an adjacent cell                                                               |
| BSS        | Base Station Subsystem                                                                 |
| BSSAP      | Base Station Subsystem Application Part                                                |
| BSSGP      | Base Station Subsystem GPRS Protocol                                                   |
| BSSMAP     | Base Station Subsystem Management Application Part                                     |
| BSSOMAP    | Base Station Subsystem Operation and Maintenance Application Part                      |
| BTFD       | Blind Transport Format Detection                                                       |
| BTS        | Base Transceiver Station                                                               |
| BVC        | BSS GPRS Protocol Virtual Connection                                                   |
| BVCI       | BSS GPRS Protocol Virtual Connection Identifier                                        |
| BWT        | Block Waiting Time                                                                     |

### C

|        |                                                          |
|--------|----------------------------------------------------------|
| C      | Conditional                                              |
| C-     | Control-                                                 |
| C-APDU | Command APDU                                             |
| C-RNTI | Cell Radio Network Temporary Identity                    |
| C-TPDU | Command TPDU                                             |
| CA     | Capacity Allocation                                      |
|        | Cell Allocation                                          |
|        | Certification Authority                                  |
| CAA    | Capacity Allocation Acknowledgement                      |
| CAD    | Card Acceptance Device                                   |
| CAI    | Charge Advice Information                                |
| CAMEL  | Customised Application for Mobile network Enhanced Logic |
| CAP    | CAMEL Application Part                                   |
| CB     | Cell Broadcast                                           |
| CBC    | Cell Broadcast Centre                                    |
|        | Cipher Block Chaining                                    |
| CBCH   | Cell Broadcast CHannel                                   |
| CBMI   | Cell Broadcast Message Identifier                        |
| CBR    | Constant Bit Rate                                        |
| CBS    | Cell Broadcast Service                                   |
| CC     | Call Control                                             |
|        | Country Code                                             |
|        | Cryptographic Checksum                                   |
| CC/PP  | Composite Capability/Preference Profiles                 |
| CCBS   | Completion of Calls to Busy Subscriber                   |
| CCCH   | Common Control Channel                                   |
| CCF    | Call Control Function                                    |
| CCH    | Control Channel                                          |

|         |                                                                                                                                   |
|---------|-----------------------------------------------------------------------------------------------------------------------------------|
| CCI     | Capability / Configuration Identifier                                                                                             |
| CCITT   | Comité Consultatif International Télégraphique et Téléphonique (The International Telegraph and Telephone Consultative Committee) |
| CCK     | Corporate Control Key                                                                                                             |
| CCM     | Certificate Configuration Message<br>Current Call Meter                                                                           |
| CCP     | Capability/Configuration Parameter                                                                                                |
| CCPCH   | Common Control Physical Channel                                                                                                   |
| Cct     | Circuit                                                                                                                           |
| CCTrCH  | Coded Composite Transport Channel                                                                                                 |
| CD      | Capacity Deallocation<br>Collision Detection                                                                                      |
| CDA     | Capacity Deallocation Acknowledgement                                                                                             |
| CDCH    | Control-plane Dedicated CHannel                                                                                                   |
| CDMA    | Code Division Multiple Access                                                                                                     |
| CDR     | Charging Data Record                                                                                                              |
| CDUR    | Chargeable DURation                                                                                                               |
| CED     | called station identifier                                                                                                         |
| CEIR    | Central Equipment Identity Register                                                                                               |
| CEND    | end of charge point                                                                                                               |
| CEPT    | Conférence des administrations Européennes des Postes et Telecommunications                                                       |
| CF      | Conversion Facility<br>all Call Forwarding services                                                                               |
| CFB     | Call Forwarding on mobile subscriber Busy                                                                                         |
| CFN     | Connection Frame Number                                                                                                           |
| CFNRc   | Call Forwarding on mobile subscriber Not Reachable                                                                                |
| CFNRy   | Call Forwarding on No Reply                                                                                                       |
| CFU     | Call Forwarding Unconditional                                                                                                     |
| CGI     | Common Gateway Interface<br>Cell Global Identifier                                                                                |
| CHAP    | Challenge Handshake Authentication Protocol                                                                                       |
| CHP     | CHarging Point                                                                                                                    |
| CHV     | Card Holder Verification information                                                                                              |
| CI      | Cell Identity<br>CUG index                                                                                                        |
| CIM     | Common Information Model                                                                                                          |
| CIR     | Carrier to Interference Ratio                                                                                                     |
| CK      | Cipher Key                                                                                                                        |
| CKSN    | Ciphering Key Sequence Number                                                                                                     |
| CLA     | CLAss                                                                                                                             |
| CLI     | Calling Line Identity                                                                                                             |
| CLIP    | Calling Line Identification Presentation                                                                                          |
| CLIR    | Calling Line Identification Restriction                                                                                           |
| CLK     | Clock                                                                                                                             |
| CM      | Connection Management                                                                                                             |
| CMD     | Command                                                                                                                           |
| CMIP    | Common Management Information Protocol                                                                                            |
| CMISE   | Common Management Information Service                                                                                             |
| CMM     | Channel Mode Modify                                                                                                               |
| CN      | Core Network<br>Comfort Noise                                                                                                     |
| CNAP    | Calling Name Presentation                                                                                                         |
| CNG     | Calling Tone                                                                                                                      |
| CNL     | Co-operative Network List                                                                                                         |
| CNTR    | Counter                                                                                                                           |
| CLNP    | Connectionless network protocol                                                                                                   |
| CLNS    | Connectionless network service                                                                                                    |
| COLI    | COnnected Line Identity                                                                                                           |
| COLP    | COnnected Line identification Presentation                                                                                        |
| COLR    | COnnected Line identification Restriction                                                                                         |
| COM     | COMplete                                                                                                                          |
| CONNACK | Connect Acknowledgement                                                                                                           |

|          |                                                     |
|----------|-----------------------------------------------------|
| CONS     | Connection-oriented network service                 |
| CORBA    | Common Object Request Broker Architecture           |
| CP-Admin | Certificate Present (in the MExE SIM)-Administrator |
| CP-TP    | Certificate Present (in the MExE SIM)-Third Party   |
| CPBCCH   | COMPACT Packet BCCH                                 |
| CPICH    | Common Pilot Channel                                |
| CPCH     | Common Packet Channel                               |
| CPCS     | Common Part Convergence Sublayer                    |
| CPS      | Common Part Sublayer                                |
| CPU      | Central Processing Unit                             |
| C/R      | Command/Response field bit                          |
| CRC      | Cyclic Redundancy Check                             |
| CRE      | Call Ree-establishment procedure                    |
| CRNC     | Controlling Radio Network Controller                |
| CS-GW    | Circuit Switched Gateway                            |
| CS       | Circuit Switched                                    |
|          | Coding Scheme                                       |
| CSCF     | Call Server Control Function                        |
| CSD      | Circuit Switched Data                               |
| CSE      | Camel Service Environment                           |
| CSG      | Closed Subscriber Group                             |
| CSGID    | Closed Subscriber Group IDentity                    |
| CSPDN    | Circuit Switched Public Data Network                |
| CT       | Call Transfer supplementary service                 |
|          | Channel Tester                                      |
|          | Channel Type                                        |
| CTCH     | Common Traffic Channel                              |
| CTDMA    | Code Time Division Multiple Access                  |
| CTFC     | Calculated Transport Format Combination             |
| CTM      | Cellular Text telephone Modem                       |
| CTR      | Common Technical Regulation                         |
| CTS      | Cordless Telephony System                           |
| CUG      | Closed User Group                                   |
| CW       | Call Waiting                                        |
|          | Continuous Wave (unmodulated signal)                |
| CWI      | Character Waiting Integer                           |
| CWT      | Character Waiting Time                              |

### D

|         |                                              |
|---------|----------------------------------------------|
| DAC     | Digital to Analog Converter                  |
| DAD     | Destination ADress                           |
| DAM     | DECT Authentication Module                   |
| DB      | Dummy Burst                                  |
| DC      | Dedicated Control (SAP)                      |
| DCA     | Dynamic Channel Allocation                   |
| DCCH    | Dedicated Control Channel                    |
| DCE     | Data Circuit terminating Equipment           |
| DCF     | Data Communication Function                  |
| DCH     | Dedicated Channel                            |
| DCK     | Depersonalisation Control Key                |
| DCN     | Data Communication Network                   |
| DCS     | Data Coding Scheme                           |
| DCS1800 | Digital Cellular Network at 1800MHz          |
| DDI     | Direct Dial In                               |
| DECT    | Digital Enhanced Cordless Telecommunications |
| DET     | Detach                                       |
| DES     | Data Encryption Standard                     |
| DF      | Dedicated File                               |
| DHCP    | Dynamic Host Configuration Protocol          |

|           |                                                              |
|-----------|--------------------------------------------------------------|
| DHO       | Diversity Handover                                           |
| diff-serv | Differentiated services                                      |
| DISC      | Disconnect                                                   |
| DL        | Data Layer                                                   |
|           | Downlink (Forward Link)                                      |
| DLCI      | Data Link Connection Identifier                              |
| DLD       | Data Link Discriminator                                      |
| Dm        | Control channel (ISDN terminology applied to mobile service) |
| DMR       | Digital Mobile Radio                                         |
| DMTF      | Distributed Management Task Force                            |
| DN        | Destination Network                                          |
| DNIC      | Data Network Identifier                                      |
| DNS       | Directory Name Service                                       |
| DO        | Data Object                                                  |
| DP        | Dial/Dialled Pulse                                           |
| DPCCH     | Dedicated Physical Control Channel                           |
| DPCH      | Dedicated Physical Channel                                   |
| DPDCH     | Dedicated Physical Data Channel                              |
| DRAC      | Dynamic Resource Allocation Control                          |
| DRNC      | Drift Radio Network Controller                               |
| DRNS      | Drift RNS                                                    |
| DRX       | Discontinuous Reception                                      |
| DS-CDMA   | Direct-Sequence Code Division Multiple Access                |
| DSAC      | Domain Specific Access Control                               |
| DSCH      | Downlink Shared Channel                                      |
| DSE       | Data Switching Exchange                                      |
| DSI       | Digital Speech Interpolation                                 |
| DSS1      | Digital Subscriber Signalling No1                            |
| DTAP      | Direct Transfer Application Part                             |
| DTCH      | Dedicated Traffic Channel                                    |
| DTE       | Data Terminal Equipment                                      |
| DTMF      | Dual Tone Multiple Frequency                                 |
| DTX       | Discontinuous Transmission                                   |

### E

|        |                                                                  |
|--------|------------------------------------------------------------------|
| E-GGSN | Enhanced GGSN                                                    |
| E-HLR  | Enhanced HLR                                                     |
| EA     | External Alarms                                                  |
| EBSG   | Elementary Basic Service Group                                   |
| ECB    | Electronic Code-book                                             |
| ECC    | Emergency Call Code                                              |
|        | Elliptic Curve Cryptography                                      |
| ECM    | Error Correction Mode (facsimile)                                |
| Ec/No  | Ratio of energy per modulating bit to the noise spectral density |
| ECSD   | Enhanced CSD                                                     |
| ECT    | Explicit Call Transfer supplementary service                     |
| ECTRA  | European Committee of Telecommunications Regulatory Affairs      |
| EDC    | Error Detection Code byte                                        |
| EDGE   | Enhanced Data rates for GSM Evolution                            |
| EEL    | Electric Echo Loss                                               |
| EF     | Elementary File (on the UICC)                                    |
| EFR    | Enhanced Full Rate                                               |
| EFS    | Error free seconds                                               |
| EGPRS  | Enhanced GPRS                                                    |
| EHPLMN | Equivalent Home PLMN                                             |
| EIR    | Equipment Identity Centre                                        |
|        | Equipment Identity Register                                      |
| EIRP   | Equivalent Isotropic Radiated Power                              |
| EL     | Echo Loss                                                        |

|         |                                                  |
|---------|--------------------------------------------------|
| EF      | Elementary File                                  |
| EM      | Element Manager                                  |
| EMC     | ElectroMagnetic Compatibility                    |
| eMLPP   | enhanced Multi-Level Precedence and Pre-emption  |
| EMMI    | Electrical Man Machine Interface                 |
| EPC     | Enhanced Power Control<br>Evolved Packet Core    |
| E-UTRA  | Evolved UTRA                                     |
| E-UTRAN | Evolved UTRAN                                    |
| EPS     | Evolved Packet System                            |
| EPCCH   | Enhanced Power Control Channel                   |
| EPROM   | Erasable Programmable Read Only Memory           |
| ERP     | Ear Reference Point<br>Equivalent Radiated Power |
| ERR     | Error                                            |
| ETNS    | European Telecommunications Numbering Space      |
| ETR     | ETSI Technical Report                            |
| ETS     | European Telecommunication Standard              |
| ETSI    | European Telecommunications Standards Institute  |
| etu     | elementary time unit                             |
| EUI     | End-User Identity                                |

### F

|         |                                           |
|---------|-------------------------------------------|
| FA      | Full Allocation<br>Fax Adaptor            |
| FAC     | Final Assembly Code                       |
| FACCH   | Fast Associated Control CHannel           |
| FACCH/F | Fast Associated Control Channel/Full rate |
| FACCH/H | Fast Associated Control Channel/Half rate |
| FACH    | Forward Access Channel                    |
| FAUSCH  | Fast Uplink Signalling Channel            |
| FAX     | Facsimile                                 |
| FB      | Frequency correction Burst                |
| FBI     | Feedback Information                      |
| FCCH    | Frequency Correction CHannel              |
| FCI     | File Control Information                  |
| FCP     | File Control Parameter                    |
| FCS     | Frame Check Sequence                      |
| FDD     | Frequency Division Duplex                 |
| FDM     | Frequency Division Multiplex              |
| FDMA    | Frequency Division Multiple Access        |
| FDN     | Fixed Dialling Number                     |
| FDR     | False transmit format Detection Ratio     |
| FEC     | Forward Error Correction                  |
| FER     | Frame Erasure Rate, Frame Error Rate      |
| FFS     | For Further Study                         |
| FH      | Frequency Hopping                         |
| FLO     | Flexible Layer One                        |
| FM      | Fault Management                          |
| FMC     | Fixed Mobile Convergence                  |
| FN      | Frame Number                              |
| FNUR    | Fixed Network User Rate                   |
| FP      | Frame Protocol                            |
| FPLMN   | Forbidden PLMN                            |
| FR      | Full Rate                                 |
| FTAM    | File Transfer Access and Management       |
| ftn     | forwarded-to number                       |

### G

|        |                                         |
|--------|-----------------------------------------|
| G-RNTI | GERAN Radio Network Temporary Identity  |
| GC     | General Control (SAP)                   |
| GCR    | Group Call Register                     |
| GERAN  | GSM EDGE Radio Access Network           |
| GGSN   | Gateway GPRS Support Node               |
| GID1   | Group Identifier (level 1)              |
| GID2   | Group Identifier (level 2)              |
| GMLC   | Gateway Mobile Location Centre          |
| GMM    | GPRS Mobility Management                |
| GSMC   | Gateway MSC                             |
| GMSK   | Gaussian Minimum Shift Keying           |
| GP     | Guard Period                            |
| GPA    | GSM PLMN Area                           |
| GPRS   | General Packet Radio Service            |
| GRA    | GERAN Registration Area                 |
| GSA    | GSM System Area                         |
| GSIM   | GSM Service Identity Module             |
| GSM    | Global System for Mobile communications |
| GSN    | GPRS Support Nodes                      |
| GT     | Global Title                            |
| GTP    | GPRS Tunneling Protocol                 |
| GTP-U  | GPRS Tunnelling Protocol for User Plane |
| GTT    | Global Text Telephony                   |
| GUP    | 3GPP Generic User Profile               |

### H

|         |                                                                                 |
|---------|---------------------------------------------------------------------------------|
| H-CSCF  | Home CSCF                                                                       |
| HANDO   | Handover                                                                        |
| HCS     | Hierarchical Cell Structure                                                     |
| HDLC    | High Level Data Link Control                                                    |
| HE      | Home Environment                                                                |
| HE-VASP | Home Environment Value Added Service Provider                                   |
| HF      | Human Factors                                                                   |
| HFN     | HyperFrame Number                                                               |
| HHO     | Hard Handover                                                                   |
| HLC     | High Layer Compatibility                                                        |
| HLR     | Home Location Register                                                          |
| HN      | Home Network                                                                    |
| HO      | Handover                                                                        |
| HOLD    | Call hold                                                                       |
| HPLMN   | Home Public Land Mobile Network                                                 |
| HPS     | Handover Path Switching                                                         |
| HPU     | Hand Portable Unit                                                              |
| HR      | Half Rate                                                                       |
| HRR     | Handover Resource Reservation                                                   |
| HSCSD   | High Speed Circuit Switched Data                                                |
| HSN     | Hopping Sequence Number                                                         |
| HSS     | Home Subscriber Server                                                          |
| HTTP    | Hyper Text Transfer Protocol                                                    |
| HTTPS   | Hyper Text Transfer Protocol Secure (https is http/1.1 over SSL, i.e. port 443) |
| HU      | Home Units                                                                      |

### I

|         |                                              |
|---------|----------------------------------------------|
| I-Block | Information Block                            |
| I-ETS   | Interim European Telecommunications Standard |
| I/O     | Input/Output                                 |
| I       | Information frames (RLP)                     |

|          |                                                |
|----------|------------------------------------------------|
| IA       | Incoming Access (closed user group SS)         |
| IAM      | Initial Address Message                        |
| IC       | Integrated Circuit                             |
|          | Interlock Code (CUG SS)                        |
| IC(pref) | Interlock Code of the preferential CUG         |
| ICB      | Incoming Calls Barred (within the CUG)         |
| ICC      | Integrated Circuit Card                        |
| ICCID    | Integrated Circuit Card IDentification         |
| ICGW     | Incoming Call Gateway                          |
| ICI      | Incoming Call Information                      |
| ICM      | In-Call Modification                           |
| ICMP     | Internet Control Message Protocol              |
| ICT      | Incoming Call Timer                            |
| ID       | Identifier                                     |
| IDL      | Interface Definition Language                  |
| IDN      | Integrated Digital Network                     |
| IDNNS    | Intra Domain NAS Node Selector                 |
| IE       | Information Element                            |
| IEC      | International Electrotechnical Commission      |
| IED      | Information Element Data                       |
| IEI      | Information Element Identifier                 |
| IEIDL    | Information Element Identifier Data Length     |
| IETF     | Internet Engineering Task Force                |
| IF       | Infrastructure                                 |
| IFD      | Interface Device                               |
| IFS      | Information Field Sizes                        |
| IFSC     | Information Field Size for the UICC            |
| IFSD     | Information Field Size for the Terminal        |
| IHOSS    | Internet Hosted Octet Stream Service           |
| IIOP     | Internet Inter-ORB Protocol                    |
| IK       | Integrity key                                  |
| IM       | Intermodulation                                |
|          | IP Multimedia                                  |
| IMA      | Inverse Multiplexing on ATM                    |
| IMC      | IMS Credentials                                |
| IMEI     | International Mobile Equipment Identity        |
| IMGI     | International mobile group identity            |
| IMPI     | IP Multimedia Private Identity                 |
| IMPU     | IP Multimedia PUblic identity                  |
| IMS      | IP Multimedia Subsystem                        |
| IMSI     | International Mobile Subscriber Identity       |
| IMT-2000 | International Mobile Telecommunications 2000   |
| IMUN     | International Mobile User Number               |
| IN       | Intelligent Network                            |
|          | Interrogating Node                             |
| INAP     | Intelligent Network Application Part           |
| INF      | INformation field                              |
| IP       | Internet Protocol                              |
| IP-CAN   | IP-Connectivity Access Network                 |
| IP-M     | IP Multicast                                   |
| IPv4     | Internet Protocol Version 4                    |
| IPv6     | Internet Protocol Version 6                    |
| IR       | Infrared                                       |
| IRP      | Integration Reference Point                    |
| ISC      | International Switching Centre                 |
| ISCP     | Interference Signal Code Power                 |
| ISDN     | Integrated Services Digital Network            |
| ISIM     | IM Services Identity Module                    |
| ISO      | International Organisation for Standardisation |
| ISP      | Internet Service Provider                      |
| ISUP     | ISDN User Part                                 |
| ITC      | Information Transfer Capability                |

|        |                                       |
|--------|---------------------------------------|
| ITU    | International Telecommunication Union |
| IUI    | International USIM Identifier         |
| IUT    | Implementation Under Test             |
| IWF    | InterWorking Function                 |
| I-WLAN | Interworking WLAN                     |
| IWMSC  | InterWorking MSC                      |
| IWU    | Inter Working Unit                    |

### J

|          |                                                  |
|----------|--------------------------------------------------|
| JAR file | Java Archive File                                |
| JCRE     | Java Card™ Run Time Environment                  |
| JD       | Joint Detection                                  |
| JNDI     | Java Naming Directory Interface                  |
| JP       | Joint Predistortion                              |
| JPEG     | Joint Photographic Experts Group                 |
| JTAPI    | Java Telephony Application Programming Interface |
| JVM      | Java™ Virtual Machine                            |

### K

|      |                                                                    |
|------|--------------------------------------------------------------------|
| k    | Windows size                                                       |
| K    | Constraint length of the convolutional code<br>USIM Individual key |
| kbps | kilo-bits per second                                               |
| Kc   | Ciphering key                                                      |
| Ki   | Individual subscriber authentication key                           |
| KSI  | Key Set Identifier                                                 |
| ksp  | kilo-symbols per second                                            |

### L

|         |                                                          |
|---------|----------------------------------------------------------|
| L1      | Layer 1 (physical layer)                                 |
| L2      | Layer 2 (data link layer)                                |
| L2ML    | Layer 2 Management Link                                  |
| L2R     | Layer 2 Relay                                            |
| L2R BOP | L2R Bit Orientated Protocol                              |
| L2R COP | L2R Character Orientated Protocol                        |
| L3      | Layer 3 (network layer)                                  |
| LA      | Location Area                                            |
| LAC     | Link Access Control<br>Location Area Code                |
| LAI     | Location Area Identity                                   |
| LAN     | Local Area Network                                       |
| LAPB    | Link Access Protocol Balanced                            |
| LAPDm   | Link Access Protocol on the Dm channel                   |
| LATA    | Local Access and Transport Area                          |
| LAU     | Location Area Update                                     |
| LCD     | Low Constrained Delay                                    |
| LCN     | Local Communication Network                              |
| LCP     | Link Control Protocol                                    |
| LCS     | Location Services                                        |
| LCSC    | LCS Client                                               |
| LCSS    | LCS Server                                               |
| LE      | Local Exchange                                           |
| LEN     | LENgth                                                   |
| LI      | Language Indication<br>Length Indicator<br>Line Identity |
| LLC     | Logical Link Control<br>Low Layer Compatibility          |

|       |                                               |
|-------|-----------------------------------------------|
| Lm    | Traffic channel with capacity lower than a Bm |
| LMSI  | Local Mobile Station Identity                 |
| LMU   | Location Measurement Unit                     |
| LN    | Logical Name                                  |
| LND   | Last Number Dialled                           |
| LNS   | L2TP Network Server                           |
| LPLMN | Local PLMN                                    |
| LR    | Location Register                             |
|       | Location Registration                         |
| LSA   | Localised Service Area                        |
| LSB   | Least Significant Bit                         |
| LSTR  | Listener SideTone Rating                      |
| LTE   | Local Terminal Emulator                       |
| LTZ   | Local Time Zone                               |
| LU    | Local Units                                   |
|       | Location Update                               |
| LV    | Length and Value                              |

### M

|       |                                                                        |
|-------|------------------------------------------------------------------------|
| M     | Mandatory                                                              |
| M     | Mandatory                                                              |
| MA    | Mobile Allocation                                                      |
|       | Multiple Access                                                        |
| MAC   | Medium Access Control (protocol layering context)                      |
|       | Message authentication code (encryption context)                       |
| MAC-A | MAC used for authentication and key agreement (TSG T WG3 context)      |
| MAC-I | MAC used for data integrity of signalling messages (TSG T WG3 context) |
| MACN  | Mobile Allocation Channel Number                                       |
| MAF   | Mobile Additional Function                                             |
| MAH   | Mobile Access Hunting supplementary service                            |
| MAHO  | Mobile Assisted Handover                                               |
| MAI   | Mobile Allocation Index                                                |
| MAIO  | Mobile Allocation Index Offset                                         |
| MAP   | Mobile Application Part                                                |
| MCC   | Mobile Country Code                                                    |
| MCI   | Malicious Call Identification supplementary service                    |
| MCML  | Multi-Class Multi-Link PPP                                             |
| Mcps  | Mega-chips per second                                                  |
| MCS   | Modulation and Coding Scheme                                           |
| MCU   | Media Control Unit                                                     |
| MD    | Mediation Device                                                       |
| MDL   | (mobile) Management (entity) - Data Link (layer)                       |
| MDS   | Multimedia Distribution Service                                        |
| ME    | Maintenance Entity                                                     |
|       | Mobile Equipment                                                       |
| MEF   | Maintenance Entity Function                                            |
| MEHO  | Mobile evaluated handover                                              |
| MER   | Message Error Ratio                                                    |
| MExE  | Mobile Execution Environment                                           |
| MF    | Master File                                                            |
|       | MultiFrame                                                             |
| MGCF  | Media Gateway Control Function                                         |
| MGCP  | Media Gateway Control Part                                             |
| MGT   | Mobile Global Title                                                    |
| MGW   | Media GateWay                                                          |
| MHEG  | Multimedia and Hypermedia Information Coding Expert Group              |
| MHS   | Message Handling System                                                |
| MIB   | Management Information Base                                            |
| MIC   | Mobile Interface Controller                                            |

|        |                                                             |
|--------|-------------------------------------------------------------|
| MIM    | Management Information Model                                |
| MIP    | Mobile IP                                                   |
| MIPS   | Million Instructions Per Second                             |
| MLC    | Mobile Location Centre                                      |
| MM     | Man Machine<br>Mobility Management<br>Multimedia            |
| MME    | Mobile Management Entity                                    |
| MMI    | Man Machine Interface                                       |
| MNC    | Mobile Network Code                                         |
| MNP    | Mobile Number Portability                                   |
| MO     | Mobile Originated                                           |
| MO-LR  | Mobile Originating Location Request                         |
| MO-SMS | Mobile Originated Short Message Service                     |
| MOHO   | Mobile Originated Handover                                  |
| MOS    | Mean Opinion Score                                          |
| MoU    | Memorandum of Understanding                                 |
| MP     | Multi-link PPP                                              |
| MPEG   | Moving Pictures Experts Group                               |
| MPH    | (mobile) Management (entity) - PHysical (layer) [primitive] |
| MPTY   | MultiParTY                                                  |
| MRF    | Media Resource Function                                     |
| MRP    | Mouth Reference Point                                       |
| MS     | Mobile Station                                              |
| MSB    | Most Significant Bit                                        |
| MSC    | Mobile Switching Centre                                     |
| MSCM   | Mobile Station Class Mark                                   |
| MSCU   | Mobile Station Control Unit                                 |
| MSE    | MExE Service Environment                                    |
| MSID   | Mobile Station Identifier                                   |
| MSIN   | Mobile Station Identification Number                        |
| MSISDN | Mobile Subscriber ISDN Number                               |
| MSP    | Multiple Subscriber Profile                                 |
| MSRN   | Mobile Station Roaming Number                               |
| MT     | Mobile Terminated<br>Mobile Termination                     |
| MT-LR  | Mobile Terminating Location Request                         |
| MT-SMS | Mobile Terminated Short Message Service                     |
| MTM    | Mobile-To-Mobile (call)                                     |
| MTP    | Message Transfer Part                                       |
| MTP3-B | Message Transfer Part level 3                               |
| MTU    | Maximum Transfer Unit                                       |
| MU     | Mark Up                                                     |
| MUI    | Mobile User Identifier                                      |
| MUMS   | Multi User Mobile Station                                   |
| MVNO   | Mobile Virtual Network Operator                             |

### N

|       |                                        |
|-------|----------------------------------------|
| NACC  | Network Assisted Cell Change           |
| NAD   | Node Address byte                      |
| NAI   | Network Access Identifier              |
| NAS   | Non-Access Stratum                     |
| NBAP  | Node B Application Part                |
| NB    | Normal Burst                           |
| NCELL | Neighbouring (of current serving) Cell |
| NBAP  | Node B Application Part                |
| NBIN  | A parameter in the hopping sequence    |
| NCC   | Network (PLMN) Colour Code             |
| NCH   | Notification CHannel                   |
| NCK   | Network Control Key                    |

|       |                                         |
|-------|-----------------------------------------|
| NCP   | Network Control Protocol                |
| NDC   | National Destination Code               |
| NDUB  | Network Determined User Busy            |
| NE    | Network Element                         |
| NEF   | Network Element Function                |
| NEHO  | Network evaluated handover              |
| NET   | NETwork                                 |
|       | Norme Europeenne de Télécommunications  |
| NEV   | NEVer                                   |
| NF    | Network Function                        |
| NI-LR | Network Induced Location Request        |
| NIC   | Network Independent Clocking            |
| NITZ  | Network Identity and Time Zone          |
| NM    | Network Manager                         |
| NMC   | Network Management Centre               |
| NMR   | Network Measurement Results             |
| NMO   | Network Mode of Operation               |
| NMS   | Network Management Subsystem            |
| NMSI  | National Mobile Station Identifier      |
| NNI   | Network-Node Interface                  |
| NO    | Network Operator                        |
| NP    | Network Performance                     |
| NPA   | Numbering Plan Area                     |
| NPI   | Numbering Plan Identifier               |
| NRI   | Network Resource Identifier             |
| NRM   | Network Resource Model                  |
| NRT   | Non-Real Time                           |
| NSAP  | Network Service Access Point            |
| NSAPI | Network Service Access Point Identifier |
| NSCK  | Network Subset Control Key              |
| NSDU  | Network service data unit               |
| NSS   | Network Sub System                      |
| Nt    | Notification (SAP)                      |
| NT    | Network Termination                     |
|       | Non Transparent                         |
| NTAAB | New Type Approval Advisory Board        |
| NTDD  | Narrow-band Time Division Duplexing     |
| NUA   | Network User Access                     |
| NUI   | National User / USIM Identifier         |
|       | Network User Identification             |
| NUP   | National User Part (SS7)                |
| NW    | Network                                 |

### O

|       |                                                   |
|-------|---------------------------------------------------|
| O     | Optional                                          |
| O&M   | Operations & Maintenance                          |
| OA    | Outgoing Access (CUG SS)                          |
| OACSU | Off-Air-Call-Set-Up                               |
| OCB   | Outgoing Calls Barred within the CUG              |
| OCCCH | ODMA Common Control Channel                       |
| OCF   | Open Card Framework                               |
| OCI   | Outgoing Call Information                         |
| OCNS  | Orthogonal Channel Noise Simulator                |
| OCT   | Outgoing Call Timer                               |
| OD    | Optional for operators to implement for their aim |
| ODB   | Operator Determined Barring                       |
| ODCCH | ODMA Dedicated Control Channel                    |
| ODCH  | ODMA Dedicated Channel                            |
| OLR   | Overall Loudness Rating                           |
| ODMA  | Opportunity Driven Multiple Access                |

|           |                                                                |
|-----------|----------------------------------------------------------------|
| ODTCH     | ODMA Dedicated Traffic Channel                                 |
| OID       | Object Identifier                                              |
| OFM       | Operational Feature Monitor                                    |
| OMC       | Operation and Maintenance Centre                               |
| OML       | Operations and Maintenance Link                                |
| OPLMN     | Operator Controlled PLMN (Selector List)                       |
| OR        | Optimal Routeing                                               |
| ORACH     | ODMA Random Access CHannel                                     |
| ORLCF     | Optimal Routeing for Late Call Forwarding                      |
| OS        | Operations System                                              |
| OSA       | Open Service Access                                            |
| OSI       | Open System Interconnection                                    |
| OSI RM    | OSI Reference Model                                            |
| OSP       | Octet Stream Protocol                                          |
| OSP:IHOSS | Octet Stream Protocol for Internet Hosted Octet Stream Service |
| OTA       | Over-The-Air                                                   |
| OTP       | One Time Password                                              |
| OVSF      | Orthogonal Variable Spreading Factor                           |

### P

|         |                                                         |
|---------|---------------------------------------------------------|
| P-CCPCH | Primary Common Control Physical Channel                 |
| P-CPIH  | Primary Common Pilot Channel                            |
| P-TMSI  | Packet TMSI                                             |
| PABX    | Private Automatic Branch eXchange                       |
| PACCH   | Packet Associated Control Channel                       |
| PAD     | Packet Assembler/Disassembler                           |
| PAGCH   | Packet Access Grant Channel                             |
| PAP     | Password Authentication Protocol                        |
| PAR     | Peak to Average Ratio                                   |
| PBID    | PhoneBook IDentifier                                    |
| PBCCH   | Packet Broadcast Control Channel                        |
| PBP     | Paging Block Periodicity                                |
| PBX     | Private Branch eXchange                                 |
| PC      | Power Control                                           |
|         | Personal Computer                                       |
| PCB     | Protocol Control Byte                                   |
| PCCC    | Parallel Concatenated Convolutional Code                |
| PCCCH   | Packet Common Control Channel                           |
| PCCH    | Paging Control Channel                                  |
| PCDE    | Peak Code Domain Error                                  |
| PCG     | Project Co-ordination Group                             |
| PCH     | Paging Channel                                          |
| PCK     | Personalisation Control Key                             |
| PCM     | Pulse Code Modulation                                   |
| PCMCIA  | Personal Computer Memory Card International Association |
| PCPCH   | Physical Common Packet Channel                          |
| PCS     | Personal Communication System                           |
| PCU     | Packet Control Unit                                     |
| PD      | Protocol Discriminator                                  |
|         | Public Data                                             |
| PDCP    | Packet Data Convergence Protocol                        |
| PDCH    | Packet Data Channel                                     |
| PDH     | Plesiochronous Digital Hierarchy                        |
| PDN     | Public Data Network                                     |
|         | Packet Data Network                                     |
| PDP     | Packet Data Protocol                                    |
| PDSCH   | Physical Downlink Shared Channel                        |
| PDTCH   | Packet Data Traffic Channel                             |
| PDU     | Protocol Data Unit                                      |
| PG      | Processing Gain                                         |

|          |                                                       |
|----------|-------------------------------------------------------|
| PH       | Packet Handler                                        |
|          | PHysical (layer)                                      |
| PHF      | Packet Handler Function                               |
| PHI      | Packet Handler Interface                              |
| PHS      | Personal Handyphone System                            |
| PHY      | Physical layer                                        |
| PhyCH    | Physical Channel                                      |
| PI       | Page Indicator                                        |
|          | Presentation Indicator                                |
| PICH     | Page Indicator Channel                                |
| PICS     | Protocol Implementation Conformance Statement         |
| PID      | Packet Identification                                 |
| PIN      | Personal Identification Number                        |
| PIXT     | Protocol Implementation eXtra information for Testing |
| PKCS     | Public-Key Cryptography Standards                     |
| PL       | Preferred Languages                                   |
| PLMN     | Public Land Mobile Network                            |
| PMD      | Physical Media Dependent                              |
| PN       | Pseudo Noise                                          |
| PNE      | Présentation des Normes Européennes                   |
| PNP      | Private Numbering Plan                                |
| POI      | Point Of Interconnection (with PSTN)                  |
| PoR      | Proof of Receipt                                      |
| POTS     | Plain Old Telephony Service                           |
| PP       | Point-to-Point                                        |
| PPCH     | Packet Paging Channel                                 |
| PPE      | Primitive Procedure Entity                            |
| PPF      | Paging Proceed Flag                                   |
| PPM      | Parts Per Million                                     |
| PPP      | Point-to-Point Protocol                               |
| PPS      | Protocol and Parameter Select (response to the ATR)   |
| PRACH    | Physical Random Access Channel                        |
|          | Packet Random Access Channel                          |
| Pref CUG | Preferential CUG                                      |
| PS       | Packet Switched                                       |
|          | Location Probability                                  |
| PSC      | Primary Synchronisation Code                          |
| PSCH     | Physical Shared Channel                               |
| PSE      | Personal Service Environment                          |
| PSPDN    | Packet Switched Public Data Network                   |
| PSTN     | Public Switched Telephone Network                     |
| PTCCH    | Packet Timing advance Control Channel                 |
| PTM      | Point-to-Multipoint                                   |
| PTM-G    | PTM Group Call                                        |
| PTM-M    | PTM Multicast                                         |
| PTP      | Point to point                                        |
| PU       | Payload Unit                                          |
| PUCT     | Price per Unit Currency Table                         |
| PUK      | PIN Unblocking Key                                    |
| PUSCH    | Physical Uplink Shared Channel                        |
| PVC      | Permanent Virtual Circuit                             |
| PW       | Pass Word                                             |

### Q

|      |                                            |
|------|--------------------------------------------|
| QA   | Q (Interface) - Adapter                    |
| QAF  | Q - Adapter Function                       |
| QoS  | Quality of Service                         |
| QPSK | Quadrature (Quaternary) Phase Shift Keying |

### R

|         |                                                                                                                                     |
|---------|-------------------------------------------------------------------------------------------------------------------------------------|
| R       | Value of Reduction of the MS transmitted RF power relative to the maximum allowed output power of the highest power class of MS (A) |
| R-APDU  | Response APDU                                                                                                                       |
| R-Block | Receive-ready Block                                                                                                                 |
| R-SGW   | Roaming Signalling Gateway                                                                                                          |
| R-TPDU  | Response TPDU                                                                                                                       |
| R99     | Release 1999                                                                                                                        |
| RA      | Routing Area                                                                                                                        |
|         | Random mode request information field                                                                                               |
| RAB     | Radio Access Bearer                                                                                                                 |
|         | Random Access Burst                                                                                                                 |
| RAC     | Routing Area Code                                                                                                                   |
| RACH    | Random Access Channel                                                                                                               |
| RADIUS  | Remote Authentication Dial In User Service                                                                                          |
| RAI     | Routing Area Identity                                                                                                               |
| RAN     | Radio Access Network                                                                                                                |
| RANAP   | Radio Access Network Application Part                                                                                               |
| RAND    | RANDom number (used for authentication)                                                                                             |
| RAT     | Radio Access Technology                                                                                                             |
| RAU     | Routing Area Update                                                                                                                 |
| RB      | Radio Bearer                                                                                                                        |
| RBER    | Residual Bit Error Ratio                                                                                                            |
| RDF     | Resource Description Format                                                                                                         |
| RDI     | Restricted Digital Information                                                                                                      |
| REC     | RECommendation                                                                                                                      |
| REJ     | REJect(ion)                                                                                                                         |
| REL     | RELease                                                                                                                             |
| Rel-4   | Release 4                                                                                                                           |
| Rel-5   | Release 5                                                                                                                           |
| REQ     | REQuest                                                                                                                             |
| RES     | user RESponse                                                                                                                       |
|         | 64-bit signed RESponse that is the output of the function f2 in a 3G AKA                                                            |
| RF      | Radio Frequency                                                                                                                     |
| RFC     | Request For Comments                                                                                                                |
|         | Radio Frequency Channel                                                                                                             |
| RFCH    | Radio Frequency CHannel                                                                                                             |
| RFE     | Routing Functional Identity                                                                                                         |
| RFN     | Reduced TDMA Frame Number                                                                                                           |
| RFU     | Reserved for Future Use                                                                                                             |
| RIM     | RAN Information Management                                                                                                          |
| RL      | Radio Link                                                                                                                          |
| RLC     | Radio Link Control                                                                                                                  |
| RLCP    | Radio Link Control Protocol                                                                                                         |
| RLP     | Radio Link Protocol                                                                                                                 |
| RLR     | Receiver Loudness Rating                                                                                                            |
| RLS     | Radio Link Set                                                                                                                      |
| RMS     | Root Mean Square (value)                                                                                                            |
| RNC     | Radio Network Controller                                                                                                            |
| RNS     | Radio Network Subsystem                                                                                                             |
| RNSAP   | Radio Network Subsystem Application Part                                                                                            |
| RNTABLE | Table of 128 integers in the hopping sequence                                                                                       |
| RNTI    | Radio Network Temporary Identity                                                                                                    |
| RPLMN   | Registered Public Land Mobile Network                                                                                               |
| RPOA    | Recognised Private Operating Agency                                                                                                 |
| RR      | Radio Resources                                                                                                                     |
| RRC     | Radio Resource Control                                                                                                              |
| RRM     | Radio Resource Management                                                                                                           |
| RSA     | Algorithm invented by Rivest, Adleman and Shamir                                                                                    |
| RSCP    | Received Signal Code Power                                                                                                          |

|        |                                     |
|--------|-------------------------------------|
| RSE    | Radio System Entity                 |
| RSL    | Radio Signalling Link               |
| RSSI   | Received Signal Strength Indicator  |
| RST    | Reset                               |
| RSVP   | Resource ReserVation Protocol       |
| RSZI   | Regional Subscription Zone Identity |
| RT     | Real Time                           |
| RTE    | Remote Terminal Emulator            |
| RTP    | Real Time Protocol                  |
| RU     | Resource Unit                       |
| RWB    | Resolution Bandwidth                |
| RX     | Receive                             |
| RXLEV  | Received signal level               |
| RXQUAL | Received Signal Quality             |

### S

|          |                                                                                     |
|----------|-------------------------------------------------------------------------------------|
| S-Block  | Supervisory Block                                                                   |
| S-CCPCH  | Secondary Common Control Physical Channel                                           |
| S-CPICH  | Secondary Common Pilot Channel                                                      |
| S-CSCF   | Serving CSCF                                                                        |
| S-RNTI   | SRNC Radio Network Temporary Identity                                               |
| SAAL     | Signalling ATM Adaptation Layer                                                     |
| SABM     | Set Asynchronous Balanced Mode                                                      |
| SACCH    | Slow Associated Control Channel                                                     |
| SACCH/C4 | Slow Associated Control CHannel/SDCCH/4                                             |
| SACCH/C8 | Slow Associated Control CHannel/SDCCH/8                                             |
| SACCH/T  | Slow Associated Control CHannel/Traffic channel                                     |
| SACCH/TF | Slow Associated Control CHannel/Traffic channel Full rate                           |
| SACCH/TH | Slow Associated Control CHannel/Traffic channel Half rate                           |
| SAD      | Source ADdress                                                                      |
| SAP      | Service Access Point                                                                |
| SAPI     | Service Access Point Identifier                                                     |
| SAR      | Segmentation and Reassembly                                                         |
| SAT      | SIM Application Toolkit                                                             |
| SB       | Synchronization Burst                                                               |
| SBLP     | Service Based Local Policy                                                          |
| SBSC     | Serving Base Station Controller                                                     |
| SBSS     | Serving Base Station Subsystem                                                      |
| SC       | Service Centre (used for SMS)                                                       |
|          | Service Code                                                                        |
| SCCH     | Synchronisation Control Channel                                                     |
| SCCP     | Signalling Connection Control Part                                                  |
| SCF      | Service Control Function (IN context), Service Capability Feature (VHE/OSA context) |
| SCH      | Synchronisation Channel                                                             |
| SCI      | Subscriber Controlled Input                                                         |
| SCN      | Sub-Channel Number                                                                  |
| SCP      | Service Control Point                                                               |
| SCTP     | S Common Transport Protocol                                                         |
| SCUDIF   | Service Change and UDI/RDI Fallback                                                 |
| SDCCH    | Stand-Alone Dedicated Control Channel                                               |
| SDH      | Synchronous Digital Hierarchy                                                       |
| SDL      | Specification Description Language                                                  |
| SDN      | Service Dialling Number                                                             |
| SDP      | Service Discovery Protocol (Bluetooth related)                                      |
|          | Session Description Protocol                                                        |
| SDT      | SDL Development Tool                                                                |
| SDU      | Service Data Unit                                                                   |
| SE       | Security Environment                                                                |
|          | Sending Entity                                                                      |

|          |                                                                                     |
|----------|-------------------------------------------------------------------------------------|
|          | Support Entity                                                                      |
| SEF      | Support Entity Function                                                             |
| SF       | Spreading Factor                                                                    |
| SFH      | Slow Frequency Hopping                                                              |
| SFI      | Short EF Identifier                                                                 |
| SFN      | System Frame Number                                                                 |
| SGSN     | Serving GPRS Support Node                                                           |
| SHCCH    | Shared Channel Control Channel                                                      |
| SI       | Screening Indicator                                                                 |
|          | Service Interworking                                                                |
|          | Supplementary Information (SIA=Supplementary Information A)                         |
| SIC      | Service Implementation Capabilities                                                 |
| SID      | Silence Descriptor                                                                  |
| SIM      | GSM Subscriber Identity Module                                                      |
| SIP      | Session Initiated Protocol                                                          |
| SIR      | Signal-to-Interference Ratio                                                        |
| SLA      | Service Level Agreement                                                             |
| SLPP     | Subscriber LCS Privacy Profile                                                      |
| SLR      | Send Loudness Rating                                                                |
| SLTM     | Signalling Link Test Message                                                        |
| SM       | Session Management                                                                  |
|          | Short Message                                                                       |
| SMDS     | Switched Multimegabit Data Service                                                  |
| SME      | Short Message Entity                                                                |
| SMG      | Special Mobile Group                                                                |
| SMI      | Structure of Management Information (RFC 1155)                                      |
| SMLC     | Serving Mobile Location Centre                                                      |
| SMS      | Short Message Service                                                               |
| SMS-CB   | SMS Cell Broadcast                                                                  |
| SMS-PP   | Short Message Service/Point-to-Point                                                |
| SMS-SC   | Short Message Service - Service Centre                                              |
| Smt      | Short message terminal                                                              |
| SN       | Serial Number                                                                       |
|          | Serving Network                                                                     |
|          | Subscriber Number                                                                   |
| SNDPC    | Sub-Network Dependent Convergence Protocol                                          |
| SNMP     | Simple Network Management Protocol                                                  |
| SNR      | Serial NumberR                                                                      |
| SOA      | Suppress Outgoing Access (CUG SS)                                                   |
| SoLSA    | Support of Localised Service Area                                                   |
| SoR      | Steering of Roaming                                                                 |
| SP       | Switching Point                                                                     |
|          | Service Provider                                                                    |
| SPC      | Signalling Point Code                                                               |
|          | Suppress Preferential CUG                                                           |
| SPCK     | Service Provider Control Key                                                        |
| SPI      | Security Parameters Indication                                                      |
| SQN      | Sequence number                                                                     |
| SRB      | Signalling Radio Bearer                                                             |
| SRES     | Signed RESponse (authentication value returned by the SIM or by the USIM in 2G AKA) |
| SRNC     | Serving Radio Network Controller                                                    |
| SRNS     | Serving RNS                                                                         |
| SS       | Supplementary Service                                                               |
|          | System Simulator                                                                    |
| SS7      | Signalling System No. 7                                                             |
| SSC      | Secondary Synchronisation Code                                                      |
|          | Supplementary Service Control string                                                |
| SSCOP    | Service Specific Connection Oriented Protocol                                       |
| SSCF     | Service Specific Co-ordination Function                                             |
| SSCF-NNI | Service Specific Coordination Function – Network Node Interface                     |
| SSCS     | Service Specific Convergence Sublayer                                               |
| SSDT     | Site Selection Diversity Transmission                                               |

|         |                                                        |
|---------|--------------------------------------------------------|
| SSE     | Service Specific Entities                              |
| SSF     | Service Switching Function                             |
| SSN     | Sub-System Number                                      |
| SSSAR   | Service Specific Segmentation and Re-assembly sublayer |
| STC     | Signalling Transport Converter                         |
| STMR    | SideTone Masking Rating                                |
| STP     | Signalling Transfer Point                              |
| STTD    | Space Time Transmit Diversity                          |
| SuM     | Subscription Management                                |
| SVC     | Switched virtual circuit                               |
| SVN     | Software Version Number                                |
| SW      | Status Word<br>Software                                |
| SW1/SW2 | Status Word 1/Status Word 2                            |

### T

|          |                                                                    |
|----------|--------------------------------------------------------------------|
| T-SGW    | Transport Signalling Gateway                                       |
| T        | Timer<br>Transparent<br>Type only                                  |
| TA       | Terminal Adaptation<br>Timing Advance                              |
| TAC      | Type Approval Code                                                 |
| TAF      | Terminal Adaptation Function                                       |
| TAR      | Toolkit Application Reference                                      |
| TB       | Transport Block                                                    |
| TBF      | Temporary Block Flow                                               |
| TBR      | Technical Basis for Regulation                                     |
| TC       | Transaction Capabilities<br>TransCoder<br>Transmission Convergence |
| TCH      | Traffic Channel                                                    |
| TCH/F    | A full rate TCH                                                    |
| TCH/F2,4 | A full rate data TCH ( $\leq 2,4\text{kbit/s}$ )                   |
| TCH/F4,8 | A full rate data TCH ( $4,8\text{kbit/s}$ )                        |
| TCH/F9,6 | A full rate data TCH ( $9,6\text{kbit/s}$ )                        |
| TCH/FS   | A full rate Speech TCH                                             |
| TCH/H    | A half rate TCH                                                    |
| TCH/H2,4 | A half rate data TCH ( $\leq 2,4\text{kbit/s}$ )                   |
| TCH/H4,8 | A half rate data TCH ( $4,8\text{kbit/s}$ )                        |
| TCH/HS   | A half rate Speech TCH                                             |
| TC-TR    | Technical Committee Technical Report                               |
| TCI      | Transceiver Control Interface                                      |
| TCP      | Transmission Control Protocol                                      |
| TD-CDMA  | Time Division-Code Division Multiple Access                        |
| TDD      | Time Division Duplex                                               |
| TDMA     | Time Division Multiple Access                                      |
| TDoc     | Temporary Document                                                 |
| TE       | Terminal Equipment                                                 |
| TE9      | Terminal Equipment 9 (ETSI sub-technical committee)                |
| Tei      | Terminal endpoint identifier                                       |
| TEID     | Tunnel End Point Identifier                                        |
| TF       | Transport Format                                                   |
| TFA      | TransFer Allowed                                                   |
| TFC      | Transport Format Combination                                       |
| TFCI     | Transport Format Combination Indicator                             |
| TFCS     | Transport Format Combination Set                                   |
| TFI      | Transport Format Indicator<br>Temporary Flow Identity              |
| TFIN     | Transport Format Indicator                                         |

|       |                                                                                     |
|-------|-------------------------------------------------------------------------------------|
| TFP   | TransFer Prohibited                                                                 |
| TFS   | Transport Format Set                                                                |
| TFT   | Traffic Flow Template                                                               |
| TI    | Transaction Identifier                                                              |
| TLLI  | Temporary Logical Link Identity                                                     |
| TLS   | Transport Layer Security                                                            |
| TLV   | Tag Length Value                                                                    |
| TM    | Telecom Management                                                                  |
| TMF   | Telecom Management Forum                                                            |
| TMN   | Telecom Management Network                                                          |
| TMSI  | Temporary Mobile Subscriber Identity                                                |
| TN    | Termination Node                                                                    |
|       | Timeslot Number                                                                     |
| TO    | Telecom Operations Map                                                              |
| TOA   | Time of Arrival                                                                     |
| TON   | Type Of Number                                                                      |
| TP    | Third Party                                                                         |
| TPC   | Transmit Power Control                                                              |
| TPDU  | Transfer Protocol Data Unit                                                         |
| TR    | Technical Report                                                                    |
| TRAU  | Transcoder and Rate Adapter Unit                                                    |
| TrCH  | Transport Channel                                                                   |
| TRX   | Transceiver                                                                         |
| TS    | Technical Specification                                                             |
|       | Teleservice                                                                         |
|       | Time Slot                                                                           |
| TSC   | Training Sequence Code                                                              |
| TSDI  | Transceiver Speech & Data Interface                                                 |
| TSG   | Technical Specification Group                                                       |
| TSTD  | Time Switched Transmit Diversity                                                    |
| TTCN  | Tree and Tabular Combined Notation                                                  |
| TTI   | Transmission Timing Interval                                                        |
| TUP   | Telephone User Part (SS7)                                                           |
| TV    | Type and Value                                                                      |
| TX    | Transmit                                                                            |
| TXPWR | Transmit PoWeR; Tx power level in the MS_TXPWR_REQUEST and MS_TXPWR_CONF parameters |

### U

|                 |                                                  |
|-----------------|--------------------------------------------------|
| U-RNTI          | UTRAN Radio Network Temporary Identity           |
| UARFCN          | UTRA Absolute Radio Frequency Channel Number     |
| UARFN           | UTRA Absolute Radio Frequency Number             |
| UART            | Universal Asynchronous Receiver and Transmitter  |
| UCS2            | Universal Character Set 2                        |
| UDD             | Unconstrained Delay Data                         |
| UDI             | Unrestricted Digital Information                 |
| UDP             | User Datagram Protocol                           |
| UDUB            | User Determined User Busy                        |
| UDCH            | User-plane Dedicated CHannel                     |
| UE              | User Equipment                                   |
| UE <sub>R</sub> | User Equipment with ODMA relay operation enabled |
| UI              | User Interface                                   |
|                 | Unnumbered Information (Frame)                   |
| UIA             | 3G Integrity Algorithm                           |
| UIC             | Union Internationale des Chemins de Fer          |
| UL              | Uplink (Reverse Link)                            |
| UM              | Unacknowledged Mode                              |
| UML             | Unified Modelling Language                       |
| UMS             | User Mobility Server                             |

|       |                                            |
|-------|--------------------------------------------|
| UMSC  | UMTS Mobile Services Switching Centre      |
| UMTS  | Universal Mobile Telecommunications System |
| UNI   | User-Network Interface                     |
| UP    | User Plane                                 |
| UPCM1 | Uniform PCM Interface (13-bit)             |
| UPD   | Up to date                                 |
| UPT   | Universal Personal Telecommunication       |
| URA   | User Registration Area                     |
|       | UTRAN Registration Area                    |
| URAN  | UMTS Radio Access Network                  |
| URB   | User Radio Bearer                          |
| URI   | Uniform Resource Identifier                |
| URL   | Uniform Resource Locator                   |
| USAT  | USIM Application Toolkit                   |
| USB   | Universal Serial Bus                       |
| USC   | UE Service Capabilities                    |
| USCH  | Uplink Shared Channel                      |
| USF   | Uplink State Flag                          |
| USIM  | Universal Subscriber Identity Module       |
| USSD  | Unstructured Supplementary Service Data    |
| UT    | Universal Time                             |
| UTRA  | Universal Terrestrial Radio Access         |
| UTRAN | Universal Terrestrial Radio Access Network |
| UUI   | User-to-User Information                   |
| UUS   | Uu Stratum                                 |
|       | User-to-User Signalling                    |

### V

|          |                                              |
|----------|----------------------------------------------|
| V        | Value only                                   |
| VA       | Voice Activity factor                        |
| VAD      | Voice Activity Detection                     |
| VAP      | Videotex Access Point                        |
| VASP     | Value Added Service Provider                 |
| VBR      | Variable Bit Rate                            |
| VBS      | Voice Broadcast Service                      |
| VC       | Virtual Circuit                              |
| VGCS     | Voice Group Call Service                     |
| VHE      | Virtual Home Environment                     |
| VLR      | Visitor Location Register                    |
| VMSC     | Visited MSC                                  |
| VoIP     | Voice Over IP                                |
| VPLMN    | Visited Public Land Mobile Network           |
| VPN      | Virtual Private Network                      |
| VSC      | Videotex Service Centre                      |
| V(SD)    | Send state variable                          |
| VTX host | The components dedicated to Videotex service |

### W

|       |                                        |
|-------|----------------------------------------|
| WAE   | Wireless Application Environment       |
| WAP   | Wireless Application Protocol          |
| WBEM  | Web Based Enterprise Management        |
| WCDMA | Wideband Code Division Multiple Access |
| WDP   | Wireless Datagram Protocol             |
| WG    | Working Group                          |
| WIM   | Wireless Identity Module               |
| WIN   | Wireless Intelligent Network           |

|         |                                           |
|---------|-------------------------------------------|
| WLAN    | Wireless Local Area Network               |
| WLAN UE | WLAN User Equipment                       |
| WPA     | Wrong Password Attempts (counter)         |
| WS      | Work Station                              |
| WSP     | Wireless Session Protocol                 |
| WTA     | Wireless Telephony Applications           |
| WTAI    | Wireless Telephony Applications Interface |
| WTDD    | Wideband Time Division Duplexing          |
| WTLS    | Wireless Transport Layer Security         |
| WTP     | Wireless Transaction Protocol             |
| WTX     | Waiting Time eXtenstion                   |
| WWT     | Work Waiting Time                         |
| WWW     | World Wide Web                            |

### X

|      |                                                                                      |
|------|--------------------------------------------------------------------------------------|
| XID  | eXchange IDentifier                                                                  |
| XMAC | exXpected Message Authentication Code (calculated by the USIM application in 3G AKA) |
| XML  | eXtensible Markup Language                                                           |
| XRES | EXpected user RESponse                                                               |

### Y

<void>

### Z

|    |           |
|----|-----------|
| ZC | Zone Code |
|----|-----------|

# --- 5 Equations

|                                          |                                                                                                                                                                                                                                                                                                                                              |
|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| $\frac{\text{CPICH}}{I_{\text{or}}}$     | The ratio of the received energy per PN chip of the CPICH to the total transmit power spectral density at the Node_B (SS) antenna connector.                                                                                                                                                                                                 |
| DPCH                                     | Average energy per PN chip for DPCH.                                                                                                                                                                                                                                                                                                         |
| $\frac{\text{DPCH}}{I_{\text{or}}}$      | The ratio of the transmit energy per PN chip of the DPCH to the total transmit power spectral density at the Node_B antenna connector.                                                                                                                                                                                                       |
| $\frac{\text{DPCCH}}{I_{\text{or}}}$     | The ratio of the transmit energy per PN chip of the DPCCH to the total transmit power spectral density at the Node B antenna connector.                                                                                                                                                                                                      |
| $\frac{\text{DPDCH}}{I_{\text{or}}}$     | The ratio of the transmit energy per PN chip of the DPDCH to the total transmit power spectral density at the Node B antenna connector.                                                                                                                                                                                                      |
| $E_c$                                    | Average energy per PN chip.                                                                                                                                                                                                                                                                                                                  |
| $\frac{E_c}{I_{\text{or}}}$              | The ratio of the average transmit energy per PN chip for different fields or physical channels to the total transmit power spectral density.                                                                                                                                                                                                 |
| $F_{\text{uw}}$                          | Frequency of unwanted signal                                                                                                                                                                                                                                                                                                                 |
| $I_o$                                    | The total received power spectral density, including signal and interference, as measured at the UE antenna connector.                                                                                                                                                                                                                       |
| $I_{\text{oac}}$                         | The power spectral density of the adjacent frequency channel as measured at the UE antenna connector.                                                                                                                                                                                                                                        |
| $I_{\text{oc}}$                          | The power spectral density of a band limited white noise source (simulating interference from cells, which are not defined in a test procedure) as measured at the UE antenna connector. The power spectral density of a band limited white noise source (simulating interference from other cells) as measured at the UE antenna connector. |
| $I_{\text{or}}$                          | The total transmit power spectral density of the Forward down link at the base station Node_B antenna connector.                                                                                                                                                                                                                             |
| $\hat{I}_{\text{or}}$                    | The received power spectral density of the down link as measured at the UE antenna connector.                                                                                                                                                                                                                                                |
| $I_{\text{ouw}}$                         | Unwanted signal power level.                                                                                                                                                                                                                                                                                                                 |
| OCNS                                     | Average energy per PN chip for the OCNS.                                                                                                                                                                                                                                                                                                     |
| $\frac{\text{OCNS}}{I_{\text{or}}}$      | The ratio of the average transmit energy per PN chip for the OCNS to the total transmit power spectral density.                                                                                                                                                                                                                              |
| $P - \text{CCPCH}$                       | Average* energy per PN chip for P-CCPCH.                                                                                                                                                                                                                                                                                                     |
| $P - \text{CCPCH} \frac{E_c}{I_o}$       | The ratio of the received P-CCPCH energy per chip to the total received power spectral density at the UE antenna connector.                                                                                                                                                                                                                  |
| $\frac{P - \text{CCPCH}}{I_{\text{or}}}$ | The ratio of the average* transmit energy per PN chip for the P-CCPCH to the total transmit power spectral density.                                                                                                                                                                                                                          |
| $P - \text{CPICH}$                       | Average* energy per PN chip for P-CPICH.                                                                                                                                                                                                                                                                                                     |
| PICH                                     | Average* energy per PN chip for PICH.                                                                                                                                                                                                                                                                                                        |

|                                   |                                                                                                                                                             |
|-----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| $\frac{\text{PICH}}{I_{or}}$      | The ratio of the received energy per PN chip of the PICH to the total transmit power spectral density at the <u>Node B</u> (SS) antenna connector.          |
| $\text{PCCPCH} \frac{E_c}{I_o}$   | The ratio of the received PCCPCH energy per chip to the total received power spectral density at the UE antenna connector.                                  |
| $\frac{\text{PCCPCH}}{I_{or}}$    | The ratio of the average transmit energy per PN chip for the PCCPCH to the total transmit power spectral density.                                           |
| $\frac{\sum \text{DPCH}}{I_{or}}$ | The ratio of the sum DPCH_Ex for one service in case of multicode to the total transmit power spectral density of the downlink at the BS antenna connector. |
| $S - \text{CCPCH}$                | Average energy per PN chip for S-CCPCH.                                                                                                                     |
| $S - \text{CPICH}$                | Average* energy per PN chip for S-CPICH.                                                                                                                    |
| $\text{SCH}$                      | Average* energy per PN chip for SCH.                                                                                                                        |
| $\text{SCCPCH}$                   | Average energy per PN chip for SCCPCH.                                                                                                                      |

\*Note: Averaging period for energy/power of discontinuously transmitted channels should be defined.

## --- Annex A (informative): Change history

| TSG SA# | SA Doc.   | SA1 Doc   | Spec   | CR   | Rev | Rel   | Cat | Subject/Comment                                                                                       | Old   | New   | WI      |
|---------|-----------|-----------|--------|------|-----|-------|-----|-------------------------------------------------------------------------------------------------------|-------|-------|---------|
| SP-07   | -         | -         | 21.905 | -    | -   | -     | -   | Approved at SA#07 as version 3.0.0                                                                    |       | 3.0.0 |         |
| SP-08   | SP-000209 | S1-000369 | 21.905 | 0001 |     | R99   | B   | New Abbreviations and Definitions for R99, language alignment and editorial changes                   | 3.0.0 | 3.1.0 |         |
| 08/2000 | -         | -         | 21.905 | -    | -   | -     | -   | MCC correction of CR001 implementation; editorial update.                                             | 3.1.0 | 3.1.1 |         |
| SP-09   | SP-000380 | S1-000477 | 21.905 | 0002 |     | R99   | D   | New Abbreviations and Definitions for R99                                                             | 3.1.1 | 3.2.0 |         |
| SP-09   | SP-000381 | S1-000627 | 21.905 | 0003 |     | R4    | D   | Change of Name of MExE                                                                                | 3.1.1 | 4.0.0 |         |
| SP-10   | SP-000659 | S1-000731 | 21.905 | 0004 |     | Rel-4 | B   | Introduces ASCII definition                                                                           | 4.0.0 | 4.1.0 | ASCII   |
| SP-10   | SP-000659 | S1-000736 | 21.905 | 0005 | 1   | Rel-4 | B   | Inclusion of GSM 01.04 v 7.0.0 acronyms and abbreviations in the vocabulary                           | 4.0.0 | 4.1.0 | CORRECT |
| SP-11   | SP-010038 | S1-010233 | 21.905 | 0006 |     | Rel-4 | D   | Editorial changes and new definitions                                                                 | 4.1.0 | 4.2.0 | Vocab   |
| SP-11   | SP-010038 | S1-010234 | 21.905 | 0007 |     | Rel-4 | B   | Inclusion of commonly used definition contained in 23.122                                             | 4.1.0 | 4.2.0 | Vocab   |
| SP-12   | SP-010256 | S1-010366 | 21.905 | 0008 |     | Rel-4 | F   | Corrections to the vocabulary requested by RAN-4                                                      | 4.2.0 | 4.3.0 | Vocab   |
| SP-12   | SP-010256 | S1-010582 | 21.905 | 0009 |     | Rel-4 | F   | CR to 21.905 on Definitions in 22.101 subscription and service provider                               | 4.2.0 | 4.3.0 | Vocab   |
| SP-12   | SP-010258 | S1-010537 | 21.905 | 0010 |     | Rel-5 | D   | Addition of definition of Service Provider and Subscription. Modification of definition of Subscriber | 4.3.0 | 5.0.0 | Vocab   |
| SP-13   | SP-010430 | S1-010649 | 21.905 | 0013 |     | Rel-5 | B   | CR to 21.905v5.0.0 (Rel-5) on Alignment of definitions requested by RAN 4                             | 5.0.0 | 5.1.0 | Vocab   |
| SP-13   | SP-010431 | S1-010838 | 21.905 | 0016 |     | Rel-5 | B   | CR to 21.905 version 5.0.0 Nomenclature for GTT                                                       | 5.0.0 | 5.1.0 | GTT     |
| SP-14   | SP-010671 | S1-011276 | 21.905 | 0021 | 1   | Rel-5 | F   | Definition of Local Services                                                                          | 5.1.0 | 5.2.0 | IMS     |
| SP-15   | SP-020046 | S1-020393 | 21.905 | 0030 |     | Rel-5 | B   | CR to 21.905: new definition of the term 'service'                                                    | 5.2.0 | 5.3.0 | TEI     |
| SP-15   | SP-020063 | S1-020431 | 21.905 | 0031 |     | Rel-5 | B   | CR 21.905 Rel. 5 Introduction of new abbreviations derived of the approval of 3GPP TS 23.236          | 5.2.0 | 5.3.0 | PSS-E   |
| SP-15   | SP-020046 | S1-020452 | 21.905 | 0032 |     | Rel-5 | B   | CR 21.905 Rel.5 B Introduction of the definitions of "pre-pay" and "post-pay" billing                 | 5.2.0 | 5.3.0 | TEI     |
| SP-15   | SP-020046 | S1-020526 | 21.905 | 0033 |     | Rel-5 | F   | CR to 21.905: Replacement of the term UMTS with 3GPP system                                           | 5.2.0 | 5.3.0 | TEI     |
| SP-15   | SP-020046 | S1-020527 | 21.905 | 0034 |     | Rel-5 | B   | CR to 21.905: missing abbreviations                                                                   | 5.2.0 | 5.3.0 | TEI     |
| SP-15   | SP-020046 | S1-020528 | 21.905 | 0035 |     | Rel-5 | B   | CR to 21.905: new definition of the term 'application'                                                | 5.2.0 | 5.3.0 | TEI     |
| SP-15   | SP-020046 | S1-020617 | 21.905 | 0036 |     | Rel-5 | B   | CR to 21.905: definitions of online and offline charging                                              | 5.2.0 | 5.3.0 | TEI     |
| SP-15   | SP-020046 | S1-020620 | 21.905 | 0037 |     | Rel-5 | B   | CR to 21.905: Improved definition of the term "application"                                           | 5.2.0 | 5.3.0 | TEI     |
| SP-16   | SP-020243 | S1-020973 | 21.905 | 0038 |     | Rel-5 | F   | CR to 21.905 5.3.0 - removal of obsolete reference                                                    | 5.3.0 | 5.4.0 | Vocab   |
| SP-17   | SP-020596 |           | 21.905 | 0039 | 1   | Rel-5 | F   | Addition of GERAN definitions and abbreviations                                                       | 5.4.0 | 5.5.0 | TEI     |
| SP-17   | SP-020596 |           | 21.905 | 0040 | 1   | Rel-5 | F   | Addition of missing GSM/GPRS abbreviations                                                            | 5.4.0 | 5.5.0 | TEI     |
| SP-17   | SP-020555 | S1-021762 | 21.905 | 0041 |     | Rel-6 | B   | CR to 21.905 definitions from TR 22.951                                                               | 5.4.0 | 6.0.0 | TEI     |
| SP-17   | SP-020555 | S1-021715 | 21.905 | 0042 |     | Rel-6 | F   | Enhancement of the definition of the 'Subscriber'                                                     | 5.4.0 | 6.0.0 | TEI     |
| SP-18   | SP-020654 | S1-022223 | 21.905 | 0043 |     | Rel-6 | D   | Update to 3GPP TR 21.905, Vocabulary for 3GPP Specifications                                          | 6.0.0 | 6.1.0 | TEI6    |
| SP-18   | SP-020666 | S1-022264 | 21.905 | 0044 |     | Rel-6 | B   | CR to 21.905 to introduce WLAN terminology                                                            | 6.0.0 | 6.1.0 | WLAN    |
| SP-19   | SP-030012 | S1-030238 | 21.905 | 0046 | -   | Rel-6 | A   | CR on Entities of the mobile system                                                                   | 6.1.0 | 6.2.0 | OAM-AR  |

|       |           |           |        |      |   |       |   |                                                                                                                                                       |       |        |                |
|-------|-----------|-----------|--------|------|---|-------|---|-------------------------------------------------------------------------------------------------------------------------------------------------------|-------|--------|----------------|
| SP-20 | SP-030247 | S1-030391 | 21.905 | 0047 | - | Rel-6 | B | Addition of the definition and acronym of 3GPP Generic User Profile                                                                                   | 6.2.0 | 6.3.0  | GUP            |
| SP-20 | SP-030240 | S1-030576 | 21.905 | 0050 | - | Rel-6 | A | Correction of acronyms in TR21.905                                                                                                                    | 6.2.0 | 6.3.0  | TEI4           |
| SP-21 | SP-030456 | S1-030971 | 21.905 | 0052 | - | Rel-6 | A | Correction of the Defintion of CDR                                                                                                                    | 6.3.0 | 6.4.0  | OAM-CH         |
| SP-22 | SP-030694 | S1-031145 | 21.905 | 0053 | - | Rel-6 | F | Terminology additions for IP-CAN and IP-CAN bearer                                                                                                    | 6.4.0 | 6.5.0  | TEI6           |
| SP-22 | SP-030694 | S1-031311 | 21.905 | 0054 | - | Rel-6 | F | Modified base station definition                                                                                                                      | 6.4.0 | 6.5.0  | Vocab          |
| SP-23 | SP-040087 | S1-040115 | 21.905 | 0055 | - | Rel-6 | B | Acronyms for the Flexible Layer One                                                                                                                   | 6.5.0 | 6.6.0  | FLOGER         |
| SP-23 | SP-040107 | S5-042112 | 21.905 | 0056 | - | Rel-6 | F | Add Subscription Management (SuM) Definition and Abbreviation to SA1's 21.905 - Align with SA5's 32.140/1, 32.171/2/... & 3GPP Work Plan (WI Acronym) | 6.5.0 | 6.6.0  | SuM            |
| SP-24 | SP-040286 | S1-040507 | 21.905 | 0057 | - | Rel-6 | F | Inclusion of ANP abbreviation as requested by SA3                                                                                                     | 6.6.0 | 6.7.0  | Vocab          |
| SP-24 | SP-040476 | -         | 21.905 | 0058 | 2 | Rel-6 | F | TR 21.905 Addition WLAN UE definition and classes of equipment and abbreviation                                                                       | 6.6.0 | 6.7.0  | WLAN           |
| SP-27 | SP-050055 | S1-050143 | 21.905 | 0061 | - | Rel-6 | A | Introduction of RAN Information Management                                                                                                            | 6.7.0 | 6.8.0  | TEI5           |
| SP-28 | SP-050213 | S1-050487 | 21.905 | 0062 | - | Rel-6 | F | Correction of OSA acronym                                                                                                                             | 6.8.0 | 6.9.0  | Vocab          |
| SP-29 | SP-050509 | S1-050780 | 21.905 | 0065 | - | Rel-6 | A | Abbreviation for SCUDIF                                                                                                                               | 6.9.0 | 6.10.0 | Vocab          |
| SP-29 | SP-050515 | S1-050781 | 21.905 | 0066 | - | Rel-6 | F | Definition and abbreviation for DSAC                                                                                                                  | 6.9.0 | 6.10.0 | Vocab          |
| SP-29 | SP-050524 | S1-050828 | 21.905 | 0067 | - | Rel-7 | B | Introduction of SBLP abbreviation                                                                                                                     | 6.9.0 | 7.0.0  | Vocab          |
| SP-31 | SP-060033 | S1-060266 | 21.905 | 0068 | - | Rel-7 | F | Correction of terminology                                                                                                                             | 7.0.0 | 7.1.0  | NSP-CR         |
| SP-32 | SP-060428 | -         | 21.905 | 0069 | 1 | Rel-7 | F | TISPAN UE definition                                                                                                                                  | 7.1.0 | 7.2.0  | FBI            |
| SP-35 | SP-070231 | -         | 21.905 | 0071 | 3 | Rel-7 | F | Terminology clarification for User Equipment and User Equipment components                                                                            | 7.2.0 | 7.3.0  | Vocab          |
| SP-35 | SP-070135 | S1-070248 | 21.905 | 0072 | - | Rel-8 | D | Adding FMC to terms and abbreviations                                                                                                                 | 7.3.0 | 8.0.0  | Vocab          |
| SP-36 | SP-070475 | S1-070442 | 21.905 | 0074 | 1 | Rel-8 | A | Addition of "Steering of Roaming" to definitions and abbreviations                                                                                    | 8.0.0 | 8.1.0  | TEI            |
| SP-37 | SP-070562 | S1-070949 | 21.905 | 76   |   | Rel-8 | B | To define 'Service Continuity' in the vocabulary                                                                                                      | 8.1.0 | 8.2.0  | TEI8           |
| SP-37 | SP-070562 | S1-070986 | 21.905 | 77   |   | Rel-8 | B | Proposal to add E-UTRA and E-UTRAN                                                                                                                    | 8.1.0 | 8.2.0  | TEI8           |
| SP-37 | SP-070562 | S1-071102 | 21.905 | 75   | 1 | Rel-8 | B | Proposal to add Evolved Packet System Evolved Packet Core                                                                                             | 8.1.0 | 8.2.0  | TEI8           |
| SP-37 | SP-070562 | S1-071233 | 21.905 | 78   | 2 | Rel-8 | C | NP definition                                                                                                                                         | 8.1.0 | 8.2.0  | TEI8           |
| SP-38 | SP-070848 | S1-071893 | 21.905 | 0079 | 1 | Rel-8 | B | Addition of definitions of an End-User and End-User Identity                                                                                          | 8.2.0 | 8.3.0  | EUI            |
| SP-39 | SP-080045 | S1-080276 | 21.905 | 0080 | 2 | Rel-8 | F | Proposal to add abbreviation for Evolved Packet Core                                                                                                  | 8.3.0 | 8.4.0  | TEI8           |
| SP-39 | SP-080045 | S1-080275 | 21.905 | 0081 | 2 | Rel-8 | F | Correction of UICC definition                                                                                                                         | 8.3.0 | 8.4.0  | TEI8           |
| SP-40 | SP-080298 | S1-080565 | 21.905 | 0082 | 1 | Rel-8 | B | Addition of definition of Pilot Identity                                                                                                              | 8.4.0 | 8.5.0  | TEI8           |
| SP-41 | SP-080493 | S1-082395 | 21.905 | 0083 | 2 | Rel-8 | B | Add definitions and abbreviations related to Home NodeB and Home eNodeB                                                                               | 8.5.0 | 8.6.0  | TEI8           |
| SP-42 | SP-080769 | S1-083441 | 21.905 | 0089 | 1 | Rel-9 | B | Addition of definition of IMS Credentials and IMC abbreviation                                                                                        | 8.6.0 | 9.0.0  | CIMS_3G<br>PP2 |
| SP-43 | SP-090080 | S1-090167 | 21.905 | 0092 | 1 | Rel-9 | A | Introduce the definition of CSG manager (Mirror CR to rel-9)                                                                                          | 9.0.0 | 9.1.0  | HomeNB         |
| SP-43 | SP-090081 | S1-090160 | 21.905 | 0094 | 2 | Rel-9 | A | Editorial changes in IMC                                                                                                                              | 9.0.0 | 9.1.0  | CIMS_3G        |

|       |           |           |        |      |   |       |   |                                               |       |       |       |
|-------|-----------|-----------|--------|------|---|-------|---|-----------------------------------------------|-------|-------|-------|
|       |           |           |        |      |   |       |   | definition                                    |       |       | PP2   |
| SP-44 | SP-090373 | S1-091277 | 21.905 | 0095 | 1 | Rel-9 | F | Align definition of Allowed CSG list          | 9.1.0 | 9.2.0 | TEI-9 |
| SP-45 | SP-090477 | S1-093056 | 21.905 | 0096 | - | Rel-9 | B | CSG Lists Definition                          | 9.2.0 | 9.3.0 | EHNB  |
| SP-45 | SP-090478 | S1-093356 | 21.905 | 0097 | 1 | Rel-9 | B | Adding definition of IMS Multimedia Telephony | 9.2.0 | 9.3.0 | TEI9  |
| SP-46 | SP-090844 | S1-094273 | 21.905 | 0100 | 1 | Rel-9 | F | Clarify the term "Active Set" in 21.905       | 9.3.0 | 9.4.0 | TEI9  |
