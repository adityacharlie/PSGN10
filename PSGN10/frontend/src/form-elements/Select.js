import { Select } from 'antd';

export default function CustomSelect(props){
    const { Option } = Select;
    const { options, placeholder } = props;

    function onChange(value) {
        console.log(`selected ${value}`);
    }

    return (
        <Select
            showSearch
            style={{ width: 200 }}
            placeholder={placeholder}
            onChange={onChange}
            filterOption={(input, option) =>
              option.children.toLowerCase().indexOf(input.toLowerCase()) >= 0
            }
        >
        {
            options.map(each => {
                return (
                    <Option key={each.name} value={each.name}>{each.name}</Option>
                )
            })
        }
        </Select>
    )
}