import React, { useState, useEffect } from 'react';
import { Layout } from 'antd';
import { 
    ArrowDownOutlined,
    ArrowUpOutlined,
    BugOutlined,
    ArrowsAltOutlined,
} from '@ant-design/icons';
import { Card, Col, Row, Statistic } from 'antd';
import { Space } from 'antd';
import useSWR from 'swr'
import Anomalies from './DashboardCards/Anomalies';
import AllPackets from './DashboardCards/AllPackets';
import LatestAnomalies from './DashboardCards/LatestAnomalies';
import { Spin } from 'antd';

const Dashboard = () => {
    const fetcher = (...args) => fetch(...args).then(res => res.json())
    const { data, error, isLoading } = useSWR('http://localhost:3000/overview', fetcher, { refreshInterval: 1000 });
    
    

    return (
        <Space direction="vertical" size="middle" style={{ display: 'flex' }}>
            <Spin spinning={isLoading} fullscreen />
            {data && (
                <>
                    <Row gutter={16}>
                    <Col span={12}>
                        <AllPackets data={data} isLoading={isLoading} />
                    </Col>
                    <Col span={12}>
                        <Anomalies data={data} isLoading={isLoading} />
                    </Col>
                    </Row>
                    <Row gutter={16}>
                        <Col span={20}>
                            <LatestAnomalies data={data.latest_anomalies} isLoading={isLoading} />
                        </Col>
                        <Col span={4}>
                            
                        </Col>
                    </Row>
                </>
            )}  
        </Space>
    );
};

export default Dashboard;