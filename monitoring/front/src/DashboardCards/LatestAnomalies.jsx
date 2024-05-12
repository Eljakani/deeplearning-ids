import React, { useState, useEffect } from 'react';
import { Layout } from 'antd';
import { 
    ArrowDownOutlined,
    ArrowUpOutlined,
    BugOutlined,
    ArrowsAltOutlined,
} from '@ant-design/icons';
import { Card, Statistic } from 'antd';
import useSWR from 'swr'
import { Empty } from 'antd';
import { List, Spin} from 'antd';
import { Button, Modal } from 'antd';




const LatestAnomalies = ({data, isLoading}) => {
    const [isModalOpen, setIsModalOpen] = useState(false);
    const [selectedItem, setSelectedItem] = useState(null);
    const handleModalLoad = (item) => {
        setSelectedItem(item);
        setIsModalOpen(true);
    }

    return (
        <>
        <Modal
            title="Anomaly Details"
            visible={isModalOpen}
            onOk={() => setIsModalOpen(false)}
            onCancel={() => setIsModalOpen(false)}
            footer={[
                <Button key="back" onClick={() => setIsModalOpen(false)}>
                    Close
                </Button>,
            ]}
        >
            <p>IP Source: {selectedItem?.ip_source}</p>
            <p>IP Destination: {selectedItem?.ip_destination}</p>
            <p>Port Source: {selectedItem?.port_source}</p>
            <p>Port Destination: {selectedItem?.port_destination}</p>
            <p>Protocol: {selectedItem?.protocol}</p>
            <p>Timestamp: {Date(selectedItem?.timestamp).toString()}</p>

        </Modal>

        <Card bordered={false} title="Latest Anomalies">
            <Spin spinning={isLoading}>
            {data?.length > 0 ? (
                <List
                itemLayout="horizontal"
                dataSource={data}
                renderItem={(item, index) => (
                  <List.Item>
                    <List.Item.Meta
                      avatar={<BugOutlined />}
                      title={<a onClick={() => handleModalLoad(item)}>{item.ip_source}</a>}
                      description='Anomaly detected in the network'
                    />
                  </List.Item>
                )}
              />
            ) : (
                <Empty />
            )}
            </Spin>
        
      </Card>
      </>
    );
};

export default LatestAnomalies;