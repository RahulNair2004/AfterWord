import React from 'react'
import {useParams} from 'react-router-dom';

const CaseDetails = () => {

    const {caseId} = useParams();
  
    return (
    <h1>CaseDetails - View Investigation {caseId}</h1>
  )
}

export default CaseDetails