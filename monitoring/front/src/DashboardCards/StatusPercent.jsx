import React, { useState, useEffect } from 'react';
import { Flex, Progress, Slider, Typography } from 'antd';
import { Card } from 'antd';



const StatusPercent = ({data, isLoading}) => {
    const formatPercent = (anomalies, all_packets) => {
        if (all_packets === 0) {
            return 0;
        }
        // format the percentage to 2 decimal places
        return parseFloat((anomalies / all_packets) * 100).toFixed(2);
    };
    
    return (
        <Card bordered={false} style={{ height: '100%',display:'flex',justifyContent:'center',alignItems:'center'}}>
        <Typography.Title level={5}>Anomaly Rate</Typography.Title>
        <Progress
          type="circle"
          percent={formatPercent(data.anomalies, data.all_packets)}
          steps={{
            count: 10,
            gap: 4,
          }}
          trailColor="rgba(0, 0, 0, 0.06)"
          strokeWidth={10}
        />
    </Card>
    );
};

export default StatusPercent;