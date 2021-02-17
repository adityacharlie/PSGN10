import React, { useState, useEffect } from 'react';
import BaseScreen from "./BaseScreen";
import { Table } from "antd";
import axios from "axios";

export default function LeagueScreen(props) {
    const [fixtures, setFixtures] = useState([]);

    useEffect( () => {
        axios
            .get("/core/fixtures/all/")
            .then(response => {
                console.log(response.data);
                setFixtures(response.data)
            })
            .finally(() => {
            })
    }, []);

    const columns = [
       {
        title: '',
        dataIndex: 'time',
        key: 'time',
      },
      {
        title: '',
        dataIndex: 'teamA',
        key: 'teamA',
      },
      {
        title: '',
        dataIndex: 'teamB',
        key: 'teamB',
      },
    ];

    return (
        <BaseScreen>
            <div className="league-header-container">
                <Table columns={columns} dataSource={fixtures} />
            </div>
        </BaseScreen>
    )
}



