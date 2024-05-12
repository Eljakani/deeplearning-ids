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


const AllPackets = ({data, isLoading}) => {
  
    return (
        <Card bordered={false}>
        <Statistic
          title="All Packets"
          value={data.all_packets}
          precision={2}
          loading={isLoading}
          valueStyle={{ color: '#3f8600' }}
          prefix={<ArrowsAltOutlined />}
          formatter={formatter}
        />
      </Card>
    );
};

export default AllPackets;