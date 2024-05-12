import React, { useState, useEffect } from 'react';
import { Layout } from 'antd';
import { 
    ArrowDownOutlined,
    ArrowUpOutlined,
    BugOutlined,
    ArrowsAltOutlined,
} from '@ant-design/icons';
import { Card, Statistic } from 'antd';
import CountUp from 'react-countup';
const formatter = (value) => <CountUp end={value} separator="," />;



const Anomalies = ({data, isLoading}) => {
    
    return (
        <Card bordered={false}>
        <Statistic
          title="Anomalies"
          value={data.anomalies}
          precision={2}
          loading={isLoading}
          valueStyle={{ color: '#cf1322' }}
          prefix={<BugOutlined />}
          formatter={formatter}
        />
      </Card>
    );
};

export default Anomalies;