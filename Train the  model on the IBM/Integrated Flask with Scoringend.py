#!/usr/bin/env python
# coding: utf-8

# In[1]:


{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "36d2fcbc",
   "metadata": {},
   "source": [
    "## SCORING ENDPOINT IN IBM CLOUD"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "4b47acb8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Scoring response\n",
      "-1\n",
      "The Website is not Legitimate... BEWARE!!\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "\n",
    "# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.\n",
    "API_KEY = \"cWGD5yTjEpEGtqPpvHPDBElN5eXFS7eh2JRDyUWhySMW\"\n",
    "token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={\"apikey\":\n",
    " API_KEY, \"grant_type\": 'urn:ibm:params:oauth:grant-type:apikey'})\n",
    "mltoken = token_response.json()[\"access_token\"]\n",
    "\n",
    "header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}\n",
    "\n",
    "# NOTE: manually define and pass the array(s) of values to be scored in the next line\n",
    "payload_scoring = {\"input_data\": [{\"field\": [[\"UsingIP\",\"LongURL\",\"ShortURL\",\"Symbol@\",\"Redirecting//\",\"PrefixSuffix-\",\"SubDomains\",\"HTTPS\",\"DomainRegLen\",\"Favicon\",\"NonStdPort\",\"HTTPSDomainURL\",\"RequestURL\",\"AnchorURL\",\"LinksInScriptTags\",\"ServerFormHandler\",\"InfoEmail\",\"AbnormalURL\",\"WebsiteForwarding\",\"StatusBarCust\",\"DisableRightClick\",\"UsingPopupWindow\",\"IframeRedirection\",\"AgeofDomain\",\"DNSRecording\",\"WebsiteTraffic\",\"PageRank\",\"GoogleIndex\",\"LinksPointingToPage\",\"StatsReport\"\n",
    "]], \"values\": [[1,1,1,1,1,-1,-1,-1,-1,1,1,1,1,-1,-1,1,1,1,0,1,1,1,1,-1,-1,-1,-1,1,0,1]]}]}\n",
    "\n",
    "response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/084b5c52-f617-40ef-a0e8-3e6cf79ae447/predictions?version=2022-11-06', json=payload_scoring,\n",
    " headers={'Authorization': 'Bearer ' + mltoken})\n",
    "print(\"Scoring response\")\n",
    "predictions=response_scoring.json()\n",
    "#print(predictions)\n",
    "pred=print(predictions['predictions'][0]['values'][0][0])\n",
    "if(pred != 1):\n",
    "    print(\"The Website is secure.. Continue\")\n",
    "else:\n",
    "    print(\"The Website is not Legitimate... BEWARE!!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "40a673bc",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c00b2ab7",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}


# In[ ]:
